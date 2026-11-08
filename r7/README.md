# CS100 Recitation 7

C++Class基础复习，约60分钟。以Lecture14的Student为主线，重点讲封装、接口与const，补充析构及new/delete。全部示例按C++17验证。

## 源码组织

- `CS100_Recitation7.tex`：入口、课程目标、封面与尾页。
- `Section01.tex`：对象、命名、访问权限、封装与接口。
- `Section02.tex`：this与const成员函数。
- `Section03.tex`：构造、初始化、默认构造、析构及动态对象。
- `code/*.inc`：课件实际引用的短代码片段，不是独立程序；各页按上下文逐步补齐Student。标有Error的行用于讲解编译错误。
- `Makefile`：复用仓库共享构建规则，不复制模板。

## 构建

依赖与仓库根README一致：Linux或WSL、make、latexmk、XeLaTeX、TeXLive及NotoCJK字体。在本目录运行：

```bash
make -j
```

输出为`build/CS100_Recitation7.pdf`。不提交生成文件、字体、旧版本、完整演示程序或个人授课稿；不改动r0至r6及共享template。

## 课堂节奏

PDF共25个物理页，含封面、3页章节页、尾页。页脚仅为正文帧号，逐页讲稿使用物理页号。

建议对象与接口约23分钟，this与const约13分钟，构造与生命周期约21分钟，开场和结束约3分钟。提问停顿计入课堂时间。

## 验收记录

- 实际运行`make -j`成功；最终PDF共25个物理页，无Overfull、Underfull或缺字诊断，所用字体全部嵌入。共享模板的包路径和PDF资产版本提示不影响编译。
- 17个片段全部按C++17检验：14项正常编译运行检查通过，8项预期编译拒绝的诊断符合教学目标。检查覆盖接口失败时状态保留、构造输入边界、const、访问权限、初始化顺序及自动/动态/数组对象的析构顺序。
- 最终课件已逐页检查；中文逐字讲稿按PDF物理页对应，渲染后25页，建议60分钟含提问停顿。个人交付仅PDF和Word，均不提交仓库。
- 本次不改GitHubActions、GitLabCI或发布流程，不打tag。
