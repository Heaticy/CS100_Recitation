# minimus-reference

交叉引用宏包，提供中文格式的智能引用（`cleveref`）。

## 引入的宏包

### `hyperref`

超链接支持。

| 宏包 | 说明 |
|------|------|
| `hyperref` | 提供`\ref`、`\cite`的超链接跳转，预配置`hidelinks`（隐藏链接边框） |

### `aliascnt`

计数器别名。

| 宏包 | 说明 |
|------|------|
| `aliascnt` | 提供`\newaliascnt`命令，实现计数器别名 |

### `cleveref`

智能引用。

| 宏包 | 说明 |
|------|------|
| `cleveref` | 提供`\cref`和`\Cref`命令，自动添加引用类型前缀 |

`cleverref`原先和`beamer`文档类冲突，经过改进，可以正常使用，但引用多个目标时链接只能指向第一个。

`cleverref`原先默认使用英文，经过改进，在检测到中文环境后，会自动使用以下的汉化。

| 引用类型 | 格式 |
|----------|------|
| `part` | 第X部分 |
| `chapter` | 第X章 |
| `section` | 第X节 |
| `subsection` | 第X小节 |
| `subsubsection` | 第X小节 |
| `appendix` | 附录X |
| `figure` | 图X |
| `table` | 表X |
| `equation` | 式(X) |
| `listing` | 代码X |
| `boxdefinition` | 定义X |
| `boxtheorem` | 定理X |
| `boxlemma` | 引理X |
| `boxcorollary` | 推论X |
| `boxproposition` | 命题X |
| `boxproperty` | 性质X |
| `boxformula` | 公式X |
| `boxequation` | 方程X |
| `boxexample` | 例X |
| `boxalgorithm` | 算法X |
| `boxprocess` | 流程X |
| `boxdesignprinciple` | 设计原则X |
