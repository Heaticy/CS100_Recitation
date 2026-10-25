#!/usr/bin/env python3
"""Build a paced, focus-animated 1080p video from real per-paragraph TTS."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import wave

ROOT=Path(__file__).resolve().parents[1]
RATE=48000
FPS=10


def probe(path):
    return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(path)],text=True))


def ass_time(t):
    c=round(t*100)
    return f'{c//360000}:{c//6000%60:02}:{c//100%60:02}.{c%100:02}'


def srt_time(t):
    ms=round(t*1000)
    return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'


def pace(project,out,target):
    durations={s['id']:json.loads((out/'audio'/f'{s["id"]}.json').read_text())['duration'] for s in project['segments']}
    voice=sum(durations.values())
    pauses={s['id']:s['pause'] for s in project['segments']}
    base=sum(pauses.values())
    tempo=1.0
    if voice+base>target:
        tempo=min(1.10,max(1.0,voice/(target-base)))
    else:
        left=target-voice-base
        # Prefer pauses at questions, code and diagrams over slowing every sentence.
        byid={s['id']:s for s in project['segments']}
        for _ in range(12):
            active={sid:(3 if val>=3 else 1) for sid,val in pauses.items()
                    if val < (16 if byid[sid]['page'] in (43,45,47,49,51,53,55) else 7)}
            if not active or left<0.01:break
            weights=sum(active.values());used=0
            for sid,weight in active.items():
                cap=16 if byid[sid]['page'] in (43,45,47,49,51,53,55) else 7
                add=min(cap-pauses[sid],left*weight/weights)
                pauses[sid]+=add;used+=add
            left-=used
        if left>0.01:tempo=max(0.94,voice/(target-sum(pauses.values())))
    result={'original_speech_seconds':voice,'base_pause_seconds':base,'tempo':tempo,
            'pause_seconds':sum(pauses.values()),'planned_seconds':voice/tempo+sum(pauses.values()),
            'target_seconds':target,'pauses':pauses}
    (out/'pacing.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    return result


ASS_HEADER='''[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
ScaledBorderAndShadow: yes
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Focus,Noto Sans CJK SC,28,&H00FFFFFF,&H00FFFFFF,&H0000BFFF,&H00000000,0,0,0,0,100,100,0,0,1,3,0,7,0,0,0,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''


def add_focus(events,start,end,focus):
    if not focus or end-start<0.4:return
    x,y,w,h=focus['rect']
    x=max(15,min(1900,x));y=max(100,min(1000,y))
    w=max(30,min(1908-x,w));h=max(25,min(1030-y,h))
    # Fading vector outlines keep the original code readable.
    shape=f'm 0 0 l {w} 0 l {w} {h} l 0 {h} l 0 0'
    tags=f'{{\\an7\\pos({x},{y})\\fad(200,200)\\1c&H00C8FF&\\1a&HEC&\\3c&H009FDF&\\3a&H10&\\bord3\\shad0\\p1}}'
    events.append(f'Dialogue: 0,{ass_time(start)},{ass_time(end)},Focus,,0,0,0,,{tags}{shape}{{\\p0}}')
    px=max(2,x-24);py=y+min(h/2-8,24)
    pointer=f'{{\\an7\\move({px-10:.1f},{py:.1f},{px:.1f},{py:.1f},0,350)\\fad(150,150)\\1c&H009FDF&\\1a&H00&\\bord0\\shad0\\p1}}m 0 0 l 18 9 l 0 18 l 0 0{{\\p0}}'
    events.append(f'Dialogue: 1,{ass_time(start)},{ass_time(end)},Focus,,0,0,0,,{pointer}')


def captions(text):
    chunks=[];buf=''
    pieces=re.findall(r'[^，。！？；\n]+[，。！？；]?|\n',text)
    for piece in pieces:
        piece=piece.strip()
        if not piece:continue
        if len(buf)+len(piece)<=44:buf+=piece
        else:
            if buf:chunks.append(buf);buf=''
            while len(piece)>44:
                cut=piece.rfind(' ',15,43)
                if cut<0:cut=32
                chunks.append(piece[:cut].strip());piece=piece[cut:].strip()
            buf=piece
    if buf:chunks.append(buf)
    return chunks or [text]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--project',type=Path,default=ROOT/'build/narration/project.json')
    ap.add_argument('--target-minutes',type=float,default=45)
    ap.add_argument('--workers',type=int,default=3)
    ap.add_argument('--pages',nargs='*',type=int)
    ap.add_argument('--prepare-only',action='store_true')
    ap.add_argument('--tempo',type=float,help='Reuse a verified speaking tempo when patching a clip')
    args=ap.parse_args();out=args.project.parent.resolve()
    project=json.loads(args.project.read_text()); plan=pace(project,out,args.target_minutes*60)
    if args.tempo is not None:
        if not 0.90<=args.tempo<=1.10:raise SystemExit('Tempo must stay within natural speech range')
        plan['tempo']=args.tempo
        plan['planned_seconds']=plan['original_speech_seconds']/args.tempo+plan['pause_seconds']
        (out/'pacing.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
    segmap={s['id']:s for s in project['segments']}
    (out/'page-audio').mkdir(exist_ok=True);(out/'clips').mkdir(exist_ok=True);(out/'focus').mkdir(exist_ok=True)
    slides=[s for s in project['slides'] if not args.pages or s['page'] in args.pages]
    def page_audio(slide):
        pcm=bytearray();local=[];events=[]
        for sid in slide['segments']:
            seg=segmap[sid];start=len(pcm)/(RATE*2)
            cmd=['ffmpeg','-v','error','-threads','1','-i',str(out/'audio'/f'{sid}.mp3'),
                 '-af',f'atempo={plan["tempo"]:.8f}', '-ar',str(RATE),'-ac','1','-f','s16le','-']
            raw=subprocess.check_output(cmd);pcm.extend(raw)
            speech_end=len(pcm)/(RATE*2)
            pause=plan['pauses'][sid]
            pcm.extend(b'\0\0'*round(pause*RATE))
            end=len(pcm)/(RATE*2)
            local.append({'id':sid,'start':start,'speech_end':speech_end,'end':end,'text':seg['text']})
            focus=seg.get('focus')
            if focus and focus.get('sequence'):
                seq=focus['sequence']
                for k,part in enumerate(seq):
                    a=start+(speech_end-start)*part['at']+.12
                    b=start+(speech_end-start)*seq[k+1]['at']-.10 if k+1<len(seq) else end-.12
                    add_focus(events,a,b,part)
            else:
                add_focus(events,start+.15,end-.12,focus)
        # Constant frame boundaries make segment joins and chapter times deterministic.
        seconds=math.ceil(len(pcm)/(RATE*2)*FPS)/FPS
        pcm.extend(b'\0\0'*max(0,round(seconds*RATE)-len(pcm)//2))
        wav=out/'page-audio'/f'p{slide["page"]:03}.wav'
        with wave.open(str(wav),'wb') as w:
            w.setnchannels(1);w.setsampwidth(2);w.setframerate(RATE);w.writeframes(pcm)
        ass=out/'focus'/f'p{slide["page"]:03}.ass';ass.write_text(ASS_HEADER+'\n'.join(events)+'\n')
        return {'page':slide['page'],'duration':seconds,'segments':local,'focus_events':len(events)//2}
    prepared={}
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs={pool.submit(page_audio,s):s for s in slides}
        for i,f in enumerate(as_completed(futs),1):
            item=f.result();prepared[item['page']]=item
            if i%10==0 or i==len(slides):print(f'Prepared page audio and focus: {i}/{len(slides)}',flush=True)
    manifest=[];cursor=0
    for slide in slides:
        item=prepared[slide['page']];item['start']=cursor;item['end']=cursor+item['duration'];item['title']=slide['title']
        manifest.append(item);cursor=item['end']
    (out/'timeline.json').write_text(json.dumps({'duration':cursor,'pages':manifest,'pacing':plan,
        'subtitle_alignment':'paragraph anchors; within-paragraph caption timing is proportional'},ensure_ascii=False,indent=2)+'\n')
    print(f'Planned finished duration: {cursor/60:.2f} minutes; tempo {plan["tempo"]:.3f}',flush=True)
    if args.prepare_only:return
    def render(slide):
        no=slide['page'];dest=out/'clips'/f'p{no:03}.mp4';item=prepared[no]
        wav=out/'page-audio'/f'p{no:03}.wav';ass=out/'focus'/f'p{no:03}.ass'
        signature=hashlib.sha256(b'1080p-10fps-ass-v1'+(out/slide['image']).read_bytes()+wav.read_bytes()+ass.read_bytes()).hexdigest()
        marker=dest.with_suffix('.signature')
        if dest.exists() and marker.exists() and marker.read_text().strip()==signature:
            return {'page':no,'file':dest.name,'bytes':dest.stat().st_size,'cached':True}
        cmd=['ffmpeg','-v','error','-y','-loop','1','-framerate',str(FPS),'-i',str(out/slide['image']),
             '-i',str(wav),'-t',f'{item["duration"]:.3f}',
             '-vf',f'ass={ass.as_posix()},format=yuv420p',
             '-af','loudnorm=I=-16:TP=-1.5:LRA=11',
             '-c:v','libx264','-preset','veryfast','-tune','stillimage','-crf','18',
             '-r',str(FPS),'-threads','2','-c:a','aac','-b:a','128k','-ar',str(RATE),'-ac','1',
             '-movflags','+faststart',str(dest)]
        subprocess.run(cmd,check=True,timeout=max(300,item['duration']*8))
        marker.write_text(signature+'\n')
        return {'page':no,'file':dest.name,'bytes':dest.stat().st_size,'cached':False}
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs=[pool.submit(render,s) for s in slides]
        for i,f in enumerate(as_completed(futs),1):
            f.result()
            print(f'Rendered animated slide: {i}/{len(slides)}',flush=True)
    if args.pages:
        concat=out/'preview-concat.txt'
        concat.write_text(''.join("file '"+(out/'clips'/f'p{s["page"]:03}.mp4').as_posix()+"'\n" for s in slides))
        dest=out/'preview.mp4'
        subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(concat),'-c','copy','-movflags','+faststart',str(dest)],check=True)
        print('Preview:',dest,flush=True);return
    concat=out/'concat.txt'
    concat.write_text(''.join("file '"+(out/'clips'/f'p{s["page"]:03}.mp4').as_posix()+"'\n" for s in slides))
    srt=[];counter=0
    for page in manifest:
        for seg in page['segments']:
            lines=captions(seg['text']);weights=[max(1,len(t)) for t in lines];total=sum(weights);pos=seg['start']
            for line,weight in zip(lines,weights):
                finish=pos+(seg['speech_end']-seg['start'])*weight/total
                counter+=1
                if len(line)>25:
                    split=line.rfind(' ',12,28)
                    if split<0:split=23
                    line=line[:split]+'\n'+line[split:].lstrip()
                srt.append(f'{counter}\n{srt_time(page["start"]+pos)} --> {srt_time(page["start"]+finish)}\n{line}\n')
                pos=finish
    sub=out/'CS100_Recitation5_口播字幕.srt';sub.write_text('\n'.join(srt),encoding='utf-8')
    chapter_pages={1:'课程导入',4:'为什么需要指针',11:'动态分配与堆栈',24:'生命周期与内存区域',31:'释放责任与常见错误',42:'指针与宏：带做练习',41:'总结与致谢'}
    starts=[(p['start'],chapter_pages[p['page']]) for p in manifest if p['page'] in chapter_pages]
    meta=[';FFMETADATA1','title=CS100 Recitation 5：C语言内存管理','comment=豆包语音合成；课件重点引导；包含练习解析']
    chapters=[]
    for i,(start,title) in enumerate(starts):
        end=starts[i+1][0] if i+1<len(starts) else cursor
        meta+=['[CHAPTER]','TIMEBASE=1/1000',f'START={round(start*1000)}',f'END={round(end*1000)}','title='+title]
        chapters.append({'start':start,'end':end,'title':title})
    metadata=out/'chapters.ffmeta';metadata.write_text('\n'.join(meta)+'\n')
    manuscript=['CS100 Recitation 5：C语言内存管理｜视频口播稿',
        '制作说明（不朗读）：含练习解析，按真实合成音频与停顿生成时间轴；PDF页码和页脚标号均对应本次课件快照。',
        f'成片计划时长：{int(cursor)//60}分{int(cursor)%60:02}秒；视频顺序为课堂、练习、致谢。','']
    slide_map={s['page']:s for s in project['slides']}
    for idx,page in enumerate(manifest,1):
        slide=slide_map[page['page']]
        footer=slide.get('footer') or '无底部标号'
        manuscript.append(f'### 【视频第{idx}页｜PDF P{page["page"]}｜底部{footer}｜{slide["title"]}】[{srt_time(page["start"])} — {srt_time(page["end"])}]')
        for seg in page['segments']:
            manuscript.append(f'[{srt_time(page["start"]+seg["start"])} — {srt_time(page["start"]+seg["speech_end"])}] '+seg['text'])
            gap=seg['end']-seg['speech_end']
            if gap>=2:manuscript.append(f'（停顿{gap:.1f}秒，供阅读或思考）')
        manuscript.append('')
    (out/'CS100_Recitation5_口播稿.txt').write_text('\n'.join(manuscript)+'\n')
    (out/'chapters.txt').write_text('\n'.join(f'{int(t)//3600:02}:{int(t)//60%60:02}:{int(t)%60:02} {title}' for t,title in starts)+'\n')
    dest=out/'CS100_Recitation5_口播教学.mp4'
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(concat),
                    '-i',str(metadata),'-i',str(sub),'-map','0:v:0','-map','0:a:0','-map','2:0',
                    '-map_metadata','1','-map_chapters','1','-c:v','copy','-c:a','copy','-c:s','mov_text',
                    '-metadata:s:s:0','language=zho','-metadata:s:s:0','title=中文（段落同步）',
                    '-movflags','+faststart',str(dest)],check=True)
    audio=out/'CS100_Recitation5_口播音频.m4a'
    subprocess.run(['ffmpeg','-v','error','-y','-i',str(dest),'-vn','-c:a','copy',str(audio)],check=True)
    info=probe(dest)
    summary={'file':dest.name,'bytes':dest.stat().st_size,'duration':float(info['format']['duration']),
             'width':1920,'height':1080,'fps':FPS,'slides':len(slides),
             'focus_events':sum(x['focus_events'] for x in manifest),'chapters':chapters,
             'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
    (out/'delivery.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
