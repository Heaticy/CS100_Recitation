#!/usr/bin/env python3
"""Check the C17 behavior examples without predicting outputs for UB."""
import os
from pathlib import Path
import shlex
import subprocess

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "code" / "behavior"
BUILD = ROOT / "build" / "behavior"
BUILD.mkdir(parents=True, exist_ok=True)
COMPILER = shlex.split(os.environ.get("CC", "gcc"))
FLAGS = ["-std=c17", "-g", "-O0", "-Wall", "-Wextra", "-Wpedantic"]
ENV = dict(os.environ, ASAN_OPTIONS="detect_leaks=0")


def compile_case(name, extra=(), tag=None, reject=None, strict=True):
    label = tag or name
    executable = BUILD / label
    args = COMPILER + FLAGS + (["-Werror"] if strict else [])
    args += list(extra) + [str(SOURCES / (name + ".c")), "-o", str(executable)]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True, env=ENV)
    (BUILD / (label + ".compile.txt")).write_text(result.stdout + result.stderr)
    if reject:
        assert result.returncode != 0 and reject in result.stderr, result.stderr
        return None
    assert result.returncode == 0, result.stderr
    return executable


def run_case(executable, output=None, diagnostic=None, fatal=True):
    result = subprocess.run([str(executable)], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, universal_newlines=True,
                            env=ENV)
    (BUILD / (executable.name + ".stdout.txt")).write_text(result.stdout)
    (BUILD / (executable.name + ".stderr.txt")).write_text(result.stderr)
    if diagnostic:
        assert diagnostic in result.stderr, result.stderr
        if fatal:
            assert result.returncode != 0, result.stderr
    else:
        assert result.returncode == 0, result.stderr
        assert result.stdout == output, (executable.name, result.stdout)
        assert not result.stderr, result.stderr


ubsan = ["-fsanitize=undefined"]
asan = ["-fsanitize=address"]
both = ["-fsanitize=address,undefined"]
run_case(compile_case("signed-overflow", ubsan),
         diagnostic="signed integer overflow", fatal=False)
run_case(compile_case("unsigned-wrap", both), output="0\n")
run_case(compile_case("format-fixed", both), output="2.25\n")
run_case(compile_case("digit-promotion", both), output="7\n")

# The slide explicitly demonstrates an 8-bit-char, 32-bit-int environment.
probe = subprocess.run(COMPILER + ["-dM", "-E", "-x", "c", "-"], input="",
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       universal_newlines=True, env=ENV)
assert probe.returncode == 0, probe.stderr
assert "#define __CHAR_BIT__ 8\n" in probe.stdout
assert "#define __INT_MAX__ 0x7fffffff\n" in probe.stdout
run_case(compile_case("char-signedness", ["-fsigned-char"], "char-signed"),
         output="-1\n")
run_case(compile_case("char-signedness", ["-funsigned-char"], "char-unsigned"),
         output="255\n")

run_case(compile_case("bounds", asan), diagnostic="stack-buffer-overflow")
run_case(compile_case("bounds-fixed", both), output="1\n")
compile_case("scope", reject="undeclared")
run_case(compile_case("scope-fixed", both), output="17\n")

# Format UB is classified from the C rule. Compile diagnostics are inspected;
# an unchecked printf mismatch is deliberately never executed for a result.
compile_case("format-mismatch", reject="format")
compile_case("format-mismatch", tag="format-warning-only", strict=False)
warning = (BUILD / "format-warning-only.compile.txt").read_text()
assert "format" in warning and "double" in warning, warning
print("C17 behavior examples passed: defined outputs, char modes, UBSan/ASan reports,")
print("scope diagnostics, and printf warning versus -Werror; logs: build/behavior/")
