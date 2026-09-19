# VSPBeamer

VSPBeamer提供了一个上科大主题，适用于教学课件和正式汇报的文档类`vsp-beamer`，以Git子模块方式引入，基于`beamer`和`ctex`。

> VSPBeamer的上游是由Heaticy维护的一套Marp/Beamer模板，这是VSPLab的传统Slide模板
>
> - https://github.com/Heaticy/vsp-marp
> - https://github.com/Heaticy/vsp-beamer
>
> 本项目从Heaticy的仓库剥离出了最核心的部分，使之成为一个可按子模块引入的独立组件，适配LumosLaTeX计划的组织方式。



VSPBeamer是LumosLaTeX计划的一部分：https://github.com/liyuxuan3003/LumosLaTeX

若需要完整的模板工程，参见VSPBeamerTemplate：https://github.com/liyuxuan3003/VSPBeamerTemplate

## 主要特点

- 提供红色和紫色两套配色。
- 提供教程和报告两类封面。
- 提供对上海科技大学背景和校徽的支持。
- 专属奶龙主题（？）支持。
- 16:9页面布局，字号由1280x720画布换算得到。
- 使用Latin Modern西文字体和系统Noto CJK SC中文字体。
- 段间提供6pt间距，避免多段落页面粘连。
- 页尾为三格信息栏，由`\VSPsetupfootline`设置；`\alert`为主题色加粗。

## 文档选项

选项直接传入文档类，由`vsp-beamer-theme`解析。

| 选项 | 默认值 | 说明 |
|------|--------|------|
| `red`、`purple`、`nailong` | `red` | 配色，三者互斥，后写覆盖先写 |
| `tutorial`、`report` | `tutorial` | 封面样式，两者互斥，后写覆盖先写 |
| `shtu` | 关闭 | 上海科技大学变体开关 |
| `sectionpages`、`nosectionpages` | `sectionpages` | 自动章节页，两者互斥，后写覆盖先写 |

## 引入方式

VSPBeamer以Git子模块的形式引入项目

```bash
git submodule add git@github.com:liyuxuan3003/VSPBeamer.git vsp-beamer
```

在主文件顶层指定输入路径和素材搜索路径

```latex
\makeatletter\def\input@path{{vsp-beamer}}\makeatother

\graphicspath{{vsp-beamer/assets/}}
```

使用文档类

```latex
\documentclass[red,tutorial,sectionpages]{vsp-beamer}
```

## 自定义命令

### `\VSPtitleframe`、`\VSPsectionframe`、`\VSPendframe`

页面插入命令。

| 命令 | 说明 |
|------|------|
| `\VSPtitleframe` | 输出封面页 |
| `\VSPsectionframe{title}{subtitle}` | 输出自定义章节过渡页 |
| `\VSPendframe{text}` | 输出尾页 |

### `\VSPsetspeaker`、`\VSPspeakerblock`、`\VSPsetupfootline`

信息设置命令。

| 命令 | 说明 |
|------|------|
| `\VSPsetspeaker[label]{name}{detail}` | 设置封面的标签、姓名和详情，并同步`\author`和`\institute` |
| `\VSPspeakerblock` | 输出封面的演讲者信息块 |
| `\VSPsetupfootline{left}{middle}{right}` | 设置页尾三格信息（左/中/右），默认为空，仅适用于非`shtu`主题 |

### `\VSPsetupLogo`、`\VSPsetupNameLogo`、`\VSPbrandmark`

内部命令。

| 命令 | 说明 |
|------|------|
| `\VSPsetupLogo{file}` | 设置页眉标志图片 |
| `\VSPsetupNameLogo{file}` | 设置名称标志图片 |
| `\VSPbrandmark` | 输出页眉标志 |
| `\VSPasset{file}` | 返回素材文件名，配合`\graphicspath`使用 |
| `\vspaccent{text}` | 使用主题强调色加粗输出文本 |
| `\vspmuted{text}` | 使用弱化色输出文本 |

## 自定义环境

### `vspcallout`

可自定义颜色的提示框环境。

```latex
\begin{vspcallout}[color]{title}
    ...
\end{vspcallout}
```

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `[color]` | 可选 | 边框和标题颜色，默认`VSPPrimary` |
| 2 | `{title}` | 必选 | 标题内容 |

### `vspquote`、`vspquoteblue`、`vspquotered`、`vspquotegreen`、`vspquotepurple`、`vspquoteblack`、`vspquoteyellow`

预设颜色的提示框环境。

```latex
\begin{vspquote}{title}
    ...
\end{vspquote}
```

| 序号 | 格式 | 类型 | 说明 |
|------|------|------|------|
| 1 | `{title}` | 必选 | 标题内容 |
