# CS100 Recitation 4：GDB、Sanitizer与C语言代码调试

面向已接触C语言数组、函数和基础指针的同学。全部示例使用C17，推荐在Ubuntu／WSL与GCC环境中复现。

- [课件PDF](build/CS100_Recitation4.pdf)：56页编号正文，含封面、分节页与结束页共62个物理页。
- [源代码与页码索引](code/README.md)：35份完整C源码、错误／修复对照、命令与固定输入。

源码末尾的注释标明对应的页码、示例用途与对照文件。页码以PDF页脚1/56至56/56为准。末尾注释保留了已有源码行号，课件和GDB脚本仍按原行号定位。

## 下载包与目录

发布包`CS100_Recitation4_GitHub.zip`解压后可作为独立GitHub仓库内容，保留以下相对位置：

```text
CS100_Recitation4/
├── README.md
├── SHA256SUMS
├── .gitignore
├── r4/
│   ├── build/CS100_Recitation4.pdf
│   ├── CS100_Recitation4.tex
│   ├── Section01.tex … Section04.tex
│   ├── BehaviorExamples.tex
│   ├── SanitizerExamples.tex
│   ├── code/
│   │   ├── README.md              # 全部源码与课件页码的索引
│   │   ├── gdb/                  # 成绩统计反例
│   │   ├── homework/             # HW1主线与作业相关辅助示例
│   │   ├── sanitizer/            # 越界、溢出与生命周期错误
│   │   ├── c/                    # 值传递、整数除法
│   │   ├── behavior/                # 行为分类、格式与作用域
│   │   ├── exercise/             # 多项式循环练习
│   │   ├── fixed/                # 配套修复版
│   │   ├── commands/             # Bash片段与GDB会话
│   │   ├── input/                # 固定输入
│   │   └── output/               # 课件使用的实测记录
│   ├── image/
│   ├── Makefile
│   └── README.md
└── template/                     # 编译课件所需共享模板与素材
```

在完整课件仓库中，本目录为`slides/r4/`。后续命令均从`r4/`执行。包内不包含本机GDB、运行库、可执行文件、临时构建记录、Git历史、原始作业资料；已有PDF可直接阅读。

## 快速运行

Ubuntu／WSL中安装工具：

```bash
sudo apt update
sudo apt install build-essential gdb python3
```

进入`r4/`后执行：

```bash
make demos
make check-all
```

`make demos`分别构建独立程序，产物位于`build/demo/`，不应将全部`.c`链接成一个程序。`make check-all`同时运行普通演示与行为分类检查；诊断记录分别位于`build/demo/output/`和`build/behavior/`。`CC`可指定兼容的C编译器，示例检查以GCC演示环境为准。

有GDB时检查脚本自动验证断点、变量、调用栈、观察点、值传递、循环边界和命令行参数。需要确保GDB检查不被跳过时运行：

```bash
python3 code/check-demos.py --require-gdb
```

部分受限容器禁止ptrace，应在允许调试的终端执行GDB检查。没有GDB时默认检查会显示`SKIP`。

错误版保留故障用于教学：ASan通常终止程序；UBSan默认通常报告后继续执行。检查以错误诊断为依据，不依赖UB后的数值输出。`behavior/scope.c`和启用`-Werror`的`behavior/format-mismatch.c`预期编译失败，由`make check-behavior`单独验证。独立释放后使用示例允许编译警告，其余普通演示采用`-Werror`。

## 课件示例

| 页脚编号 | 示例 | 错误现象／观察点 | 配套修复 |
|---|---|---|---|
| 1—2 | [成绩统计](code/gdb/grades.c) | 60分参与求和却未计数，示例输出110 | [统一及格条件](code/fixed/grades.c) |
| 4—8、18—30 | [HW1求和与最大值](code/homework/hw1-p3.c) | 输入`3 5 2 0`，输出`10 10` | [传入当前输入x](code/fixed/hw1-p3.c)，输出`10 5` |
| 33—37 | [HW2多项式越界](code/sanitizer/polynomial.c) | 从`coef[count]`开始读取，ASan报告越界 | [从count-1开始](code/fixed/polynomial-bounds.c)，输出`17.000` |
| 38—39 | [power乘法溢出](code/sanitizer/power.c) | 32位int无法表示50000²，UBSan报告溢出 | [使用long long](code/fixed/power.c)，输出`2500000000` |
| 40—41 | [数组循环](code/sanitizer/array_loop.c) | `i<=6`访问六元素数组的`data[6]` | [边界改为i<6](code/fixed/array_loop.c)，输出`1` |
| 43、45 | [值传递3+5](code/c/sum.c) | 修改形参后，调用者仍输出`3` | [指针更新](code/fixed/sum.c)，输出`8` |
| 44 | [值传递3+3](code/c/sum-three.c) | 实测会话中形参变为6，调用者仍为3 | [指针更新](code/fixed/sum-three.c)，输出`6` |
| 46—50 | [C行为分类](code/behavior/README.md) | 有符号／无符号、格式匹配、char、越界与作用域 | [各源码及修复对照](code/README.md) |
| 51—53 | [多项式循环练习](code/exercise/polynomial.c) | 下标合法却漏掉常数项，输出`8.000` | [循环包含下标0](code/fixed/polynomial.c)，输出`17.000` |

