# 示意图

`c-python-execution.svg`是C与Python执行流程的可编辑矢量源文件，使用Noto Sans CJK SC字体。课件嵌入同名PDF，以便XeLaTeX直接编译。

修改SVG后，在仓库根目录执行：

```bash
python3 intro/tools/export-diagram.py
make -j -C intro
```

导出脚本需要PyGObject、librsvg和Python的Cairo绑定。SVG与导出的PDF应一起提交；普通课件编译与CI直接使用已提交的PDF，无需安装SVG导出依赖。
