# R4代码示例索引

页码使用PDF页脚1/56至56/56，不含封面、分节页和结束页。每份C源码末尾均有“课件位置”“用途”和对照源码注释；注释放在末尾，以保留课件截图、GDB断点和实测诊断中的原行号。每份`.c`含独立的`main`，应分别编译。

## 当前课件与配套修复

| 源码 | 使用位置 | 用途 | 对照源码 |
|---|---|---|---|
| [gdb/grades.c](gdb/grades.c) | 第1—2页：成绩统计反例 | 调试用错误版：求和包含60分，计数却使用score > 60。 | [fixed/grades.c](fixed/grades.c) |
| [fixed/grades.c](fixed/grades.c) | 第1—2页：成绩统计反例的配套修复 | 修复版：求和与计数统一使用score >= 60。 | [gdb/grades.c](gdb/grades.c) |
| [homework/hw1-p3.c](homework/hw1-p3.c) | 第4—8页、第18—30页：HW1求和与最大值、连续GDB演示 | 调试用错误版：辅助函数收到累计和sum，而非当前输入x。 | [fixed/hw1-p3.c](fixed/hw1-p3.c) |
| [fixed/hw1-p3.c](fixed/hw1-p3.c) | 第30页：HW1传参错误的修复验证 | 修复版：传入当前输入x；int输入及中间结果仍须在范围内。 | [homework/hw1-p3.c](homework/hw1-p3.c) |
| [sanitizer/polynomial.c](sanitizer/polynomial.c) | 第33—37页：HW2 P3、ASan数组越界 | 错误版：i=count使首次读取访问coef[count]。 | [fixed/polynomial-bounds.c](fixed/polynomial-bounds.c) |
| [fixed/polynomial-bounds.c](fixed/polynomial-bounds.c) | 第35—36页：HW2数组越界的配套修复 | 修复版：从count-1开始，处理至下标0，输出17.000。 | [sanitizer/polynomial.c](sanitizer/polynomial.c) |
| [sanitizer/power.c](sanitizer/power.c) | 第38—39页：power乘法溢出、UBSan与GDB | 错误版：32位int不能表示50000的平方；不依赖UB后的输出。 | [fixed/power.c](fixed/power.c) |
| [fixed/power.c](fixed/power.c) | 第39页：power修复验证 | 修复版：乘积、返回值使用long long，输出2500000000；本例结果须可表示。 | [sanitizer/power.c](sanitizer/power.c) |
| [sanitizer/array_loop.c](sanitizer/array_loop.c) | 第40—41页：数组循环、ASan与条件断点 | 错误版：i<=6访问六元素数组的data[6]。 | [fixed/array_loop.c](fixed/array_loop.c) |
| [fixed/array_loop.c](fixed/array_loop.c) | 第41页：数组循环修复验证 | 修复版：循环条件改为i<6，输出1。 | [sanitizer/array_loop.c](sanitizer/array_loop.c) |
| [c/sum.c](c/sum.c) | 第43页、第45页：C按值传递，3+5 | 错误版：仅修改形参副本，调用者仍输出3，预期为8。 | [fixed/sum.c](fixed/sum.c) |
| [fixed/sum.c](fixed/sum.c) | 第43页、第45页：按值传递示例的配套修复，3+5 | 修复版：传入&sum，通过*sum修改调用者，输出8。 | [c/sum.c](c/sum.c) |
| [c/sum-three.c](c/sum-three.c) | 第44页：实测GDB会话使用的3+3变体 | 错误版：形参变为6，返回调用者后原变量仍为3。 | [fixed/sum-three.c](fixed/sum-three.c) |
| [fixed/sum-three.c](fixed/sum-three.c) | 第44页：指针更新修复，3+3 | 修复版：通过指针修改原变量，输出6；与3+5示例分开。 | [c/sum-three.c](c/sum-three.c) |
| [behavior/signed-overflow.c](behavior/signed-overflow.c) | 第47页：有符号溢出与无符号回绕 | 错误版：INT_MAX减2后加3，有符号溢出属于UB。 | [behavior/unsigned-wrap.c](behavior/unsigned-wrap.c) |
| [behavior/unsigned-wrap.c](behavior/unsigned-wrap.c) | 第47页：有符号溢出与无符号回绕 | 有定义行为：无符号运算按类型取值个数取模，输出0。 | [behavior/signed-overflow.c](behavior/signed-overflow.c) |
| [behavior/format-mismatch.c](behavior/format-mismatch.c) | 第48页：printf格式必须匹配实参类型 | 错误版：%d与double不匹配；仅检查编译诊断，不运行预测输出。 | [behavior/format-fixed.c](behavior/format-fixed.c) |
| [behavior/format-fixed.c](behavior/format-fixed.c) | 第48页：printf格式修复 | 修复版：%.2f匹配double，输出2.25。 | [behavior/format-mismatch.c](behavior/format-mismatch.c) |
| [behavior/digit-promotion.c](behavior/digit-promotion.c) | 第48页：字符整数提升 | 有定义示例：本课环境中提升为int，数字字符连续，输出7。 | — |
| [behavior/char-signedness.c](behavior/char-signedness.c) | 第49页：char的符号属性由实现定义 | 使用-fsigned-char或-funsigned-char；8位char、32位int环境分别输出-1和255。 | — |
| [behavior/bounds.c](behavior/bounds.c) | 第50页：数组越界与编译错误要分开 | 错误版：data[6]越界；与第40页同一边界问题，用于行为分类。 | [behavior/bounds-fixed.c](behavior/bounds-fixed.c) |
| [behavior/bounds-fixed.c](behavior/bounds-fixed.c) | 第50页：数组边界示例的配套修复 | 修复版：i<6，输出1。 | [behavior/bounds.c](behavior/bounds.c) |
| [behavior/scope.c](behavior/scope.c) | 第50页：数组越界与编译错误要分开 | 预期编译失败：show看不到main的局部变量number。 | [behavior/scope-fixed.c](behavior/scope-fixed.c) |
| [behavior/scope-fixed.c](behavior/scope-fixed.c) | 第50页：作用域示例的配套修复 | 修复版：通过函数形参传递number，输出17。 | [behavior/scope.c](behavior/scope.c) |
| [exercise/polynomial.c](exercise/polynomial.c) | 第51—52页：多项式循环练习 | 逻辑错误版：i>0漏掉常数项对应的一轮，输出8.000。 | [fixed/polynomial.c](fixed/polynomial.c) |
| [fixed/polynomial.c](fixed/polynomial.c) | 第53页：练习解答，不能漏掉常数项 | 修复版：循环包含下标0，输出17.000。 | [exercise/polynomial.c](exercise/polynomial.c) |

