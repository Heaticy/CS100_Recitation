#!/usr/bin/env python3
"""Synthesize cached per-paragraph speech with Volcengine Doubao speech v2."""
import argparse
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
import uuid

import requests

ROOT=Path(__file__).resolve().parents[1]
ENDPOINT='https://openspeech.bytedance.com/api/v3/tts/unidirectional'


def duration(path):
    return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(path)],text=True))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--project',type=Path,default=ROOT/'build/narration/project.json')
    ap.add_argument('--key-file',type=Path)
    ap.add_argument('--workers',type=int,default=2)
    ap.add_argument('--pages',nargs='*',type=int)
    args=ap.parse_args();out=args.project.parent
    key=os.environ.get('VOLC_TTS_API_KEY')
    if not key:
        f=args.key_file or out/'.tts-key'
        key=f.read_text().strip()
    project=json.loads(args.project.read_text()); voice=project['voice']
    audio=out/'audio';audio.mkdir(exist_ok=True)
    def run(seg):
        path=audio/(seg['id']+'.mp3');meta=audio/(seg['id']+'.json')
        digest=hashlib.sha256(json.dumps({'voice':voice,'text':seg['speech']},sort_keys=True,ensure_ascii=False).encode()).hexdigest()
        if path.exists() and meta.exists():
            old=json.loads(meta.read_text())
            if old.get('request_sha256')==digest:return old
        headers={'X-Api-Key':key,'X-Api-Resource-Id':voice['resource_id'],
                 'X-Api-Request-Id':str(uuid.uuid4()),'Content-Type':'application/json'}
        payload={'user':{'uid':'cs100-r5-narration'},'req_params':{
            'text':seg['speech'],'speaker':voice['speaker'],
            'audio_params':{'format':'mp3','sample_rate':24000,'speech_rate':voice['speech_rate']}}}
        for attempt in range(5):
            try:
                chunks=[];success=False
                with requests.post(ENDPOINT,headers=headers,json=payload,stream=True,timeout=(20,180)) as r:
                    if r.status_code!=200:
                        raise RuntimeError(f'HTTP {r.status_code}')
                    for line in r.iter_lines():
                        if not line:continue
                        line=line.decode().removeprefix('data:').strip()
                        if not line:continue
                        obj=json.loads(line)
                        code=obj.get('code')
                        if code not in (0,20000000):
                            msg=str(obj.get('message','')).replace(key,'[redacted]')
                            raise RuntimeError(f'provider {code}: {msg[:180]}')
                        if obj.get('data'):chunks.append(base64.b64decode(obj['data']))
                        if code==20000000:success=True
                if not success or not chunks:raise RuntimeError('Incomplete or empty speech response')
                tmp=path.with_suffix('.part.mp3');tmp.write_bytes(b''.join(chunks))
                seconds=duration(tmp)
                if seconds<0.2:raise RuntimeError('Audio too short')
                tmp.replace(path)
                result={'id':seg['id'],'page':seg['page'],'duration':seconds,
                        'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                        'request_sha256':digest}
                meta.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
                return result
            except Exception as e:
                if attempt==4:raise RuntimeError(f'{seg["id"]}: {str(e).replace(key,"[redacted]")}') from None
                time.sleep(min(2**attempt,15))
        raise AssertionError('unreachable')
    segments=[s for s in project['segments'] if not args.pages or s['page'] in args.pages]
    results=[];done=0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures=[pool.submit(run,s) for s in segments]
        for future in as_completed(futures):
            results.append(future.result());done+=1
            if done%10==0 or done==len(segments):
                print(f'Synthesized {done}/{len(segments)} segments; audio so far {sum(x["duration"] for x in results)/60:.1f} min',flush=True)
    requested_count=len(results)
    results=[json.loads((audio/(s['id']+'.json')).read_text()) for s in project['segments'] if (audio/(s['id']+'.json')).exists()]
    total=sum(x['duration'] for x in results)
    (out/'speech-summary.json').write_text(json.dumps({'segments':len(results),'speech_seconds':total,
        'audio_bytes':sum(x['bytes'] for x in results),'voice':voice},ensure_ascii=False,indent=2)+'\n')
    print(f'Complete: {len(results)} segments, {total/60:.2f} minutes of real provider speech.',flush=True)

if __name__=='__main__':main()
