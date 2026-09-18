# minimus-colorbox

彩色定理盒子宏包，提供定理、示例、日语对照、证明等带框环境。

## 引入的宏包

### `amsthm`

AMS定理环境。

| 宏包 | 说明 |
|------|------|
| `amsthm` | 提供`\newtheorem`命令和`proof`环境，基本的定理证明支持 |

### `aliascnt`

计数器别名。

| 宏包 | 说明 |
|------|------|
| `aliascnt` | 提供`\newaliascnt`命令，创建计数器别名 |

### `tcolorbox`

彩色文本框。

| 宏包 | 说明 |
|------|------|
| `tcolorbox` | 提供`\NewTcbTheorem`等命令，创建彩色文本框|

`\tcbuselibrary`预加载库：

| 库 | 说明 |
|----|------|
| `breakable` | 跨页分割 |
| `theorems` | 定理支持 |

`\tcbset`预配置：

| 选项 | 说明 |
|------|------|
| `arc=0.1mm` | 圆角 |
| `colback=black!3!white` | 浅灰背景 |
| `left=0.2cm` | 左边距 |
| `right=0.2cm` | 右边距 |
| `toptitle=0.05cm` | 标题上方间距 |
| `bottomtitle=0.05cm` | 标题下方间距 |
| `fonttitle=\bfseries\rmfamily` | 标题加粗正体 |
| `breakable` | 允许跨页分割 |
| `lines before break=1` | 至少1行后才允许断页 |
| `separator sign={\ }` | 定理标题分隔符为空格 |
| `theorem hanging indent=0pt` | 长标题第二行左边对齐 |

各类型盒子的配色：

| 类型 | 配色样式 |
|------|----------|
| 定义类（`boxdefstyle`） | 绿灰色 |
| 定理类（`boxthmstyle`） | 蓝灰色 |
| 示例类（`boxexpstyle`） | 青色 |
| 文本类（`boxtxtstyle`） | 红色 |
| 日语例句（`boxjpsetstyle`） | 蓝色，圆角`1.0mm` |
| 日语对话（`boxjpcovstyle`） | 绿色，圆角`1.0mm` |

## 自定义环境

### `BoxDefinition`、`BoxTheorem`、`BoxLemma`、`BoxCorollary`、`BoxProposition`、`BoxProperty`、`BoxFormula`、`BoxEquation`、`BoxExample`、`BoxAlgorithm`、`BoxProcess`、`BoxDesignPrinciple`

定理类盒子，统一参数格式。

```latex
\begin{BoxDefinition}*[title;label]
    ...
\end{BoxDefinition}
```

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `*` | 标记 | 不编号 |
| 2 | `[title;label]` | 可选 | 标题和标签（见下） |

`[title;label]`有几种用法
- `[title]`，标题为`title`，标签为`title`。
- `[title;]`，标题为`title`，无标签。
- `[;label]`，无标题，标签为`label`。
- `[title;label]`，标题为`title`，标签为`label`。
- 在带`*`时，由于已经禁止编号，此时不会创建标签。

| 环境 | 样式 | 计数 | 标签 | 功能 |
|------|------|------|------|------|
| `BoxDefinition` | `boxdefstyle` | `cntboxdef` | `def:label` | 定义 |
| `BoxTheorem` | `boxthmstyle` | `cntboxthm` | `thm:label` | 定理 |
| `BoxLemma` | `boxthmstyle` | `cntboxthm` | `lem:label` | 引理 |
| `BoxCorollary` | `boxthmstyle` | `cntboxthm` | `col:label` | 推论 |
| `BoxProposition` | `boxthmstyle` | `cntboxthm` | `pps:label` | 命题 |
| `BoxProperty` | `boxthmstyle` | `cntboxthm` | `ppt:label` | 性质 |
| `BoxFormula` | `boxthmstyle` | `cntboxthm` | `fml:label` | 公式 |
| `BoxEquation` | `boxthmstyle` | `cntboxthm` | `eqt:label` | 方程 |
| `BoxExample` | `boxexpstyle` | `cntboxexp` | `exp:label` | 示例 |
| `BoxAlgorithm` | `boxtxtstyle` | `cntboxalg` | `alg:label` | 算法 |
| `BoxProcess` | `boxtxtstyle` | `cntboxalg` | `pro:label` | 流程 |
| `BoxDesignPrinciple` | `boxtxtstyle` | `cntboxdespri` | `despri:label` | 设计原则 |

### `JPSentence`、`JPConversation`

日语对照环境。在环境内写日语，在大括号内写中文。

```latex
\begin{JPSentence}{translation}
    ...
\end{JPSentence}
```

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `{translation}` | 可选 | 中文翻译，出现在`\tcblower`之后 |

### `Proof`、`Solution`

证明与解答环境，标题分别为“证明”和“解”。

```latex
\begin{Proof}[reference]
    ...
\end{Proof}
```

```latex
\begin{Solution}[reference]
    ...
\end{Solution}
```

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `[reference]` | 可选 | 引用目标（如`\cref{thm:test}`），默认为空 |

```latex
\begin{Proof}[\cref{thm:main}]
    It is easy to prove.
\end{Proof}
```
