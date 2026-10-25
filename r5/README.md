# CS100 Recitation 5：C语言内存管理

沿用仓库的上科大红色Beamer主题，以中文讲解为主，保留Memory layout、lifetime、stack、heap、ownership等英文术语。从实参／形参的值传递引出指针，在此处解释生命周期与dangling pointer，再讲动态分配、memory区域与释放责任，课堂以回顾结束；指针与宏练习作为附录供课后独立完成。

- [课件PDF](build/CS100_Recitation5.pdf)：55页编号正文，含封面、5张分节页及结束页共62个物理页。
- [课件入口](CS100_Recitation5.tex)：按顺序引用五份`Section*.tex`。
- [课堂示例](code/)：完整C17程序、用于课件展示的`.inc`片段，以及内存布局观察命令。

## 编译与运行

从仓库根目录执行：

```bash
make -j -C r5
make -C r5 check-demos
```

PDF编译依赖共享的`template/`、XeLaTeX、latexmk与中文字体，与其他习题课一致。示例检查需要Python3和C17编译器，默认使用`cc`，可通过`CC=gcc`指定。

`check-demos`逐个编译全部17份完整`.c`程序，使用`-std=c17 -Wall -Wextra -Werror -pedantic -O0 -g`，验证课堂输出及动态数组的零大小、非法输入和过大字节数处理。`.inc`是代码阅读片段，可能故意保留错误、缺少上下文，不单独编译。

从`r5/`执行布局观察：

```bash
bash code/layout.sh
```

该演示需要Linux／WSL环境与binutils中的`size`、`objdump`。通过`size`比较.bss与.data，通过符号表确认`array`的section。具体地址、二进制文件大小与类型大小随平台和工具链变化。

## 课堂安排

建议90分钟，页码为PDF物理页，便于直接跳转。课堂讲解到第47页结束；第48—62页为课后练习附录，不占课堂讲解时间。

| 课堂进度 | PDF物理页 | 内容 |
|---|---|---|
| 0—5分钟 | 1—4 | 开场问题、目录与指针主题导入 |
| 5—25分钟 | 5—10 | 实参与形参、传地址、生命周期、dangling pointer及栈空间复用的可能后果 |
| 25—50分钟 | 11—24 | Stack／Heap直观结构、VLA、作业禁用规则与栈耗尽风险，malloc/calloc/realloc、大小检查、分配失败与安全扩容、create_point修复版 |
| 50—65分钟 | 25—33 | memory区域、static与automatic、scope与lifetime、.bss/.data与栈帧 |
| 65—85分钟 | 34—45 | free、别名、泄漏、所有权、链表释放与错误小结 |
| 85—90分钟 | 46—47 | 回顾、提问与课堂结束 |
| 课后自学 | 48—62 | 指针／宏练习及综合题，答案单独成页，课堂不讲 |

同学已学过struct，课件直接使用结构体案例，不再补充其基础语法。第42—44页链表案例聚焦二级指针更新表头、节点生命周期与释放顺序。全部练习均供课后独立完成，课堂不安排题目或答案讲解。

`dangling-write.inc`以C风格的`create_point`函数创建并初始化局部结构体，再错误地返回其地址。它只用于读代码分析：局部对象生命周期结束后，指针值变为不确定值，不应继续使用。随后在main中创建新结构体并通过悬空指针写入；图示说明后续对象可能复用同一栈空间，悬空写入可能破坏新对象，但这不是可保证的地址布局或程序输出，不作为运行演示或测试用例。

本课程所有作业禁止使用VLA。课件在动态分配开头解释`int a[n]`，重点对比malloc失败返回NULL、可以检查处理，而VLA通常占用栈空间，n过大可能造成栈耗尽和安全风险；用“发射中心要建在酒泉，而不是紫禁城”辅助记忆。VLA示例仅供读代码，不加入可运行示例。

