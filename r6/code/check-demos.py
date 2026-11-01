#!/usr/bin/env python3
"""Compile and exercise the complete slide examples, not the .inc fragments."""
from pathlib import Path
import os
import shlex
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'build' / 'demo'
OUT.mkdir(parents=True, exist_ok=True)
CXX = shlex.split(os.environ.get('CXX', 'c++'))
CASES = {
    'hello': ('', 'Hello, C++!\n'),
    'io': ('20 22\n', '42\n'),
    'string-basics': ('', 'Hello, C++!\nHello\nsize=11\n'),
    'string-io': ('Ada Lovelace\n', 'Hello, Ada Lovelace!\n'),
    'vector-basics': ('', 'size=5 front=1 back=12\n1 3 5 7 12 \nsize=4 back=7\n'),
    'vector-read': ('5\n10 20 30 40 50\n', '50 40 30 20 10\n'),
}
for source in sorted((ROOT / 'code').glob('*.cpp')):
    subprocess.run(CXX + ['-std=c++17', '-Wall', '-Wextra', '-Werror', '-pedantic',
                          '-O0', '-g', str(source), '-o', str(OUT / source.stem)],
                   check=True, timeout=30)
for name, (data, expected) in CASES.items():
    result = subprocess.run([str(OUT / name)], input=data, text=True,
                            capture_output=True, check=True, timeout=5)
    assert result.stdout == expected, (name, result.stdout, expected)
    print('PASS', name)
for name, inputs in {
    'io': ('not-a-number\n',),
    'vector-read': ('-1\n', '3\n1 2\n'),
    'string-io': ('',),
}.items():
    for data in inputs:
        result = subprocess.run([str(OUT / name)], input=data, text=True,
                                capture_output=True, timeout=5)
        assert result.returncode != 0 and not result.stdout, (name, data, result)
    print('PASS', name + ': invalid/missing input rejected')
result = subprocess.run([str(OUT / 'growth')], text=True,
                        capture_output=True, check=True, timeout=5)
rows = [[int(field) for field in line.split()] for line in result.stdout.splitlines()]
assert len(rows) == 17 and all(len(row) == 2 for row in rows), rows
assert [row[0] for row in rows] == list(range(1, 18)), rows
capacities = [row[1] for row in rows]
assert all(capacity >= size for size, capacity in rows), rows
assert all(later >= earlier for earlier, later in zip(capacities, capacities[1:])), rows
print('PASS growth: size/capacity invariants')
print('All complete C++17 examples passed.')
