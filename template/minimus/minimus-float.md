# minimus-float

图表排版宏包，提供表格和图片环境，支持长表格、子图、标签。

## 引入的宏包

### `float`

浮动体位置控制。

| 宏包 | 说明 |
|------|------|
| `float` | 提供`[H]`位置参数，禁止浮动体浮动 |

### `caption`、`subcaption`

标题与子标题。

| 宏包 | 说明 |
|------|------|
| `caption` | 提供`\caption`、`\captionof`命令 |
| `subcaption` | 提供`\subcaptionbox`命令 |

预配置设置：

| 选项 | 说明 |
|------|------|
| `captionsetup[table]{skip=6.0pt}` | 表格标题间距 |
| `captionsetup[figure]{skip=6.0pt,belowskip=-8pt}` | 图片标题间距 |
| `captionsetup[subfigure]{belowskip=0pt}` | 子图标题间距 |
| `subcaptionsetup{labelformat=simple}` | 子图标签仅显示`(a)` |

### `tabularray`

现代表格排版。

| 宏包 | 说明 |
|------|------|
| `tabularray` | 提供`tblr`环境，现代化的表格环境支持 |

### `multirow`

跨行合并单元格。

| 宏包 | 说明 |
|------|------|
| `multirow` | 提供`\multirow`命令，用于简单场景下的表格跨行 |

### `graphicx`、`pdfpages`

图形插入。

| 宏包 | 说明 |
|------|------|
| `graphicx` | 提供`\includegraphics`命令，支持插入PDF、PNG、JPG等图片 |
| `pdfpages` | 提供`\includepdf`命令，支持插入完整PDF页面 |

## 自定义命令

### `\linenone`、`\linesplit`、`\linemiddle`、`\lineborder`

表格线宽度预设。

| 命令 | 说明 |
|------|------|
| `\linenone` | 0.0pt，无宽度线 |
| `\linesplit` | 0.2pt，分隔线 |
| `\linemiddle` | 0.4pt，中间线 |
| `\lineborder` | 1.0pt，边框线 |

该设置是用在`tblr`环境的格式设置上，例如`hline{even[2-Z]}={\linesplit}`。

### `\figuresub`

子图命令，在`Figure`环境内使用。

| 命令 | 说明 |
|------|------|
| `\figuresub*[caption;label]{graphics}{width}` | 排版子图，带`*`时不编号 |

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `*` | 标记 | 子图不编号 |
| 2 | `[caption;label]` | 可选 | 标题和标签，格式为`\label{fig:label}`|
| 3 | `{graphics}` | 必选 | `\includegraphics{...}`命令 |
| 4 | `{width}` | 可选 | `width\linewidth`的子图宽度，默认自适应 |

`[caption;label]`有几种用法
- `[caption]`，标题为`caption`，标签为`caption`。
- `[caption;]`，标题为`caption`，无标签。
- `[;label]`，无标题，标签为`label`。
- `[caption;label]`，标题为`caption`，标签为`label`。
- 在带`*`时，由于已经禁止编号，此时不会创建标签。

## 自定义环境

### `Table`

表格环境，是`table`环境的包装，默认使用`[H]`。

```latex
\begin{Table}*[caption;label]&&!!
    ...
\end{Table}
```

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `*` | 标记 | 表格不编号 |
| 2 | `[caption;label]` | 可选 | 标题和标签，格式为`tab:label` |
| 3 | `&` | 标记 | 移除中间线 |
| 4 | `&` | 标记 | 移除边框线 |
| 5 | `!` | 标记 | 启用浮动体，使用`[htbp]`而非`[H]` |
| 6 | `!` | 标记 | 启用长表格 |

`[caption;label]`有几种用法
- `[caption]`，标题为`caption`，标签为`caption`。
- `[caption;]`，标题为`caption`，无标签。
- `[;label]`，无标题，标签为`label`。
- `[caption;label]`，标题为`caption`，标签为`label`。
- 在带`*`时，由于已经禁止编号，此时不会创建标签。

`Table`环境是专门为`tblr`适配的，自动产生三线表。

```latex
\begin{Table}[My Table;mytable]!
    \begin{tblr}{colspec={XX}}
        English & Greek \\
        A & $\alpha$ \\
        B & $\beta$ \\
        C & $\theta$ \\
        D & $\delta$ \\
    \end{tblr}
\end{Table}
```

```latex
% Use ! suffix to have float table
\begin{Table}[My Float Table]!
```

```latex
% Use !! suffix to have long table
\begin{Table}[My Long Table]!!
```

### `Figure`

图片环境，是`figure`环境的包装，默认使用`[H]`。

```latex
\begin{Figure}*[caption;label]!
    ...
\end{Figure}
```

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `*` | 标记 | 图片不编号 |
| 2 | `[caption;label]` | 可选 | 标题和标签，格式为`fig:label`|
| 3 | `!` | 标记 | 启用浮动，使用`[htbp]`而非`[H]` |

`[caption;label]`有几种用法
- `[caption]`，标题为`caption`，标签为`caption`。
- `[caption;]`，标题为`caption`，无标签。
- `[;label]`，无标题，标签为`label`。
- `[caption;label]`，标题为`caption`，标签为`label`。
- 在带`*`时，由于已经禁止编号，此时不会创建标签。

`Figure`环境中如果要排版多行的子图，可以简单的用一个空行。

```latex
\begin{Figure}[My Figure;myfigure]
    \includegraphics{image.pdf}
\end{Figure}
```

```latex
\begin{Figure}[Many Figures]
    \figuresub[PartA;a]{\includegraphics{PartA.pdf}}{0.35}
    \figuresub[PartB;b]{\includegraphics{PartB.pdf}}{0.45}

    \figuresub[PartC]{\includegraphics{PartC.pdf}}
\end{Figure}
```

```latex
% Use ! suffix to have float figure
\begin{Figure}[My Float Figure]!
```
