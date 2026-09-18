# VSPBeamerTemplate

VSPBeamerTemplate是一个开箱即用的LaTeX模板，适用于教学课件和正式汇报，具有上科大主题，基于自定义文档类`vsp-beamer`。

VSPBeamerTemplate是LumosLaTeX计划的一部分：https://github.com/liyuxuan3003/LumosLaTeX

https://github.com/liyuxuan3003/VSPBeamerTemplate.git

> VSPBeamer的上游是由Heaticy维护的一套Marp/Beamer模板，这是VSPLab的传统Slide模板
> 
> - https://github.com/Heaticy/vsp-marp
> - https://github.com/Heaticy/vsp-beamer
>
> Heaticy的版本实际上更加完善。本项目存在的主要目的是适配LumosLaTeX计划的组织方式。

## 引入方式

克隆模板仓库

```bash
git clone git@github.com:liyuxuan3003/VSPBeamerTemplate.git
```

初始化项目

```
cd VSPBeamerTemplate
./init.sh MyProject
```

初始化会自动完成项目重命名、子模块加载、移除模板的远程引用等操作，只能执行一次。

## 目录结构

项目的目录结构如下

```
VSPBeamerTemplate   # The root of git repo
|- .git
|- MyProject        # The sub dir of source files (run make here!)
.  |- build/
.  |- makefile-latex/
.  |- minimus/
.  |- vsp-beamer/
.  |- Makefile
.  |- MyProject.tex
.  |- Section01.tex
|- .gitignore
|- .gitmodules
|- init.sh
|- README.md
|- VSPBeamerTemplate.md
```

请注意，根目录下仅有`.gitignore`和`README.md`等文件，代码均位于一个二级目录下！

## 构建方式

模板提供`Makefile`进行编译，任何`make`命令都需要在二级目录下运行。

编译文档及其插图

```bash
make -j
```

清理文档输出目录

```bash
make clean
```

## 子模块

模板的具体使用方式，请参见各个子模块的文档。

| 子模块 | 文档 |
|--------|------|
| `vsp-beamer` | [README](CS100Linux/vsp-beamer/README.md) |
| `minimus` | [README](CS100Linux/minimus/README.md) |
| `makefile-latex` | [README](CS100Linux/makefile-latex/README.md) |
