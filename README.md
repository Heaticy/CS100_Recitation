# CS100_Recitation

CS100习题课课件仓库。共享模板位于`template/`，各习题课在独立目录持有自己的源码、演示代码与图片。

## 目录结构

```
CS100_Recitation
|- template/          # 共享模板：vsp-beamer文档类、minimus宏包、makefile-latex构建系统
|- r1/                # 习题课一（Linux基础），在该目录下运行make编译
|  |- build/
|  |- code/           # 课堂演示代码
|  |- image/          # 课件图片（origin/为原图归档）
|  |- Makefile
|  |- CS100Linux.tex
|  |- Section01.tex…
|- r0/                # 习题课零（环境配置），在该目录下运行make编译
|  |- build/
|  |- code/           # 课堂演示代码
|  |- img/            # 课件图片
|  |- Makefile
|  |- CS100EnvSetup.tex
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

## 模板

`template/`直接纳入本仓库管理，不使用子模块。其内容源自VSPBeamer（上科大Beamer主题）、Minimus与MakefileLaTeX，均为LumosLaTeX计划的组成部分。更新主题时，将上游改动套用到`template/vsp-beamer/`后提交即可。
