# Minimus

Minimus是个人在长期LaTeX写作中整理出的一套宏包，包含许多自定义命令和环境，并集成了众多常用宏包。

Minimus的名称来源于坎巴拉太空计划（Kerbal Space Program）中对应现实中地球的Kerbin的第二卫星Minmus的错拼。

Minimus是LumosLaTeX计划的一部分：https://github.com/liyuxuan3003/LumosLaTeX

## 核心思想

Minimus的目标是创造可持续的LaTeX写作体验，为每个新工程提供一致的环境

- **常用宏包**：集成常用宏包，例如`physics`、`cleveref`、`graphicx`、`tabularray`等，确保实用命令和环境总是开箱可用。
- **环境包装**：封装原生环境，例如`Equation`、`Figure`、`Table`等，减少冗余代码，简化标签创建。
- **符号缩写**：定义数学符号，例如`\R`、`\e`、`\i`、`\dx`等，为需要特殊字体又具有明确意义的数学符号命名。

Minimus在架构层面是以Git子模块形式引入，这意味着

- Minimus不绑定任何模板，它可以独立的被维护和更新，且可以轻松引入任何项目
- Minimus不存在因更新破坏依赖的问题，你总是可以使用特定版本

## 主要优势

Minimus具体解决了以下问题

- 宏包选择和组合经过长期实践检验，先进且稳定，避免了每次都需要引入大量宏包才能开始写作的困难。
- 引入`physics`宏包，解决了向量和微分等数学排版上的痛点：向量的粗体，微分的正体$\mathrm{d}$，自适应括号的繁琐语法。
- 引入`siunitx`宏包，解决了物理单位的排版问题（单位和数值间的恰当空格，单位需要正体，尤其是μm和μs）。
- 引入`mhchem`宏包，解决了化学符号的排版问题（化学符号需要正体，上下标通常只在斜体的数学环境中可用）。
- 引入`listings`宏包，解决了代码的排版问题（代码文件可以放在外部独立存在，简单可靠的高亮机制）。
- 引入`cleveref`宏包，解决了引用只有计数而无类型的问题（希望得到图2.1而不是2.1）。
- 引入`tabularray`宏包，先进的表格解决方案，内容格式分离，统一横纵单元格合并，统一长表和定宽表。
- 引入`tikz`宏包以及`circuitikz`和`tikz-timing`宏包，高质量的插图绘制方案，最佳的电路图和时序图支持。
- 定义了一系列`\R`、`\C`、`\e`、`\i`等需要`\mathbb`或`\mathrm`字体但又极为常用且有明确意义的数学符号。
- 定义了一系列`\Sum[a][b]`、`\Int[a][b]`、`\Lim[a][b]`等包装命令，避免巨算符`\sum_{a}^{b}`繁琐的上下标语法。
- 定义了`Equation`、`Align`、`Gather`等数学公式环境，集成标签创建。
- 定义了`Figure`、`Table`、`Code`等图表环境和`\figuresub`的子图命令，默认居中，集成标题和标签创建。
- 定义了`BoxDefinition`、`BoxTheorem`等定理环境，基于`tcolorbox`的彩色框，视觉效果好。
- 重定义`\chapter`、`\section`等章节命令，自动用标题创建标签，优化短标题控制。
- `Table`环境和`tblr`深度结合，默认提供三线表。
- `Table`环境可以通过极为简单的`!!`后缀语法启用长表格。
- `\code`命令提供便捷的行内代码体验，自动处理与相邻中文的间距问题（部分特殊符号仍需`\`转义）。
- `\qty`命令在`physics`和`siunitx`间存在命名冲突，后者的被重命名为`\qnum`（也可以继续使用`\SI`保证最大兼容性）。
- `Equation`系列环境提供`!`和`!!`选项，包装自定义的`\forcezero`和`\forceline`，用于修正长公式因编号造成的居中偏移。
- 统一的`[label]`、`[caption;label]`、`{title;label}`标题和标签语法，使用灵活。
- 标题和标签集成在环境参数中，接口统一，不需要独立的`\caption`和`\label`。
- 标签自动根据环境添加`eq:`、`fig:`、`tab:`、`sec:`等前缀。
- 标签在未给出时（`;label`可省略），默认以标题作为标签名，确保标签覆盖率。
- 在中文环境下，使用`\cref`时引用前缀会自动被汉化（Figure 1.1变成图1.1，Chapter 1变成第一章）。

## 宏包列表

使用时请遵照以下顺序加载，调换顺序可能导致错误。

| 宏包 | 文档 |
|------|------|
| `minimus-section` | [minimus-section.md](minimus-section.md) |
| `minimus-text` | [minimus-text.md](minimus-text.md) |
| `minimus-math` | [minimus-math.md](minimus-math.md) |
| `minimus-float` | [minimus-float.md](minimus-float.md) |
| `minimus-code` | [minimus-code.md](minimus-code.md) |
| `minimus-colorbox` | [minimus-colorbox.md](minimus-colorbox.md) |
| `minimus-reference` | [minimus-reference.md](minimus-reference.md) |
| `minimus-bibtex` | [minimus-bibtex.md](minimus-bibtex.md) |
| `minimus-tikz` | [minimus-tikz.md](minimus-tikz.md) |

## 引入方式

Minimus以Git子模块形式引入项目

```bash
git submodule add git@github.com:liyuxuan3003/Minimus.git minimus
```

在主文件顶层指定输入路径以找到子模块中的文件

```latex
\makeatletter\def\input@path{{minimus}}\makeatother
```

在文档中，推荐引入以下包

```latex
\usepackage{minimus-section}
\usepackage{minimus-text}
\usepackage{minimus-math}
\usepackage{minimus-float}
\usepackage{minimus-code}
\usepackage{minimus-colorbox}
\usepackage{minimus-reference}
\usepackage{minimus-bibtex}
```

在插图中，推荐引入以下包

```latex
\usepackage{minimus-text}
\usepackage{minimus-math}
\usepackage{minimus-tikz}
```
