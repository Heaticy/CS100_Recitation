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
- 重写`Section01.tex`，共25页，新增`code/why/`下的示例脚本。Windows相关截图暂以`% TODO`占位，未插入图片。
- 删除`Section05.tex`远程连接一节，并从主文件移除对应`\input`，同时删除仅供该节使用的`code/shell/ssh.sh`、`scp.sh`、`passwd.sh`、`code/no-password.sh`。
- 编译通过，共90页，无Overfull警告与错误。

## 2026.09.17 15:44

- 确认第一章发行版术语：使用“Centos系”指代该分支，使用“Redhat”而非“RHEL”。这是教学取舍，CentOS在国内计算机教育中认知度高，Redhat比RHEL更直观，非笔误，后续不要“修正”。
- 第一节的发行版列表保持为：Debian系（Debian、Ubuntu）、Centos系（Fedora、Centos、Redhat）、Arch系（Arch Linux）。