## 补充与扩展示例

以下源码继续保留供课后复现。标注“未展示”的程序没有对应的当前课件页，不能按旧版页码查找。

| 源码 | 使用位置 | 用途 | 对照源码 |
|---|---|---|---|
| [homework/hw0-input.c](homework/hw0-input.c) | 补充示例：HW0输入检查；当前56页课件未展示 | scanf返回值不是2时退出；小输入123 500输出623。 | — |
| [homework/argv-first.c](homework/argv-first.c) | 补充示例：HW2 argc/argv；当前56页课件未展示 | 仅打印每个参数的首字符，供argv-session.gdb观察，不是完整作业答案。 | — |
| [sanitizer/sum-overflow.c](sanitizer/sum-overflow.c) | 补充示例：HW1累加溢出；当前56页课件未展示 | 错误版：32位int累计INT_MAX和1，用UBSan观察诊断。 | [fixed/sum-overflow.c](fixed/sum-overflow.c) |
| [fixed/sum-overflow.c](fixed/sum-overflow.c) | 补充示例：独立累加溢出的修复；当前课件未展示 | 修复版：long long累计，边界输入输出2147483648；中间结果须可表示。 | [sanitizer/sum-overflow.c](sanitizer/sum-overflow.c) |
| [fixed/hw1-p3-wide.c](fixed/hw1-p3-wide.c) | 补充示例：HW1完整程序的宽类型修复；当前课件未展示 | 同时修正实参和读写类型；输入及中间总和均须可由long long表示。 | [homework/hw1-p3.c](homework/hw1-p3.c) |
| [sanitizer/use-after-free.c](sanitizer/use-after-free.c) | 补充示例：独立C内存生命周期；当前56页课件未展示 | 错误版：free后解引用，ASan报告heap-use-after-free；不属于作业实现。 | [fixed/use-after-free.c](fixed/use-after-free.c) |
| [fixed/use-after-free.c](fixed/use-after-free.c) | 补充示例：生命周期修复；当前课件未展示 | 修复版：本例无需堆分配，使用局部变量，输出90。 | [sanitizer/use-after-free.c](sanitizer/use-after-free.c) |
| [c/poly-division.c](c/poly-division.c) | 第46页整数除法说明的扩展程序；当前课件未展示完整程序 | 逻辑错误版：3/2先做整数除法，多项式输出6.000。 | [fixed/poly-division.c](fixed/poly-division.c) |
| [fixed/poly-division.c](fixed/poly-division.c) | 第46页整数除法说明的扩展修复；当前课件未展示完整程序 | 修复版：除法之前转换为double，输出10.750。 | [c/poly-division.c](c/poly-division.c) |

