# agent-request

## 目标

- 完成CS100关于Linux基础的课件。

## 信息

- 参考项目：`/home/workspace/Teaching/20260201-CS110/CS110Linux`
- 参考项目：`/home/workspace/Teaching/20260201-CS110/CS110Makefile`
- 参考项目：`/home/workspace/Summary/20250301-UbuntuNote`

## 阶段目标

### 完成迁移

- 首先从CS110迁移内容到这个项目，模板有一些不一样，但环境基本一致。

### 内容调整讨论

- 首先，当前的`vsp-beamer`模板存在缺陷，段间没有间距，尝试给它加个`6pt`。请注意，修改子模块，你需要先切出一个分支，可以是`feature/add-parskip`。
- Linux是什么这一节要大改，名字改成为什么使用Linux？
- 我的想法是，移除操作系统史话，这一部分的逻辑要重构。
- 第一步，简要说明Linux和GNU/Linux以及各个发行版的关系，推荐用Ubuntu。保留原有的第一页，第二页解释Linux是操作系统内核GNU是用户空间工具，两者合并是一个完整的操作系统，但是有很多发行版。常见的有Debian、Ubuntu、Fedora、Centos、Arch。并强调这节课都假定用Ubuntu。
- 第二步，列举Windows的痛点，对比Linux上这些其实很容易。中心思想：有些事情本不应如此繁琐，只是我们习惯如此。这部分会需要几个Windows上操作的截图。我目前想到的痛点有几个。
- 第一，安装软件。在Windows上，安装包要去浏览器搜索，安装路径可以随意改。下载的时候要面对各类欺诈性网页，即便找到了正确的官网，也需要在众多选项中找到正确的下载链接，安装程序还需要手动运行，有些要装`C:`的`Program Files`，有些要在`C:`下的独立目录，许多自作聪明的科普还会告诉你软件不要装`C:`要装`D:`，最后的结果是软件分布在各个地方。然后介绍，在Linux上，安装LaTeX只需要一句话，`sudo apt install texlive-full`。由此引出包管理器的概念，你可能要总结几个要素，软件包被集中管理，软件包有统一的下载安装方式，软件安装有统一固定的安装路径，例如，执行程序和库分别安装到`/bin`和`/lib`。
- 第二，系统更新。在Windows上，更新是强制性的，更新是需要重启的，更新内容是不透明的，更新仅限于操作系统本身。这四个可能要加一些描述。然后介绍，在Linux上，我们并不区分系统软件和应用软件，两者都被统一的`apt`管理，可以一起更新。列出`sudo apt upgrade`和`sudo apt update`并说明两个的差别，你可以随时执行而且无需重启。
- 第三，路径表示。在Windows上，使用`\`作为路径分割符，有盘符`C:`和`D:`的概念。然而，这实际上造成了很多麻烦，因为`\`是许多编程语言的转义，这导致很多时候路径看起来变成`\\`。在Linux上，有统一的`/`根目录，且使用`/`做分隔。
- 第四，命令表示。在Windows上，cmd和powershell非常难用，它的命令名称和命令格式都和主流格格不入。在Linux上，有统一的POSIX规范，有标准的`cd ls`这样的命令，使用`-`短选项和`--`长选项，使用`/`分隔路径，有统一的根目录。这样看其实第三和第四应该合并？这里可以引出一下什么是POSIX规范，并指出其实所有类UNIX系统都遵守（包括MacOS），明确Windows才是那个异类。
- 第五，环境复杂。在Windows上，你可能需要一个庞大的Visual Studio或Anaconda来编写C和Python，它们捆绑了许多无用的图形界面，很容易被困在表象，经常会面对命令不知道在哪里敲（回到前面糟糕的cmd）。在Linux上，gcc和python都是很容易安装的，对照教程很容易学习，编辑器可以另外配置。
- 第三步，介绍Linux是一个成熟的系统，也有图形界面，也可以做很多事情。列举一些例子，核心其实是，有些有开源替代或更好的做法，有些也有商业软件支持。
- 给一个例子，命令行简洁，但也可以用图形，仍然有类似文件资源管理器的东西，软件包下载也可以有图形界面。
- 文档和表格，Word这类图形化的编辑本身就是糟糕的，可以用Markdown或LaTeX替代，Powerpoint这类，Markdown有Marp，LaTeX有Beamer，本质没有区别，只是一种特殊的文档。Excel本质是数据处理，可以用csv存储数据用pandas这类Python库处理数据。如果仍然需要处理，开源的有Libra Office，但可用性不佳，商业的有WPS支持。PDF阅读器是自带的。
- 网页和邮件，浏览器有Firefox，邮件客户端有Thunderbird。
- 可能要再找些各个方面的例子？图像（GIMP Inkscape），照片（Digikam Rawtherapee），密码管理器（pass），C/C++开发（gcc g++ make，可以提一下arm开发keil是伪需求），Python开发（python conda uv），代码编辑器（vscode同样可用，vscodium更好），电路板（Kicad），机加工（Freecad），FPGA（Vivado有linux，纯仿真有verilator和gtkwave）
- 游戏，Minecraft能玩，Steam有兼容层，除了各别反作弊，说一下Steam OS，现场展示Minecraft和帝国时代2。
- 可以放一个著名的fuck nvidia的图，但说明现在显卡支持已经非常好了。
- 第四步，给出wsl和双系统的方案，指出需要ubuntu24.04或ubuntu26.04。
- Linux的远程连接这一节直接删除，不要了。
