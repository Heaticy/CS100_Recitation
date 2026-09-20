# CS100_Recitation

CS100习题课课件仓库。共享模板位于`template/`，各习题课在独立目录持有自己的源码、演示代码与图片。

## 目录结构

```
CS100_Recitation
|- template/          # 共享模板：vsp-beamer文档类、minimus宏包、makefile-latex构建系统
|- intro/            # 课程导论：致敬GKxx、TA自我介绍与课程理念
|  |- CS100_Intro.tex
|  |- Section01.tex…
|  |- code/
|  |- image/
|  |- Makefile
|- r1/                # 习题课一（Linux基础），在该目录下运行make编译
|  |- build/
|  |- code/           # 课堂演示代码
|  |- image/          # 课件图片（origin/为原图归档）
|  |- Makefile
|  |- CS100_Recitation1.tex
|  |- Section01.tex…
|- r0/                # 习题课零（环境配置），在该目录下运行make编译
|  |- build/
|  |- code/           # 课堂演示代码
|  |- img/            # 课件图片
|  |- Makefile
|  |- CS100_Recitation0.tex
|  |- Section01.tex…
|- AGENTS.md          # agent工作流约定
|- agent-request.md
|- agent-log.md
```

## 构建

在习题课目录下运行

```bash
make -j
```

输出PDF位于`build/`，清理使用`make clean`。

导论课件可使用`make -j -C intro`编译，输出为`intro/build/CS100_Intro.pdf`。TA自我介绍页位于`intro/Section02.tex`，依次为李超凡、李宇轩、蒋烨与王诗涵。课程语言标准为C17与C++17。

CI在普通推送时编译验证intro、r0和r1；仅打tag时发布三份PDF。

## 模板

`template/`直接纳入本仓库管理，不使用子模块。其内容源自VSPBeamer（上科大Beamer主题）、Minimus与MakefileLaTeX，均为LumosLaTeX计划的组成部分。更新主题时，将上游改动套用到`template/vsp-beamer/`后提交即可。