HW0输入检查、HW2命令行参数、独立求和溢出、HW1宽类型修复和释放后使用保留为补充示例，当前课件没有展示。整数除法完整程序是第46页规则说明的扩展，错误／修复输出为`6.000`／`10.750`。完整列表见[代码索引](code/README.md)。

宽类型修复假定输入与中间结果可以由该类型表示。多项式固定为P(x)=1+2x+3x²，不假定正式作业的输入协议。

## 现场调试入口

HW1连续演示与回归：

```bash
./build/demo/hw1-p3 < code/input/sum-max.txt
gdb -q -nx -batch -x code/commands/session.gdb ./build/demo/hw1-p3
bash code/commands/verify.sh
```

实测在第二个输入5处，调用者`x=5`、`sum=8`，辅助函数却收到`value=8`。将`updateMaximum(maximum, sum)`修正为`updateMaximum(maximum, x)`后重新编译。

power和数组循环的交互演示，分别启动、退出GDB后再运行下一组：

```bash
bash code/commands/power-sanitizer.sh
gdb -q -x code/commands/power-session.gdb build/demo/power-ubsan
```

```bash
bash code/commands/array-sanitizer.sh
gdb -q -x code/commands/array-session.gdb build/demo/array-loop-asan
```

两份脚本在错误操作执行前停止：power中`i=1`、`result=50000`、`x=50000`；数组中`i=6`且六个元素均为1。对应命令与源码见[代码索引](code/README.md)。

`code/output/`保存课件引用的实测诊断和用户会话，文本中的源码路径及行号已统一到包内文件，截图保留原样。新运行记录写入`build/`，具体地址、进程号与报告格式可随环境变化。

## 教学安排

| 时间 | 正文页码 | 内容 |
|---|---|---|
| 0—10分钟 | 1—8 | 成绩统计、HW1反例与调试思路 |
| 10—20分钟 | 9—17 | GDB概念、安装验证与编译参数 |
| 20—43分钟 | 18—30 | HW1连续GDB演示与修复 |
| 43—62分钟 | 31—42 | 多项式越界、power溢出与数组循环 |
| 62—68分钟 | 43—45 | 值传递与指针更新 |
| 68—77分钟 | 46—50 | C17行为分类与编译错误 |
| 77—85分钟 | 51—53 | 多项式循环练习 |
| 85—90分钟 | 54—56 | 调试流程、速查与提问 |

## 编译PDF与重新打包

课件使用仓库共享的上科大红色Beamer主题。编译需TeX Live、latexmk和中文字体：

```bash
sudo apt install latexmk texlive-full fonts-noto-cjk
make -j
```

PDF输出为`build/CS100_Recitation4.pdf`。`r4/`与`template/`必须相邻。

重新编译并生成GitHub发布包：

```bash
make package
```

输出为`build/dist/CS100_Recitation4_GitHub.zip`和对应`.zip.sha256`。若只需打包已确认与源码一致的现有PDF，可直接运行`python3 code/package-release.py`；该命令不会编译PDF或执行示例检查。压缩包根目录另含`SHA256SUMS`，解压后运行`sha256sum -c SHA256SUMS`验证文件。

发布到现有完整课件仓库时提交`r4/`的源码和文档；独立建库可直接使用解压后的内容。独立包内的`.gitignore`保留PDF，忽略其他构建产物。当前完整课件仓库忽略`build/`，若需把PDF一并提交，可使用`git add -f r4/build/CS100_Recitation4.pdf`；ZIP也可作为GitHub Release附件上传。

## 来源与适用范围

[作业改编说明](code/homework/README.md)与[行为示例说明](code/behavior/README.md)记录来源。HW1／HW2案例依据starter注释制作，是课堂调试变体；不作为完整作业标准答案。原始作业资料位于作者工作区，不是本包的运行或编译依赖。

HW1主线不用数组或动态内存；HW2多项式使用固定数组，不使用堆内存或math.h。释放后使用为独立C内存管理补充示例。课件中的演示命令统一从提交包的`r4/`目录执行。第12页使用`code/commands/check-server-tools.sh`检查共享服务器中的GCC与GDB；无sudo权限时先按管理员说明加载工具环境。

## 参考资料

- [GDB手册](https://sourceware.org/gdb/current/onlinedocs/gdb.html/)
- [GCC插桩选项](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html)
- [AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html)
- [UndefinedBehaviorSanitizer](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)
