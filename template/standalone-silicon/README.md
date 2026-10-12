# StandaloneSilicon

StandaloneSilicon提供了一个适用于独立TikZ绘图的文档类`standalone-silicon`，以Git子模块方式引入，基于`standalone`。

StandaloneSilicon的命名遵守"功能+同首字母元素名"的规则，Silicon为第14号元素硅（Si）。

StandaloneSilicon是LumosLaTeX计划的一部分：https://github.com/liyuxuan3003/LumosLaTeX

推荐搭配Minimus使用：https://github.com/liyuxuan3003/Minimus

## 主要特点

- 基于`standalone`，适用于创建独立的TikZ绘图。
- 添加了中文字体和中文支持。

## 引入方式

StandaloneSilicon以Git子模块的形式引入项目

```bash
git submodule add git@github.com:liyuxuan3003/StandaloneSilicon.git standalone-silicon
```

在主文件顶层指定输入路径

```latex
\makeatletter\def\input@path{{standalone-silicon}}\makeatother
```

使用文档类

```latex
\documentclass{standalone-silicon}
```

## 最小示例

搭配Minimus的最小示例

```latex
\makeatletter\def\input@path{{minimus}{standalone-silicon}}\makeatother

\documentclass{standalone-silicon}

\usepackage{minimus-text}
\usepackage{minimus-math}
\usepackage{minimus-tikz}

\begin{document}
\begin{tikzpicture}

\end{tikzpicture}
\end{document}
```
