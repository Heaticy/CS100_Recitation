#!/usr/bin/env python3
"""Package R4 with its PDF and shared templates, excluding local build tools."""

import hashlib
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent.parent
SLIDES = ROOT.parent
NAME = "CS100_Recitation4"
PREFIX = NAME + "/"
PDF = ROOT / "build" / (NAME + ".pdf")
DEST = ROOT / "build" / "dist"


def main():
    if not PDF.is_file() or not PDF.read_bytes().startswith(b"%PDF-"):
        raise SystemExit("Missing lecture PDF; run make in r4/ first.")
    files = {}
    # Explicit source directories avoid copying .git, tools, logs or binaries.
    for directory in (ROOT / "code", ROOT / "image", SLIDES / "template"):
        for path in sorted(directory.rglob("*")):
            if (not path.is_file() or path.is_symlink()
                    or any(part.startswith(".") or part in ("build", "__pycache__")
                           for part in path.relative_to(directory).parts)
                    or path.suffix in (".pyc", ".o", ".aux", ".log", ".synctex")):
                continue
            files[path.relative_to(SLIDES).as_posix()] = path.read_bytes()
    # Only public root documents belong in the submission package.
    for path in sorted(ROOT.iterdir()):
        if path.is_file() and (path.suffix == ".tex" or path.name in ("README.md", "Makefile")):
            files["r4/" + path.name] = path.read_bytes()
    files["r4/build/" + PDF.name] = PDF.read_bytes()
    files["README.md"] = """# CS100 Recitation 4

GDB、Sanitizer与C语言代码调试。此目录可直接作为独立GitHub仓库的内容。

- [课件PDF](r4/build/CS100_Recitation4.pdf)
- [使用说明](r4/README.md)
- [源码与课件页码索引](r4/code/README.md)

保留`r4/`与`template/`的相对位置。在Ubuntu／WSL中准备GCC、GDB、Make、Python3后运行：

```bash
cd r4
make demos
make check-all
```

重新编译PDF还需TeX Live、latexmk与中文字体，在`r4/`运行`make -j`。
重新打包运行`make package`，输出位于`r4/build/dist/`。
`SHA256SUMS`列出所有包内文件的校验值，可在本目录运行`sha256sum -c SHA256SUMS`。
原作业、本机工具与Git历史不随包分发。错误示例用于教学，部分程序预期报告错误或编译失败。
""".encode("utf-8")
    files[".gitignore"] = b"**/build/*\n!r4/build/CS100_Recitation4.pdf\n__pycache__/\n*.pyc\n"
    checksums = "".join("{}  {}\n".format(hashlib.sha256(data).hexdigest(), name)
                        for name, data in sorted(files.items()))
    files["SHA256SUMS"] = checksums.encode("utf-8")
    DEST.mkdir(parents=True, exist_ok=True)
    archive = DEST / (NAME + "_GitHub.zip")
    with zipfile.ZipFile(str(archive), "w", compression=zipfile.ZIP_DEFLATED) as output:
        for name, data in sorted(files.items()):
            output.writestr(PREFIX + name, data)
    with zipfile.ZipFile(str(archive)) as output:
        assert output.testzip() is None
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix(".zip.sha256").write_text("{}  {}\n".format(digest, archive.name))
    print("Packaged {} files: {}".format(len(files), archive))
    print("SHA256: " + digest)


if __name__ == "__main__":
    main()
