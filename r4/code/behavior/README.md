# C17行为分类示例

用于当前课件第46—50页，讨论整数、字符、格式匹配、数组边界与作用域。源码末尾标注具体页码，完整入口见[代码索引](../README.md)。课堂演示环境为8位char、32位int。

| 源码 | 规则与观察结果 |
|---|---|
| [signed-overflow.c](signed-overflow.c) | INT_MAX减2后加3：有符号溢出，UB |
| [unsigned-wrap.c](unsigned-wrap.c) | UINT_MAX减2后加3：无符号回绕，输出0 |
| [format-mismatch.c](format-mismatch.c)、[format-fixed.c](format-fixed.c) | double与%d不匹配为UB，改%.2f输出2.25 |
| [digit-promotion.c](digit-promotion.c) | 字符整数提升，输出7；数字字符连续由C标准保证 |
| [char-signedness.c](char-signedness.c) | 普通char的符号属性由实现定义；两种编译选项分别输出-1和255 |
| [bounds.c](bounds.c)、[bounds-fixed.c](bounds-fixed.c) | 六元素数组访问下标6为UB；修复后输出1 |
| [scope.c](scope.c)、[scope-fixed.c](scope-fixed.c) | show不能访问main的局部变量；通过形参传入后输出17 |

“有定义行为”是本课对明确遵循语言规则情形的教学用语；UB、实现定义与有定义不是穷尽的标准分类，另外还有未指定行为。使用未声明标识符属于需诊断的翻译错误，应先与运行时问题区分。

## 验证与复现

准备好GCC及Sanitizer运行库后，从`r4/`执行：

```bash
make check-behavior
```

编译产物、标准输出及诊断保存于`build/behavior/`。故意的格式不匹配示例分别按启用／关闭-Werror编译以检查诊断，不执行其未定义行为来预测某个输出。作用域错误应编译失败。有符号溢出与数组越界分别检查UBSan、ASan诊断；其他例子核对输出且要求无Sanitizer诊断。检测器自身的输出只验证演示环境，行为分类仍依据C语言规则。

## 规则依据

- [C标准草案N1570](https://www.open-std.org/JTC1/SC22/WG14/www/docs/n1570.pdf)：3.4术语；5.2.1字符集；6.2.1作用域；6.2.5整型；6.3.1.1整数提升；6.5表达式；6.5.6指针与数组；7.21.6.1格式实参类型。
- [GCC语言标准选项](https://gcc.gnu.org/onlinedocs/gcc/C-Dialect-Options.html)：C17是对C11的勘误修订，另说明-fsigned-char／-funsigned-char。
- [GCC整型实现说明](https://gcc.gnu.org/onlinedocs/gcc/Integers-implementation.html)：普通char的默认符号属性与目标平台有关。
