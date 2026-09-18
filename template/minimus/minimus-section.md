# minimus-section

章节命令增强宏包，重定义标准章节命令以支持分号语法自动标签。

## 引入的宏包

### `apptools`

附录检测工具。

| 宏包 | 说明 |
|------|------|
| `apptools` | 提供`\IfAppendix`命令，用于判断当前是否处于附录环境 |

## 自定义命令

`minimus-section`不定义新的用户命令，而是重定义标准LaTeX章节命令，为它们增加自动标签功能。

`minimus-section`重定义的命令包括`\part`、`\chapter`、`\section`、`\subsection`、`\subsubsection`。

这些重定义在`beamer`文档类中不生效。

### `\part`、`\chapter`、`\section`、`\subsection`、`\subsubsection`

标准章节命令的增强版本，支持分号语法自动生成标签。

| 命令 | 说明 |
|------|------|
| `\part*[short]{title;label}!` | 重定义的`\part`|
| `\chapter*[short]{title;label}!` | 重定义的`\chapter`|
| `\section*[short]{title;label}!` | 重定义的`\section`|
| `\subsection*[short]{title;label}!` | 重定义的`\subsection`|
| `\subsubsection*[short]{title;label}!` | 重定义的`\subsubsection`|

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `*` | 标记 | 禁止编号 |
| 2 | `[short]` | 可选 | 短标题，用于页眉和目录 |
| 3 | `{title;label}` | 必选 | 标题和标签（见下） |
| 4 | `!` | 标记 | 控制短标题范围（见下） |

`{title;label}`有几种用法
- `{title}`，标题为`title`，标签为`title`。
- `{title;}`，标题为`title`，无标签。
- `{title;label}`，标题为`title`，标签为`label`。
- 在带`*`时，由于已经禁止编号，此时不会创建标签。

`!`标记控制短标题的使用范围：

- 无`!`：短标题仅用于PDF书签，页眉和目录仍用完整标题
- 有`!`：短标题同时用于PDF书签、页眉和目录

标签前缀按层次自动分配：

| 命令 | 标签格式 |
|------|----------|
| `\part` | `part:label` | |
| `\chapter` | `chap:label` / `ap:label`| |
| `\section` | `sec:label` | |
| `\subsection` | `subsec:label` | |
| `\subsubsection` | `subsubsec:label` | |

```latex
\section{Introduction;Intro}

\subsection{History}

See \cref{sec:Intro} and \cref{subsec:History}.
```
