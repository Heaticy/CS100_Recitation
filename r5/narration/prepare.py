#!/usr/bin/env python3
"""Prepare the user's script and a read-only PDF snapshot for narrated video."""
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

import pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent

def clean(text):
    return '\n'.join(x.strip() for x in text.splitlines()).strip()

def speech(text):
    replacements = {
        'CS100': 'CS一百', 'C17': 'C十七',
        'sizeof(struct Point)': 'struct Point的大小',
        'sizeof(struct Node)': 'struct Node的大小',
        'sizeof(int *)': 'int指针的大小',
        'sizeof(int)': 'int类型的大小',
        'p->x': 'p箭头x', 'head->next': 'head箭头next',
        '&point': 'point的地址', '&local': 'local的地址',
        '&global': 'global的地址', '&n': 'n的地址',
        '*p = 42': '将p指向的对象赋值为四十二',
        'int *tmp': 'int指针tmp', 'int *p': 'int指针p',
        'int *q': 'int指针q', 'struct Node *next': 'Node指针next',
        'p = NULL': '把p设为null', 'q = NULL': '把q设为null',
        '==': '等于', '!=': '不等于', '++': '自增',
        '->': '箭头', '%zu': '百分号zu',
        'NULL': 'null', 'UB': 'U B', 'VLA': 'V L A',
        '.bss': 'B S S段', '.data': 'data段',
        '.rodata': 'rodata段', '.text': 'text段',
        'create_point': 'create point', 'set_number': 'set number',
        'new_point': 'new point', 'global_uninit': 'global uninit',
        'global_init': 'global init', 'static_global': 'static global',
        'static_local': 'static local', 'static_zero': 'static zero',
        'min_int': 'min int', 'add_two': 'add two',
    }
    for a, b in replacements.items():
        text = text.replace(a, b)
    text = re.sub(r'\b([a-zA-Z]+)\[(\d+)\]', r'\1下标\2', text)
    text = text.replace('`', '').replace('；', '。')
    return text

# Add brief guided reading to the supplied prose, without changing the slides.
GUIDANCE = {
 5: '读代码时先不要同时盯住整页。先在main里找到n的初值，再沿着函数调用走到上面的set number。我们要比较的是两个不同作用域里的对象，而不是两个名字的拼写。',
 6: '现在请只看图左侧的n，再看右侧的x。它们即使一开始都等于十，也不是同一个存储位置。这就像原件和复印件内容相同，却是两张纸。',
 7: '请把目光停在取地址和解引用这两个动作上。取地址告诉函数去哪里，解引用才是真正沿着地址访问对象。只改变形参p本身，并不会自动改掉调用者的指针。',
 8: '这里的箭头很重要。左边装的是地址，右边才是被访问的数据。不要因为左边指针变量还在，就推断右边对象一定还活着。',
 9: '函数叫create point，不会自动给局部结构体延长寿命。危险不在于结构体的值有没有被覆盖，而在于函数返回时，这个局部对象的生命周期已经结束。',
 13: '请沿着左图从main往上看：每次调用建立新的调用现场，返回时退出对应一层。再看右图，已经申请的块和空闲块交错分布。每个申请成功的块内部仍是一段连续的空间。',
 15: '这页重点不是背栈有多大，而是失败时有没有可靠的处理路径。申请堆空间后先检查null，确认成功再访问；不能把是否崩溃当作空间足够的判断方法。',
 16: '把现在的point和第一节的point对照起来。原来point本身是一个局部结构体，现在point变成了局部指针，真正的结构体由malloc创建。这一处改变，才让返回出去的地址有了有效的所指对象。',
 19: '星号放在变量声明里表示指针类型，但申请空间时，要看你准备放进去的对象是什么。放十个整数，就算十个整数的大小；放一个Point结构体，就算一个完整Point的大小。',
 20: '这段代码中n等于五，合法下标从零到四。a下标零和a下标四都为零，展示的是整数数组的零初始化效果。使用结束之后，仍然要free。',
 21: '先只看左图的原地扩展，再看右图的搬家。无论底层选哪一种，程序都应采用返回的新指针。不能因为某一次地址没有变化，就继续沿用旧别名。',
 22: '失败时的关键是，旧块还活着。临时指针接收null，不影响我们手中的旧指针；直接覆盖p，则会把清理旧块需要的线索一起丢掉。',
 23: '我们把流程再顺一遍：先接住返回值，再判断失败，最后才更新p。这里失败后选择清理并退出，是示例的错误处理策略；如果业务允许，也可以保留旧块继续处理。',
 25: '先不要急着看答案。每一次调用里，哪些对象是新创建的，哪些对象沿用上次的值？请把两次调用分别当作一轮，在心里写出每轮三个数。',
 27: '作用域回答的是名字在哪里可以用，生命周期回答的是对象何时存在。比如static局部变量，函数外不能直接用它的名字，但函数返回之后，那个对象仍然存在。',
 28: '这张图是理解用途的示意，不要求你死记具体地址。抓住三组就够了：调用现场主要看Stack，动态对象主要看Heap，全局与static对象看静态存储区。再把代码和只读数据与运行时可写数据分开。',
 29: '请先按是否有static存储期分组，再看有没有显式初值。没有写初值的全局变量，不等于没有初始化；而普通局部变量没写初值，也绝不等于自动得到零。',
 32: '看这页的两步图示：第一步结束了所指对象的生命周期；第二步才改写指针变量。free和把指针设为空，是两个不同的操作。',
 33: '一个分配块要作为整体释放。块内部的地址可以用来访问有效元素，却不能代替分配接口返回的那个指针交给free。',
 34: '请数右边的对象，而不是数左边的指针。p和q只是两份地址，只有一次分配，就只有一个需要安排释放的动态对象。',
 35: '这个例子正好与悬空指针相反。悬空指针是地址还在、对象已死；内存泄漏则可能是对象还占着空间，但程序已经失去能管理它的指针。',
 36: '创建函数和调用者需要约定责任。创建失败返回null，调用者就不能继续访问成员；创建成功后，调用者接过对象，也接过最后释放它的责任。',
 38: '先存next，再free当前节点，最后移动到next。请按这个顺序沿着右下方箭头走一遍。顺序颠倒以后，就会去读取一个已经不存在的节点。',
 40: '知识回顾之后，我们用几道练习检查自己是否真的分清了指针、对象和生命周期。你可以在题目页暂停视频，独立写下答案，再继续看解析。',
}

