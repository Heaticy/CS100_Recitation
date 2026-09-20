# agent-log

## 2026.09.17 10:00

- 从CS110的CS110Linux项目迁移Linux基础课件到本项目，适配vsp-beamer模板。
- 迁移`code/`代码示例目录，与CS110保持一致。
- 迁移`Section01.tex`至`Section05.tex`，覆盖Linux是什么、基本命令、目录结构、权限管理、远程连接五个章节。
- 重写主文件`CS100Linux.tex`，改用vsp-beamer接口：`\VSPtitleframe`、`\VSPsetspeaker`、`\VSPendframe`等，并加载五个Section。
- 主文件标题暂定`Linux基础`/`CS100`，后续可按实际情况调整。
- 编译通过，共83页，无Overfull警告。

## 2026.09.17 12:37

- 修复`vsp-beamer`子模块段间无间距的问题：在`feature/add-parskip`分支上为`vsp-beamer-theme.sty`增加`\parskip=6pt`与`\parindent=0pt`，并同步更新README。该分支仅在本地提交，尚未推送上游。
- 大改第一章：`\section{Linux是什么}`改为`\section{为什么使用Linux？}`。
- 移除操作系统史话（Unix/BSD/GNU的历史叙述），重构为四步：Linux与GNU/Linux及发行版的关系；Windows的痛点（安装软件、系统更新、路径与命令、开发环境）与Linux的对比；Linux作为成熟桌面系统的能力（文档表格、网络通信、图形图像、开发工具、工程软件、游戏、显卡）；WSL与双系统的入门方案。
- 重写`Section01.tex`，共25页，新增`code/init/`下的示例脚本。Windows相关截图暂以`% TODO`占位，未插入图片。
- 删除`Section05.tex`远程连接一节，并从主文件移除对应`\input`，同时删除仅供该节使用的`code/shell/ssh.sh`、`scp.sh`、`passwd.sh`、`code/no-password.sh`。
- 编译通过，共90页，无Overfull警告与错误。

## 2026.09.17 15:44

- 确认第一章发行版术语：使用“Centos系”指代该分支，使用“Redhat”而非“RHEL”。这是教学取舍，CentOS在国内计算机教育中认知度高，Redhat比RHEL更直观，非笔误，后续不要“修正”。
- 第一节的发行版列表保持为：Debian系（Debian、Ubuntu）、Centos系（Fedora、Centos、Redhat）、Arch系（Arch Linux）。

## 2026.09.18 21:20

- 图片体积优化：原图（41MB）移到`CS100Linux/image/origin/`归档，用ImageMagick统一处理生成压缩版到`CS100Linux/image/`。
- 处理方式：`convert -resize '1600x1600>' -strip -interlace Plane -quality 85`，即最长边压到1600像素、去除元数据、渐进式JPEG、质量85。
- 所有引用图片由`.png`改为`.jpg`（`Section01.tex`共17处），`fuck-u-nvidia.jpg`保持`.jpg`。
- 优化后图片总计约3.3MB（约12倍压缩），关闭草稿选项后完整PDF约3.1MB，编译约8秒。
- `CS100Linux.tex`中`\setkeys{Gin}{draft}`（临时草稿选项）保持原样未动。
- 注意：`origin/`中原图仍被git跟踪，用于将来重新处理，正常编译只使用`image/`根目录下的压缩版。

## 2026.09.19 02:26

- 移植Heaticy/vsp-beamer上游当日两个提交（828f9a7、2ac7093）至打包版`vsp-beamer-theme.sty`：子模块新建`feature/marp-parity`分支（基于v2.1），改动行与上游主题文件逐行一致，并同步README。
- 改动内容：章节页标题字号22.68pt放大至35.43pt（对应Marp 100px），长标题只在空格与CJK边界换行（新增`\vsp@displaywrap`，字体选择移入节点`font=`键）；`\textbf`重定义为主题色加粗、`\alert`仅变色，课件中22处`\textbf`将随之变为强调色；shtu页码上移（`dp=0.10cm`改`0.20cm`）；代码框线颜色从`VSPTeal`改为`VSPPrimary!45!white`。
- 已确认`vsp-beamer.cls`与`minimus`内部不使用`\textbf`，重定义不影响模板自身结构。
- r1子模块指针更新至`feature/marp-parity`，注意该分支尚未推送liyuxuan3003上游，推送前其他克隆无法解析该指针。
- 关闭草稿选项后重新全量编译，共101页，无Overfull警告与错误。

## 2026.09.19 02:55

- 结构重构：去除全部子模块，改为仓库内共享模板。决策原因：上游实际开发在Heaticy/vsp-beamer，课程经`liyuxuan3003/VSPBeamer`打包层+子模块指针消费，链路过长且多次出现本地分支指针不可解析的问题；vendor后主题更新简化为「上游diff套用到`template/vsp-beamer/`」一跳。
- 新结构：`template/`（vsp-beamer、minimus、makefile-latex三个原子模块内容直接纳入仓库）+`r1/`（源码平铺：tex、Makefile、code/、image/）+顶层agent工作流文件。
- r1仓库（cs100linux.git）历史经`git subtree add`完整并入顶层并保留（含Marp对齐移植），gitlab上的cs100linux.git未动，可作归档或删除；本地嵌套`.git`与备份`r1-migrate/`在验证内容无损后删除。注意：子模块内仅本地存在的`feature/marp-parity`分支引用随嵌套`.git`一并移除，其内容已vendor进`template/vsp-beamer/vsp-beamer-theme.sty`（逐字节校验一致）。
- 构建接线：`r1/Makefile`前置定义`CLSS_VSP_BEAMER`等变量指向`../template`（利用`latex-std-dependence.mk`的`?=`可覆盖性），主文件`\input@path`与`\graphicspath`同步改路径；xelatex从源码目录运行，相对路径成立。
- 全量编译验证通过，共101页，无Overfull警告与错误，与重构前页数一致。

