#!/usr/bin/env python3
"""Check the observable behavior used in the lecture, including intentional bugs."""

import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "build/demo/output"
OUTPUT.mkdir(parents=True, exist_ok=True)
# These cases check bounds, lifetime and arithmetic, not leak detection.
# LeakSanitizer's ptrace probe is unavailable in some restricted environments.
ENV = dict(os.environ, ASAN_OPTIONS="detect_leaks=0")


def run(name, data=""):
    result = subprocess.run(
        [str(ROOT / "build/demo" / name)], input=data,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        universal_newlines=True, cwd=str(ROOT), timeout=15, env=ENV,
    )
    (OUTPUT / (name + ".txt")).write_text(result.stdout + result.stderr)
    return result


def expect(name, expected, data=""):
    result = run(name, data)
    assert result.returncode == 0, (name, result.returncode, result.stderr)
    assert result.stdout.strip() == expected, (name, result.stdout, expected)
    assert not result.stderr, (name, result.stderr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-gdb", action="store_true")
    args = parser.parse_args()

    expect("grades", "150", "3\n59 60 90\n")
    for data, expected in (("3\n59 60 90\n", "75"), ("1\n60\n", "60"),
                           ("0\n", "No passing scores"), ("2\n40 59\n", "No passing scores")):
        expect("grades-fixed", expected, data)
    result = run("grades-fixed", "1\n101\n")
    assert result.returncode == 1 and not result.stdout
    print("PASS: complete C grade program and threshold/input checks")

    expect("hw0-input", "623", "123 500\n")
    result = run("hw0-input", "123\n")
    assert result.returncode == 1 and not result.stdout
    expect("hw1-p3", "10 10", "3 5 2 0\n")
    expect("hw1-p3-wide", "10 5", "3 5 2 0\n")
    expect("hw1-p3-wide", "2147483648 2147483647", "2147483647 1 0\n")
    for data, expected in (
        ("3 5 2 0\n", "10 5"), ("5 0\n", "5 5"),
        ("5 5 2 0\n", "12 5"), ("3 0 99\n", "3 3"),
        ("-5 -2 -9 0\n", "-16 -2"), ("1 2 3 0\n", "6 3"),
    ):
        expect("hw1-p3-fixed", expected, data)
    result = subprocess.run(
        [str(ROOT / "build/demo/argv-first"), "-std=c17", "-Wall", "hello.c", "-o", "hello"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, timeout=15)
    assert result.returncode == 0 and result.stdout == "-\n-\nh\n-\nh\n", result
    print("PASS: HW0 input checking, HW1 sum/max regression and HW2 argv excerpt")

    for name, wrong, fixed in (
        ("sum", "3", "8"), ("sum-three", "3", "6"),
        ("poly-division", "6.000", "10.750"),
        ("exercise", "8.000", "17.000"),
    ):
        expect(name, wrong)
        expect(name + "-fixed", fixed)
    print("PASS: C pass-by-value/pointer update, division and polynomial exercise")

    for name, error, fixed, data, source in (
        ("polynomial-bounds", "stack-buffer-overflow", "17.000", "", "polynomial.c"),
        ("sum-overflow", "signed integer overflow", "2147483648", "2147483647 1 0\n", "sum-overflow.c"),
        ("use-after-free", "heap-use-after-free", "90", "", "use-after-free.c"),
        ("power-ubsan", "signed integer overflow", "2500000000", "", "power.c"),
        ("array-loop-asan", "stack-buffer-overflow", "1", "", "array_loop.c"),
    ):
        result = run(name, data)
        # UBSan normally reports signed overflow and continues; ASan aborts.
        if name not in ("sum-overflow", "power-ubsan"):
            assert result.returncode != 0, (name, result.stdout, result.stderr)
        assert error in result.stderr, (name, result.stderr)
        assert "code/sanitizer/" + source + ":" in result.stderr
        expect(name + "-fixed", fixed, data)
    print("PASS: polynomial/array ASan, accumulation/power UBSan and lifetime extension")

    gdb = shutil.which(os.environ.get("GDB", "gdb"))
    if not gdb:
        assert not args.require_gdb, "GDB is required but unavailable"
        print("SKIP: GDB session (install gdb, then use --require-gdb)")
        return
    result = subprocess.run(
        [gdb, "-q", "-nx", "-batch", "-x", "code/commands/session.gdb",
         "./build/demo/hw1-p3"], cwd=str(ROOT), stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, universal_newlines=True, timeout=30,
    )
    (OUTPUT / "gdb-session.txt").write_text(result.stdout)
    assert result.returncode == 0, result.stdout
    for evidence in (
        r"\$1 = 8", r"\$2 = 3", r"#0.*updateMaximum", r"#1.*main",
        r"\$3 = 5", r"\$4 = 8", r"Old value = 3", r"New value = 8",
        r"10 10", r"exited normally",
    ):
        assert re.search(evidence, result.stdout), (evidence, result.stdout)
    print("PASS: GDB conditional breakpoint, values, backtrace and watchpoint")

    for session, executable, arguments, evidence in (
        ("sum-value", "sum", [], (r"\$1 = 3", r"\$2 = 8", r"\$3 = 3")),
        ("sum-pointer", "sum-fixed", [], (r"\$1 = 3", r"\$2 = 8", r"\$3 = 8")),
        ("exercise", "exercise", [], (r"\$1 = 1", r"\$2 = 3", r"\$3 = 8", r"8\.000")),
        ("argv-session", "argv-first", ["-std=c17", "-Wall", "hello.c", "-o", "hello"],
         (r"\$1 = 6", r'"-std=c17"')),
    ):
        result = subprocess.run(
            [gdb, "-q", "-nx", "-batch", "-x", "code/commands/" + session + ".gdb",
             "--args", "./build/demo/" + executable] + arguments,
            cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            universal_newlines=True, timeout=30,
        )
        (OUTPUT / ("gdb-" + session + ".txt")).write_text(result.stdout)
        assert result.returncode == 0, result.stdout
        for pattern in evidence:
            assert re.search(pattern, result.stdout), (pattern, result.stdout)
    print("PASS: GDB C value/pointer updates, polynomial boundary and argc/argv")

    for session, executable, evidence in (
        ("power-session", "power-ubsan", (r"\$1 = 1", r"\$2 = 50000", r"\$3 = 50000")),
        ("array-session", "array-loop-asan", (r"\$1 = 6", r"\$2 = \{1, 1, 1, 1, 1, 1\}", r"\$3 = 24")),
    ):
        result = subprocess.run(
            [gdb, "-q", "-nx", "-batch", "-ex", "set pagination off",
             "-x", "code/commands/" + session + ".gdb", "./build/demo/" + executable],
            cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            universal_newlines=True, timeout=30,
        )
        (OUTPUT / ("gdb-" + session + ".txt")).write_text(result.stdout)
        assert result.returncode == 0, result.stdout
        for pattern in evidence:
            assert re.search(pattern, result.stdout), (pattern, result.stdout)
    print("PASS: GDB power and array stop before the invalid operation")


if __name__ == "__main__":
    main()