EXERCISES = {
42: ['下面进入指针与宏练习。每道题先展示题目，留一点思考时间，然后讲解答案。视频可以随时暂停，先自己做，再核对。'],
43: ['第一题，判断这五句话的对错。A，普通局部变量一定活到整个程序结束。B，动态分配的对象可以跨越一次函数调用继续存在。C，把指针赋值为null会自动释放原来的内存。D，全局变量可以通过free它的地址来释放。E，多个指针可以同时指向一个仍然有效的分配。', '请先选择正确项，并用对象的生命周期解释理由。不要只背字母，逐项想一想对象是谁、由谁管理。'],
44: ['正确的是B和E。A错，普通局部对象离开对应代码块后就结束生命周期。B对，动态对象的存在不依赖创建它的函数有没有返回。', 'C错，赋值为null只改变指针，原来的分配可能因此泄漏。D错，全局变量不是动态分配出来的，不能这样free。E对，多个指针可以形成别名，但需要协调访问与释放责任。'],
45: ['第二题，移动形参，会不会改变调用者的指针？数组a有两个元素，分别是四和六。main里的p指向第一个元素，把p传给move。', 'move里面只把自己的形参p向后移动一个元素，没有通过二级指针修改main里的p，也没有改数组内容。请先判断最后两次解引用各会打印什么。'],
46: ['答案是四、四。函数得到的是地址值的副本，移动形参只改变这份副本。a的第一个元素仍然是四，main里的p也仍指向第一个元素。', '如果目标是修改调用者的指针本身，就把那个指针变量的地址传进去，用二级指针更新它。这和我们最开始传入n的地址，是同一种按值传递规则。'],
47: ['第三题，写add two，让调用者的整数加二，同时返回修改前的旧值。例如原来x等于零，调用后返回零，而x变成二。', '需要修改调用者的对象，所以形参应接收地址。接下来思考：旧值应什么时候保存，新的值应什么时候写回？这里假定指针有效，并且加二不会发生有符号整数溢出。'],
48: ['一种清晰写法是，形参用int指针x，先定义old保存x所指对象的值，再给该对象加二，最后返回old。', 'main调用时传入x的地址。输出是零、二。指针参数本身依然按值传递，但它帮助函数找到并修改了调用者的整数对象。'],
49: ['第四题，看宏MUL。它直接写成a乘b，没有加任何括号。现在计算十六除以MUL括号一加一、三减一。', '宏先做文本替换，再按运算符优先级计算。请先写出展开后的整个表达式，不要把宏调用想象成已经算好结果的函数调用。'],
50: ['展开后是十六除以一，加上一乘三，再减一。先乘除再加减，得到十六加三减一，也就是十八。', '正确写法是，参数a和b各自加括号，整个乘法表达式外面再加一层括号。这次MUL先得到四，十六除以四，最终得到四。'],
51: ['第五题，使用条件运算符写MIN宏，返回两个参数中较小的值。条件成立取前一个分支，否则取后一个分支。先考虑每个参数与整体表达式的括号。', '再思考一个进阶问题：把i自增作为实参，会只执行一次吗？宏参数在展开后出现几次，就可能被求值几次。'],
52: ['常见写法是，括号a小于括号b，问号a、冒号b，再为整个表达式加括号。但加括号只解决优先级，不解决重复求值。', '例子里i初始为一。比较时第一次执行i自增，参与比较的是一，i变成二；条件成立，在真分支又执行一次i自增，得到二，i变成三。因此输出是二、三。', '这种带副作用的实参不适合交给会重复使用参数的宏。对普通整数，可以使用下面的min int函数，让每个实参在调用时只求值一次。'],
53: ['第六题，写一个PS宏，接收类型名，打印这个类型的名字和它的大小。例如传入long long，输出类型名long long，以及本平台sizeof的结果。', '两个提示：井号可以把宏参数字符串化；sizeof的结果类型是size t，要用百分号zu打印。请把类型名文本和大小这两部分分别想清楚。'],
54: ['答案使用井号type，把传入的类型名变成字符串。它与前后的字符串字面量相邻，编译时会自动拼接。', '另一个printf参数使用sizeof括号type。注意输出的字节数由平台决定，不能把某个常见平台上的八字节当成所有实现的固定答案。'],
55: ['最后一道综合题。这段代码只分配两个整数，用p和q两个指针指向它。接着访问p下标二，free之后又通过q读取，并再次free。', '请逐行标出违反的规则。先检查分配失败，再检查合法下标，然后追踪对象何时结束生命周期，最后检查释放次数。不要预测未定义行为之后的输出。'],
56: ['一共有几处关键问题。第一，没有检查malloc是否返回null。第二，两个元素只有下标零和一，访问下标二越界。', '第三，free之后，再读q下标零是释放后使用。第四，最后free q重复释放同一块分配。p设为null只改p，不会同步更新q。', '把整个流程记成：检查分配、初始化、范围内访问、统一安排释放、停止使用旧别名。做完这几道题，再回头看开场的四个问题，指针和内存管理就能连成一条线。'],
}