动态分配的讲解接续前面的失败案例：`create-point.c`用malloc创建Point结构体，函数返回时局部指针结束生命周期，动态对象继续存在；main使用后free。第13页先以调用栈帧和分散的分配块介绍Stack／Heap，再讲VLA爆栈，完整地址区域在后面介绍。

## 完整程序与预期结果

| 文件 | 观察点 | 预期结果 |
|---|---|---|
| `by-value.c` | 修改形参副本不改变实参对象 | 两行：`inside: 42`、`outside: 10` |
| `by-address.c` | 将地址值复制给形参，通过指针修改调用者对象 | `42` |
| `lifetime.c` | 局部／static／全局变量 | 两行：`1 1 11`、`1 2 12` |
| `bss.c`、`data.c` | 零初始化与非零初始化数组 | 退出码分别为0、1；结合符号表观察 |
| `create-point.c` | 用malloc修复前面的结构体创建函数，main检查、使用并free | 两行：`99 15`、`20 30` |
| `malloc.c` | 单整数分配补充示例，课件主线使用create-point.c | `42` |
| `array.c` | 运行时大小与乘法回绕检查 | 输入`5`输出`0`；输入协议为可由size_t表示的非负整数 |
| `calloc.c` | 整数数组零初始化 | `0 0` |
| `realloc.c` | 临时指针接收扩容结果 | `10 20 30 40` |
| `owned.c` | 返回动态对象的补充示例，所有权课件回看create-point.c | `42` |
| `list.c` | 头插、分配失败清理、逐节点释放 | `20 10` |
| `pointer.c` | 指针形参仍按值传递 | `4 4` |
| `add-two.c` | 修改调用者对象并返回旧值 | `0 2` |
| `macro-mul.c` | 参数与整体括号 | 两行：`18`、`4` |
| `macro-min.c` | 条件运算符与重复求值 | 两行：`2 3`、`3` |
| `macro-size.c` | 字符串化与`%zu` | 类型名及本平台的`sizeof`结果 |

课件及配套示例统一使用显式类型的sizeof表达式：整数用`sizeof(int)`，结构体用`sizeof(struct Point)`或`sizeof(struct Node)`。`sizeof(int *)`仅表示指针本身的大小，不用于代替int对象大小。

所有完整程序均检查可能失败的动态分配。输入数组示例演示分配大小检查，不作为任意文本或超范围整数的完整输入解析器。`add_two`要求有效指针且原值加2可由int表示。

`list.c`中的节点定义、头插与释放函数来自课件展示的`list-node.inc`、`list-insert.inc`与`list-free.inc`；修改时应保持二者一致。

## 改编说明

原材料为用户提供的《Discussion 3 memory.pdf》，标题为《Memory Management in C — Computer Architecture Discussion》，日期为2026年3月20日。按CS100习题课的语言与版式重新组织，不直接嵌入原稿页面。

- 区分C语言的存储期／生命周期规则和常见Linux／ELF实现，布局图将.bss与.data标为Static区，并按读写用途增加RAM／ROM教学类比分组；明确Linux中的.text与.rodata通常也驻留物理RAM，ROM标签仅类比只读属性，保留布局限制；紧接代码对照未初始化／非零初始化全局变量、静态局部／全局变量、零初始化static对象、字符串字面量及局部指针的常见位置；同页列初始值，明确未显式初始化的全局／static对象零初始化，而普通automatic局部变量不会自动置零，应先赋值再读。
- 明确零初始化对象可进入.bss，.bss在运行时仍占存储。
- 补齐分配失败、字节数乘法溢出、realloc失败保留原块、成功后旧别名失效等条件。
- 不按stack／heap／global给越界错误作固定严重程度排名。
- 保留原稿六组练习的主题，修正函数签名，补充宏副作用与平台相关的sizeof说明。
- 不讲Valgrind；第45页只用一句话呼应上节课的AddressSanitizer，不新增工具教程。
