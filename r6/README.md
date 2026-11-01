# CS100 Recitation 6：从C到C++

本讲帮助熟悉C的学生过渡到C++17，重点介绍输入输出、`std::string`、`std::vector`，以及动态容器的资源管理、容量增长和访问失效。示例对照保留C17写法，但不把“替换库函数”误当成C++的全部变化。

## 内容结构

- **输入输出与程序结构**：`iostream`、流运算符、命名空间、C标准库的C++头文件，以及`std::endl`与换行符的区别。
- **字符串**：对象初始化、复制、连接、比较、边界检查、范围for、按单词和按行输入、`c_str()`接口。
- **动态数组**：`std::vector<T>`初始化、独立拷贝、大小与首尾操作、动态读入、遍历、边界和类模板参数推导。
- **资源与增长**：RAII、`size()`与`capacity()`、均摊常数追加、`reserve()`、引用与迭代器失效。

## 页面安排与建议进度

PDF共47个物理页，其中41个为编号帧；物理页还包含封面、5个分节页和结束页。

| 物理页 | 内容 | 90分钟课堂建议 |
|---|---|---|
| 1–3 | 封面、过渡问题、目录 | 0–5分钟：从手写C字符串和动态数组的问题出发 |
| 4–13 | 输入输出与程序结构 | 5–15分钟 |
| 14–24 | `std::string` | 15–35分钟 |
| 25–36 | `std::vector` | 35–60分钟 |
| 37–45 | 资源管理、增长与失效 | 60–80分钟 |
| 46–47 | 迁移总结、结束页 | 80–85分钟 |

本讲无练习附录；如需布置课后练习，在课程平台另行发布。

## 构建

需要XeLaTeX、`latexmk`、支持C++17的`g++`和Python 3。

```bash
make -j
make check-demos
```

- 课件输出：`build/CS100_Recitation6.pdf`。
- `make check-demos`使用`-std=c++17 -Wall -Wextra -Werror -pedantic`编译并运行完整示例，同时检查正常输入、失败输入和容量增长不变量。
- `build/`是生成目录，不属于课件源文件。

## 完整示例与预期结果

`code/`中的7份`.cpp`都是可以独立编译运行的完整程序。

| 程序 | 示例输入 | 预期结果 |
|---|---|---|
| `hello.cpp` | 无 | 输出`Hello, C++!` |
| `io.cpp` | `20 22` | 输出`42` |
| `string-basics.cpp` | 无 | 三行输出`Hello, C++!`、`Hello`和`size=11` |
| `string-io.cpp` | `Ada Lovelace` | 输出`Hello, Ada Lovelace!` |
| `vector-basics.cpp` | 无 | 三行输出`size=5 front=1 back=12`、`1 3 5 7 12`和`size=4 back=7` |
| `vector-read.cpp` | `5`，随后`2 3 5 7 11` | 逆序输出`11 7 5 3 2` |
| `growth.cpp` | 无 | 输出17组大小与容量；大小依次为1至17，容量不减且始终不小于大小 |

`growth.cpp`的具体容量序列由标准库实现决定，检查脚本不假定每次恰好翻倍。输入失败时，`io.cpp`、`string-io.cpp`和`vector-read.cpp`返回非零状态；`vector-read.cpp`也拒绝负数元素个数。

字符分类示例在调用`std::isspace`和`std::isupper`前将`char`转换为`unsigned char`，避免负的`char`值造成未定义行为。

## 代码片段与来源

- `CS100_Recitation6.tex`是主文件，`Section01.tex`至`Section04.tex`按主题组织页面。
- `code/*.inc`是供LaTeX清单引用的局部片段。部分片段故意展示错误，或省略外围变量与函数，不应单独编译。
- 完整程序与幻灯片片段共享相同写法；课堂讨论以完整程序的可运行行为为准。

本讲由旧版`CS100-recitations-fall2025/r6/r6.md`的Marp讲稿改编为当前仓库的Beamer格式，保留输入输出、字符串和动态数组主线，重组为四个课堂章节，并为完整示例加入C++17自动检查。
