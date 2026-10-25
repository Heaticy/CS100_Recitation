#!/usr/bin/env python3
"""Compile and exercise the complete slide examples, not the .inc fragments."""
from pathlib import Path
import ctypes
import os
import re
import shlex
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'build' / 'demo'
OUT.mkdir(parents=True, exist_ok=True)
CC = shlex.split(os.environ.get('CC', 'cc'))
CASES = {
    'by-value': ('', 'inside: 42\noutside: 10\n'),
    'by-address': ('', '42\n'),
    'lifetime': ('', '1 1 11\n1 2 12\n'),
    'malloc': ('', '42\n'),
    'calloc': ('', '0 0\n'),
    'array': ('5\n', '0\n'),
    'realloc': ('', '10 20 30 40\n'),
    'owned': ('', '42\n'),
    'list': ('', '20 10\n'),
    'pointer': ('', '4 4\n'),
    'add-two': ('', '0 2\n'),
    'macro-mul': ('', '18\n4\n'),
    'macro-min': ('', '2 3\n3\n'),
}
for source in sorted((ROOT / 'code').glob('*.c')):
    subprocess.run(CC + ['-std=c17', '-Wall', '-Wextra', '-Werror', '-pedantic',
                        '-O0', '-g', str(source), '-o', str(OUT / source.stem)],
                   check=True, timeout=30)
for name, (data, expected) in CASES.items():
    result = subprocess.run([str(OUT / name)], input=data, text=True,
                            capture_output=True, check=True, timeout=5)
    assert result.stdout == expected, (name, result.stdout, expected)
    print('PASS', name)
for data in ('0\n', 'not-a-number\n', f'{ctypes.c_size_t(-1).value}\n'):
    result = subprocess.run([str(OUT / 'array')], input=data, text=True,
                            capture_output=True, timeout=5)
    assert result.returncode != 0 and not result.stdout, (data, result)
print('PASS array: invalid/zero/excessive size rejected')
for name, status in [('bss', 0), ('data', 1)]:
    result = subprocess.run([str(OUT / name)], timeout=5)
    assert result.returncode == status, (name, result.returncode)
result = subprocess.run([str(OUT / 'macro-size')], text=True,
                        capture_output=True, check=True, timeout=5)
assert re.fullmatch(r'Size of long long: [1-9][0-9]*\nSize of int: [1-9][0-9]*\n',
                    result.stdout), result.stdout
print('PASS bss/data and platform-dependent sizeof output')
print('All complete C17 examples passed.')