def semantic_focus(page,text,index,count):
    no=page.number+1
    def zone(x,y,w,h):return {'rect':[round(x*1920),round(y*1080),round(w*1920),round(h*1080)],'mode':'region'}
    def find(*terms):
        for term in terms:
            rects=[r for r in page.search_for(term) if page.rect.height*.17<r.y0<page.rect.height*.87]
            if rects:
                r=rects[0]+(-3,-3,3,3);sx=1920/page.rect.width;sy=1080/page.rect.height
                return {'rect':[round(r.x0*sx),round(r.y0*sy),round(r.width*sx),round(r.height*sy)],'mode':'line'}
        return None
    def sequence(*foci):
        foci=[f for f in foci if f]
        return {'sequence':[dict(f,at=i/len(foci)) for i,f in enumerate(foci)]} if foci else None
    if no==5:
        return [find('set_number(n)'),find('x = 42'),None,find('outside')][min(index,3)]
    if no==7:
        return [None,find('set_number(&n)'),find('*p = 42'),zone(.58,.54,.36,.08),sequence(find('set_number(&n)'),find('*p = 42'))][min(index,4)]
    if no==8:
        return [zone(.12,.27,.76,.25),zone(.12,.27,.38,.25),zone(.51,.27,.38,.25),None,sequence(zone(.12,.27,.38,.25),zone(.51,.27,.38,.25))][min(index,4)]
    if no==9:
        return [find('struct Point point'),find('p->x = 99'),find('return &point'),find('p->x = 99'),find('return &point')][min(index,4)]
    if no==14:return find('int a[n]') if index<2 else zone(.05,.71,.88,.1)
    if no==15:
        left=zone(.04,.25,.45,.43);right=zone(.50,.25,.45,.43)
        if '左边' in text:return left
        if '右边' in text:return right
        if '酒泉' in text:return zone(.07,.71,.85,.15)
        if '这页重点' in text:return sequence(left,right)
        return None
    if no==16:
        return [None,find('point = malloc'),find('if (point == NULL)'),sequence(find('point->x'),find('point->y'),find('return point')),
                sequence(find('create_point(10, 15)'),find('p->x = 99'),find('free(p)')),sequence(zone(.05,.30,.44,.43),zone(.50,.30,.44,.43))][min(index,5)]
    if no==17:
        if index==0:return None
        if index==1:return zone(.06,.68,.87,.07)
        return sequence(zone(.13,.53,.38,.17),zone(.14,.29,.37,.21),zone(.57,.29,.31,.21))
    if no==18:
        terms={1:'malloc',2:'calloc',3:'realloc',4:'free'}
        return find(terms[index]) if index in terms else None
    if no==19:
        if '下面那个灰框' in text:return sequence(find('sizeof(int *)'),zone(.15,.50,.76,.1),zone(.15,.62,.76,.1))
        if '10 个 int' in text:return find('10 * sizeof(int)')
        if '星号' in text:return sequence(zone(.15,.50,.76,.1),zone(.15,.62,.76,.1))
        return None
    if no==20:return find('calloc') if index==0 else sequence(find('a[0]'),find('a[4]'),find('free(a)'))
    if no==21:
        left=zone(.06,.27,.43,.35);right=zone(.53,.27,.43,.35)
        if '情况 A' in text:return left
        if '情况 B' in text:return right
        if '所以大家' in text:return zone(.06,.65,.9,.18)
        if '先只看左图' in text:return sequence(left,right)
        return None
    if no==23:
        return [None,find('int *tmp = realloc'),sequence(find('if (tmp == NULL)'),find('free(p)')),sequence(find('p = tmp'),find('p[2] = 30')),sequence(find('int *tmp = realloc'),find('if (tmp == NULL)'),find('p = tmp'))][min(index,4)]
    if no==25:return [find('int global'),sequence(find('++local'),find('++count'),find('++global')),find('tick()')][min(index,2)]
    if no==26:
        if index==0:return zone(.06,.33,.87,.12)
        if 'local' in text and 'count' not in text:return find('local')
        if 'count' in text:return find('count')
        return None
    if no==27:
        if text.startswith('Scope'):return find('Scope')
        if 'Lifetime（' in text:return find('Lifetime')
        if '最上面' in text:return zone(.26,.47,.65,.08)
        if '中间一行' in text:return zone(.26,.56,.52,.08)
        if '最下面' in text:return zone(.26,.65,.52,.08)
        return None
    if no==28:
        if '最上面是 Stack' in text:return zone(.10,.19,.43,.12)
        if '往下一格' in text:return zone(.10,.48,.43,.08)
        if '再往下' in text:return zone(.10,.56,.43,.15)
        if '最下面两层' in text:return zone(.10,.72,.43,.15)
        if '再看最右侧' in text:return zone(.51,.20,.06,.65)
        if '大家顺着' in text:return zone(.10,.19,.43,.67)
        return None
    if no==29:
        if '未初始化的全局' in text:return sequence(find('global_uninit'),find('static_zero'))
        if '带了非零' in text:return sequence(find('global_init'),find('static_global'),find('static_local'))
        if '普通局部变量 local' in text:return find('int local')
        if text.startswith('第一'):return zone(.05,.65,.9,.13)
        if text.startswith('第二'):return find('const char *p')
        if text.startswith('我们把'):return zone(.51,.18,.43,.42)
        return None
    if no==30:return zone(.07,.27,.40,.45) if index==0 else zone(.06,.72,.88,.1)
    if no==32:
        if '第一步' in text:return zone(.56,.26,.35,.17)
        if '第二步' in text:return zone(.56,.45,.35,.17)
        if '两步图示' in text:return sequence(zone(.56,.26,.35,.17),zone(.56,.45,.35,.17))
        return None
    if no==34:
        if '申请了一块' in text:return find('int *q = p')
        if '看左边的代码' in text:return find('int *q = p')
        if '注意右边' in text:return zone(.53,.29,.42,.32)
        if '当你调用' in text:return sequence(find('free(p)'),find('p = NULL'),zone(.53,.29,.42,.32))
        if '记住右下' in text:return zone(.52,.66,.43,.09)
        if '请数右边' in text:return zone(.53,.29,.42,.32)
        return None
    if no==36:return sequence(find('create_point(10, 15)'),find('free(p)')) if index<2 else find('if (p == NULL)')
    if no==37:
        if index==0:return zone(.1,.31,.77,.33)
        if index==1:return zone(.1,.31,.77,.33)
        return find('free(head)') or zone(.06,.72,.88,.08)
    if no==38:
        if '错误示范' in text:return zone(.54,.24,.42,.25)
        if text.startswith('第一步'):return find('struct Node *next')
        if text.startswith('第二步'):return find('free(head)')
        if text.startswith('第三步'):return find('head = next')
        if '顺序' in text:return sequence(find('struct Node *next'),find('free(head)'),find('head = next'))
        return None
    if no==39:
        for key in ('Out-of-bounds','Uninitialized','Dangling','Double free','Memory leak','AddressSanitizer'):
            if key.lower() in text.lower():return find(key)
        return None
    if no==40:
        if text.startswith('第一'):return find('在哪里')
        if text.startswith('第二'):return find('活多久')
        if text.startswith('第三'):return find('能访问')
        if text.startswith('第四'):return find('谁释放')
        if text.startswith('记住'):return zone(.06,.73,.88,.1)
        return None
    if no in (43,44):return zone(.10,.29,.80,.39) if index==0 else None
    if no==45:return find('int a[2]') if index==0 else find('p = p + 1')
    if no==46:return zone(.05,.29,.88,.23) if index==0 else find('int **p')
    if no==47:return find('int add_two') if index==0 else zone(.08,.65,.84,.18)
    if no==48:return sequence(find('int old = *x'),find('*x += 2'),find('return old')) if index==0 else find('add_two(&x)')
    if no==49:return find('#define MUL') if index==0 else None
    if no==50:return find('BAD_MUL') if index==0 else find('#define MUL')
    if no==51:return find('#define MIN') if index==0 else find('MIN(i++')
    if no==52:return [find('#define MIN'),find('MIN(i++, 5)'),find('min_int')][min(index,2)]
    if no==53:return find('#define PS') if index==0 else zone(.08,.60,.84,.2)
    if no==54:return find('#type') if index==0 else find('sizeof(type)')
    if no==55:return zone(.06,.23,.88,.5) if index==0 else sequence(find('malloc'),find('p[2]'),find('free(p)'),find('free(q)'))
    if no==56:
        if index==0:return zone(.08,.26,.86,.24)
        if index==1:return zone(.08,.50,.86,.23)
        return zone(.06,.76,.88,.09)
    return NotImplemented