## 2026.09.19 03:10

- 页尾改版：新增`\VSPsetupfootline{left}{middle}{right}`，左中右三格分别为课程与习题课节次、年份、主讲者，替代原页尾（shtu居中页码框/非shtu短标题+节名+页码框），页码不再展示。
- 页尾模板统一shtu与非shtu变体；shtu背景图底部左右角有校园剪影与书法装饰（实测高约0.50–0.55cm），shtu下三格整行上移至`dp=0.68cm`避开，非shtu保持贴底`dp=0.10cm`。
- 尾页底部同步展示同一行三格信息（shtu白底用`VSPMuted`，红底用`white!82`）。
- r1主文件设置三格为`CS100 Recitation 1`/`Fall 2026`/`Yuxuan Li`，模板README同步记录。
- 编译验证：101页，无Overfull警告与错误；抽查正文页、目录页、尾页渲染，页尾三格与装饰条、正文均无冲突。

## 2026.09.19 03:28

- 修正三格页尾在shtu下的行为：shtu背景图底部左右角有装饰，三格行会重叠，因此shtu页尾恢复居中页码框，`\VSPsetupfootline`三格信息仅在尾页底部展示；无背景图的变体仍逐页展示三格。该行为同步至模板README与上游文档。
- 上游同步：`/home/lichf/workspace/vsp-beamer`（Heaticy/vsp-beamer）提交`5820e7e`并推送GitHub与GitLab镜像，含三格页尾、shtu行为、尾页信息行与文档；已跑`make check`全量通过（非shtu模板页尾空槽、shtu页码框均渲染验证）。
- 新增`.gitlab-ci.yml`：`build`作业每次推送编译并产出`dist/CS100-Recitation1.pdf`（保留14天）；`release`作业打tag时编译并创建GitLab release，PDF以`CS100-Recitation1.pdf`命名挂为可下载产物。runner使用`latex-runner`标签（与vsp-beamer仓库一致）。
- 推送本仓库至gitlab（cs100/cs100_recitation）。首次release：`git tag v0.1.0 && git push origin v0.1.0`。

## 2026.09.19 14:48

- 新增r0习题课（环境配置），从marp版`CS100-Fall2025-Recitation-00.md`迁移为beamer格式。
- 合并伪动画重复页：第一节6页合并为2页（编辑器/编译器/IDE一页、我们到底需要什么一页），其余各节同样精简；原marp的`trans`过渡页改为`\section`自动章节页，`toc_a`目录页保留为`\tableofcontents`。
- 代码块统一使用`Code`环境包裹`\lstinputlisting`（与r1一致），代码素材落在`r0/code/`下按主题分目录；图片素材复制自`env_setup/img/`到`r0/img/`。
- 修复`\code{...}+\code{...}`在xeCJK+listings下的peek冲突：改为单个`\code{Ctrl+Alt+T}`的写法，避免`+`被xeCJK的`__xeCJK_listings_peek_active_loop`误解析。
- 编译验证：39页，无Overfull警告与错误；抽查封面、内容页、代码页、尾页渲染正常。
- CI更新：`build`与`release`作业同时编译r0和r1，产出`CS100-Recitation0.pdf`与`CS100-Recitation1.pdf`；顶层README补充r0目录说明。

## 2026.09.20 16:34

- 新增独立`intro/`课件，复用红色上科大Beamer模板，按致敬GKxx、TA自我介绍、课程理念组织内容。
- 原样收录用户提供的图片，GKxx经历与贡献按用户提供的信息编写。
- 按用户确认，TA自我介绍页留空；课程语言标准为C17和C++17，编译器具体版本不擅自指定。
- 课程理念覆盖问题建模、C与Python差异、AI时代的理解与验证、编译环境、代码习惯和Git版本管理。
- 编译生成23页PDF，无Overfull、Underfull或缺字警告，已检查全部页面缩略图。

## 2026.09.20 16:35

- 将intro接入CI的编译验证与tag发布流程，发布产物新增`CS100_Intro.pdf`；普通推送仍只编译验证。
- README补充intro目录、构建命令、TA空白页位置及课程标准，并修正已有主文件名称。
- intro增量编译通过，CI配置通过YAML解析及发布规则检查；本次不打tag、不触发release。

## 2026.09.20 16:39

- 在GKxx介绍后新增Bilibili主页截图页，说明深入学习C/C++语言细节可参考其讲课视频，环境配置应跟随新版r0课件。
- 原样保存用户提供的新截图，保留原致敬图片；编译通过，共24页，新增页已检查排版，无溢出或缺字。
