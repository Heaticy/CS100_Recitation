# minimus-text

文本排版工具宏包，提供下划线、编号、注音等文本排版命令。

## 引入的宏包

### `ulem`

下划线工具。

| 宏包 | 说明 |
|------|------|
| `ulem` | 提供`\uline`、`\uuline`、`\uwave`、`\sout`、`\xout`等多种下划线和删除线样式 |

在中文环境下（检测到`xeCJK`包时）额外加载`xeCJKfntef`，使`ulem`的线型命令兼容中文，并提供`\dotcnuline`命令。

### `xurl`

URL断行工具。

| 宏包 | 说明 |
|------|------|
| `xurl` | 修复`\url`命令无法在任意字符处断行的问题 |

### `xcolor`

颜色支持。

| 宏包 | 说明 |
|------|------|
| `xcolor` | 提供`\color`、`\textcolor`等命令，预加载`dvipsnames`、`svgnames`、`x11names`颜色集 |

### `pifont`

符号字体。

| 宏包 | 说明 |
|------|------|
| `pifont` | 提供`\ding`命令，可访问PostScript符号集中的特殊字符 |

### `tikz`

绘图工具（基础）。

| 宏包 | 说明 |
|------|------|
| `tikz` | 基本TikZ绘图支持，加载`positioning`库，`\fg`命令依赖此宏包 |

## 自定义命令

### `\dotcnuline`

中文逐字加点式下划线。仅在中文环境（加载`xeCJK`时）可用。

| 命令 | 说明 |
|------|------|
| `\dotcnuline{text}` | 为每个中文字符下方添加一个点（`\CJKunderdot`） |

### `\circnum`、`\circnumdark`

带圈数字。

| 命令 | 说明 |
|------|------|
| `\circnum{n}` | 空心圈数字，`n`取值1-10 |
| `\circnumdark{n}` | 实心圈数字，`n`取值1-10 |

### `\romannum`、`\Romannum`

罗马数字。

| 命令 | 说明 |
|------|------|
| `\romannum{n}` | 小写罗马数字，如`\romannum{6}`输出vi |
| `\Romannum{n}` | 大写罗马数字，如`\Romannum{6}`输出VI |

### `\fg`

日语振假名（汉字上方标注读音假名）。依赖TikZ排版。

| 命令 | 说明 |
|------|------|
| `\fg{kanji}{furigana}` | 在汉字上方排版振假名 |

```latex
\fg{日本}{にほん}
```