def make_focus(page, text, index, count):
    """Find actual PDF words first; diagram pages use deliberately broad regions."""
    manual=semantic_focus(page,text,index,count)
    if manual is not NotImplemented:return manual
    page_no = page.number + 1
    zones = {
      6: [(0.13,0.25,0.31,0.19),(0.57,0.25,0.31,0.19),(0.05,0.48,0.9,0.26)],
      10:[(0.10,0.23,0.37,0.3),(0.57,0.23,0.37,0.3),(0.05,0.61,0.9,0.24)],
      13:[(0.07,0.21,0.42,0.38),(0.54,0.21,0.42,0.38)],
      15:[(0.04,0.25,0.45,0.43),(0.50,0.25,0.45,0.43),(0.07,0.71,0.85,0.15)],
      17:[(0.14,0.29,0.37,0.21),(0.57,0.29,0.31,0.21),(0.13,0.53,0.38,0.17)],
      21:[(0.06,0.27,0.43,0.35),(0.53,0.27,0.43,0.35),(0.06,0.65,0.9,0.18)],
      22:[(0.05,0.25,0.44,0.55),(0.53,0.43,0.43,0.2)],
      27:[(0.11,0.34,0.79,0.15),(0.12,0.49,0.77,0.11),(0.11,0.61,0.79,0.12)],
      28:[(0.10,0.19,0.43,0.12),(0.10,0.48,0.43,0.08),(0.10,0.56,0.43,0.15),(0.10,0.72,0.43,0.15),(0.59,0.18,0.35,0.65)],
      29:[(0.05,0.20,0.43,0.4),(0.52,0.20,0.43,0.4),(0.05,0.65,0.9,0.2)],
      32:[(0.05,0.28,0.45,0.35),(0.56,0.26,0.35,0.17),(0.56,0.45,0.35,0.17)],
      33:[(0.04,0.23,0.45,0.54),(0.53,0.27,0.43,0.43)],
      34:[(0.05,0.28,0.44,0.48),(0.53,0.29,0.42,0.32)],
      35:[(0.04,0.26,0.48,0.32),(0.53,0.32,0.42,0.22)],
      38:[(0.05,0.34,0.44,0.35),(0.54,0.24,0.42,0.25),(0.54,0.53,0.42,0.25)],
    }
    if page_no in zones:
        z=zones[page_no][min(len(zones[page_no])-1,index*len(zones[page_no])//max(count,1))]
        return {'rect':[round(z[0]*1920),round(z[1]*1080),round(z[2]*1920),round(z[3]*1080)],'mode':'region'}
    terms=[]
    for term in ['return &point', 'point = malloc', 'if (point == NULL)', 'point->x', 'point->y',
                 'free(p)', 'int *tmp = realloc', 'if (tmp == NULL)', 'p = tmp',
                 'int n = 10', 'set_number(n)', 'x = 42', 'set_number(&n)', '*p = 42',
                 'calloc', 'sizeof(int *)', 'sizeof(int)', 'global_uninit', 'static_zero',
                 'static int count', 'int local = 0', 'MIN', '#type']:
        short=term.split(' = ')[0]
        if term in text or (len(short)>5 and short in text): terms.append(term)
    for term in reversed(terms):
        rects=page.search_for(term)
        rects=[r for r in rects if r.y0>page.rect.height*.17 and r.y1<page.rect.height*.87]
        if rects:
            r=rects[0]+(-3,-3,3,3)
            sx=1920/page.rect.width;sy=1080/page.rect.height
            return {'rect':[round(r.x0*sx),round(r.y0*sy),round(r.width*sx),round(r.height*sy)],'mode':'line'}
    # Keep broad explanations unobstructed rather than inventing an inaccurate pointer.
    return None


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pdf',type=Path,default=ROOT/'build/CS100_Recitation5.pdf')
    ap.add_argument('--output',type=Path,default=ROOT/'build/narration')
    args=ap.parse_args(); out=args.output
    (out/'slides').mkdir(parents=True,exist_ok=True)
    source=(HERE/'source.txt').read_text()
    pattern=re.compile(r'^### 【P(\d+)\s*\|([^\n]+)】\[(\d+):(\d+)\s*-\s*(\d+):(\d+)\][^\n]*$',re.M)
    headings=list(pattern.finditer(source)); pages={};corrections=[]
    for i,m in enumerate(headings):
        body=source[m.end():headings[i+1].start() if i+1<len(headings) else len(source)]
        body='\n'.join(x for x in body.splitlines() if not re.match(r'^\s*(─+|第[一二三四五六七八九十]+节：|课堂总结与收尾)',x))
        pages[int(m[1])]={'header':m[0], 'body':clean(body)}
    fixes={
      10:[('很多同学在自己电脑上跑刚才那段错误代码时，会发现一个特别诡异的现象：明明改的是 p->x = 99，结果后面打印 new_point.x，居然莫名其妙变成了 99！为什么新变量会无辜躺枪？','这类悬空指针错误可能出现一个诡异后果：明明通过p写入，后来创建的其他对象却被破坏。但刚才这段代码不保证出现这个现象，也可能崩溃。为什么新变量可能无辜躺枪？'),('很可能会复用','可能复用'),('实际上就砸到了','就可能砸到'),('我们必须使用动态内存分配','一种办法就是使用动态内存分配')],
      14:[('所有作业和考试','所有作业')],
      19:[('在 64 位机器上固定是 8 字节','常见64位环境通常为8字节，具体以平台为准'),('内存立马就不够装、越界崩溃了','就可能分配不足，后续越界访问属于未定义行为')],
      20:[('长度为 2','长度为 5'),('calloc(2, sizeof(int))','calloc(5, sizeof(int))')],
      23:[('所以，安全调用 realloc 的标准姿势看右边第 11 到 14 行：','所以，安全调用realloc的标准姿势，是先看左边申请扩容的代码，再看右边更新指针的步骤：')],
      25:[('step','tick')],26:[('step','tick')],
      29:[('显式初始化为 0 的 static_zero','没有显式初始化的 static_zero')],
      32:[('归还给了系统','归还给分配器供后续复用')],
      39:[('强烈建议大家开启上节课讲过的 AddressSanitizer，一抓一个准','可以结合上节课讲过的AddressSanitizer帮助定位')],
    }
    for no, pairs in fixes.items():
        for old,new in pairs:
            if old in pages[no]['body']:
                pages[no]['body']=pages[no]['body'].replace(old,new)
                corrections.append({'page':no,'before':old,'after':new})
    pages[41]['body']='今天我们从形参与实参出发，讲清了指针、生命周期、动态分配和释放责任，也完成了课后练习的解析。建议大家课后亲手修改这些示例，再用今天的四个问题检查自己的代码。CS一百第五次习题课就到这里，谢谢大家！'
    doc=pymupdf.open(args.pdf)
    if len(doc)!=56:raise SystemExit(f'Expected current 56-page PDF, got {len(doc)}')
    snapshot=out/'slides.pdf';shutil.copy2(args.pdf,snapshot)
    ordered=list(range(1,41))+list(range(42,57))+[41]
    segments=[]; slide_items=[]
    for order,no in enumerate(ordered):
        page=doc[no-1]
        if no in EXERCISES:paras=EXERCISES[no]
        else:
            paras=[x.strip() for x in pages[no]['body'].splitlines() if x.strip()]
            if no in GUIDANCE:
                if no in (5,6,25):paras.insert(max(len(paras)-1,0),GUIDANCE[no])
                else:paras.append(GUIDANCE[no])
        title={4:'我们为什么需要指针？',11:'运行时需要空间：动态分配',24:'Memory区域与对象的生命周期',31:'谁负责free：指针、别名与所有权',42:'指针与宏：带做练习',41:'Thank You'}.get(no,page.get_text().splitlines()[0])
        footer_matches=re.findall(r'(\d+)\s*/\s*(\d+)',page.get_text())
        footer='/'.join(footer_matches[-1]) if footer_matches else None
        image=out/'slides'/f'p{no:03}.png'
        pix=page.get_pixmap(matrix=pymupdf.Matrix(1920/page.rect.width,1080/page.rect.height),alpha=False)
        im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
        if im.size!=(1920,1080):im=im.resize((1920,1080),Image.Resampling.LANCZOS)
        im.save(image)
        ids=[]
        for j,text in enumerate(paras):
            sid=f'p{no:03}-{j+1:02}'
            pause=0.75
            if text.endswith(('？','?')):pause=3.0
            if j==len(paras)-1:pause=1.0
            if no in (5,25,43,45,47,49,51,53,55) and j==len(paras)-1:pause=7.0
            if no in (9,16,19,21,23,28,29,33,38) and j==len(paras)-1:pause=3.5
            if no in (4,11,24,31,42):pause=1.3
            spoken=speech(text)
            item={'id':sid,'page':no,'order':len(segments),'text':text,'speech':spoken,
                  'pause':pause,'focus':make_focus(page,text,j,len(paras)),
                  'sha256':hashlib.sha256(spoken.encode()).hexdigest()}
            segments.append(item);ids.append(sid)
        slide_items.append({'page':no,'order':order,'title':title,'image':str(image.relative_to(out)),'segments':ids,'footer':footer})
    data={'pdf_sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest(),'target_seconds':2700,
          'width':1920,'height':1080,'slides':slide_items,'segments':segments,'corrections':corrections,
          'voice':{'speaker':'zh_female_vv_uranus_bigtts','speech_rate':-15,'resource_id':'seed-tts-2.0'}}
    (out/'project.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    (out/'corrections.json').write_text(json.dumps(corrections,ensure_ascii=False,indent=2)+'\n')
    print(f'Prepared {len(slide_items)} slides and {len(segments)} speech segments; {len(corrections)} corrections.')
    print(f'Characters after speech normalization: {sum(len(x["speech"]) for x in segments)}; planned pauses: {sum(x["pause"] for x in segments):.1f}s')

if __name__=='__main__':main()