## 运行入口

从`r4/`执行：

```bash
make demos
make check-all
python3 code/check-demos.py --require-gdb
```

`make demos`构建普通示例、配套修复和Sanitizer演示，产物位于`build/demo/`。`make check-all`另外验证行为分类示例，记录位于`build/behavior/`。`behavior/scope.c`与`behavior/format-mismatch.c`预期在启用`-Werror`时编译失败，故不放入普通成功构建列表。错误示例保留故障用于教学。

## 其他材料

| 目录／脚本 | 用途 |
|---|---|
| [commands/](commands/) | Bash编译片段与GDB命令，见下表 |
| [input/](input/) | 固定输入：求和最大值、重复值、单元素、哨兵与溢出边界 |
| [output/](output/) | 课件引用的实测诊断与会话；文本路径和行号统一到包内源码，地址保留实测值 |
| [build-demos.sh](build-demos.sh) | 用C17逐个编译独立程序 |
| [check-demos.py](check-demos.py) | 检查现象、修复输出、Sanitizer与可选GDB会话 |
| [check-behavior.py](check-behavior.py) | 检查行为分类示例，预期失败的编译也在此验证 |
| [package-release.py](package-release.py) | 打包PDF、源码、模板与校验清单 |

### 命令与课件位置

所有Bash命令从`r4/`执行；`.gdb`在相应程序的GDB会话中使用。`basic/condition/inspect/stack/watch`是连续操作片段，不能在错误的暂停位置单独执行。

| 命令文件 | 对应位置／用途 |
|---|---|
| [argv-session.gdb](commands/argv-session.gdb) | 补充：argc/argv批处理 |
| [argv.gdb](commands/argv.gdb) | 补充：交互检查命令行参数 |
| [argv.sh](commands/argv.sh) | 补充：启动argc/argv调试 |
| [array-sanitizer.sh](commands/array-sanitizer.sh) | 第40页：数组ASan演示 |
| [array-session.gdb](commands/array-session.gdb) | 第41页：越界前暂停 |
| [basic.gdb](commands/basic.gdb) | 第20页：函数断点与运行 |
| [build-debug.sh](commands/build-debug.sh) | 第17页：构建HW1错误版 |
| [build-sanitizer.sh](commands/build-sanitizer.sh) | 第33页：多项式ASan／UBSan构建 |
| [check-poly-division.sh](commands/check-poly-division.sh) | 第46页扩展：整数除法逻辑错误不会必然触发Sanitizer |
| [compile-and-debug.sh](commands/compile-and-debug.sh) | 第10页：编译器与调试器区别 |
| [condition.gdb](commands/condition.gdb) | 第28页：条件断点 |
| [exercise.gdb](commands/exercise.gdb) | 第51—53页：多项式循环练习 |
| [inspect.gdb](commands/inspect.gdb) | 第23页：变量观察 |
| [install.sh](commands/install.sh) | 第11页：Ubuntu／WSL安装 |
| [power-sanitizer.sh](commands/power-sanitizer.sh) | 第38页：power的UBSan演示 |
| [power-session.gdb](commands/power-session.gdb) | 第39页：第二次乘法前暂停 |
| [session.gdb](commands/session.gdb) | 第18—30页：完整HW1批处理会话 |
| [stack.gdb](commands/stack.gdb) | 第26页：调用栈 |
| [start-gdb.sh](commands/start-gdb.sh) | 第20页：启动HW1调试 |
| [sum-pointer.gdb](commands/sum-pointer.gdb) | 第43、45页：3+5指针修复观察 |
| [sum-value.gdb](commands/sum-value.gdb) | 第43、45页：3+5值传递观察 |
| [check-server-tools.sh](commands/check-server-tools.sh) | 第12页：检查共享服务器中的GCC与GDB |
| [verify-install.gdb](commands/verify-install.gdb) | 第13—15页：GDB帮助与退出 |
| [verify-install.sh](commands/verify-install.sh) | 第13—15页：终端验证 |
| [verify.sh](commands/verify.sh) | 第30页：HW1修复回归 |
| [watch.gdb](commands/watch.gdb) | 第29页：观察点 |

作业改编边界见[作业来源](homework/README.md)，C行为规则与验证方式见[行为示例说明](behavior/README.md)。原始作业资料不随发布包分发。
