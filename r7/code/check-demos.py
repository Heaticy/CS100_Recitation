#!/usr/bin/env python3
"""Compile the slide fragments in context and check the behavior they teach."""
from pathlib import Path
import os
import re
import shlex
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / 'code'
CXX = shlex.split(os.environ.get('CXX', 'c++'))
FLAGS = ['-std=c++17', '-Wall', '-Wextra', '-Werror', '-pedantic']
HEADERS = '''#include <cassert>
#include <iostream>
#include <stdexcept>
#include <string>
#include <type_traits>
'''
CONST_ERROR = r'discards qualifiers|not marked const|const.*this|this.*const'
DEFAULT_ERROR = r'no matching function.*Student::Student|no matching constructor'
covered = set()
passed = []


def fragment(name):
    covered.add(name)
    return (CODE / name).read_text(encoding='utf-8')


def split_main(source):
    """Keep the displayed class-body fragment separate from its call site."""
    return source.split('// In main():', 1)


constructor = fragment('constructor.inc')
setter = fragment('set-name.inc')
graduated = fragment('names.inc')
fields = fragment('init-order.inc').split('// Write initializers', 1)[0]


def student(*, getter=None, graduation=None, destructor=''):
    if getter is None:
        getter = 'std::string getName() const { return m_name; }\n'
    if graduation is None:
        graduation = graduated
    return ('class Student {\nprivate:\n' + fields + '\npublic:\n'
            + constructor + setter + graduation + getter
            + 'std::string getID() const { return m_id; }\n'
            + destructor + '\n};\n')


def main(body):
    return '\nint main() {\n' + body + '\n}\n'


def check(directory, name, source, *, expected='', error=None):
    cpp = directory / (name + '.cpp')
    executable = directory / name
    cpp.write_text(HEADERS + source, encoding='utf-8')
    result = subprocess.run(CXX + FLAGS + [str(cpp), '-o', str(executable)],
                            text=True, capture_output=True, timeout=30)
    if error is not None:
        assert result.returncode != 0, (name, 'expected a compilation error')
        assert re.search(error, result.stderr, re.I | re.S), (name, result.stderr)
        kind = 'expected compilation error'
    else:
        assert result.returncode == 0, (name, result.stderr)
        result = subprocess.run([str(executable)], text=True, capture_output=True,
                                timeout=5)
        assert result.returncode == 0, (name, result.returncode, result.stderr)
        assert result.stdout == expected, (name, result.stdout, expected)
        kind = 'compiled and ran'
    passed.append(kind)
    print('PASS', name + ':', kind)


with tempfile.TemporaryDirectory(prefix='cs100-r7-') as temporary:
    directory = Path(temporary)

    # Link the displayed declarations to later definitions; do not read the
    # integer member before the constructor lesson has supplied its initial value.
    member_definitions = (
        setter.replace('bool setName(', 'bool Student::setName(', 1)
        + graduated.replace('bool graduated(', 'bool Student::graduated(', 1)
        + 'std::string Student::getName() const { return m_name; }\n')
    check(directory, 'member-declarations', fragment('members.inc')
          + member_definitions + main('''
        Student s;
        assert(s.getName().empty());
        assert(s.setName("Alice"));
        const Student &view = s;
        assert(view.getName() == "Alice");
    '''))

    check(directory, 'constructor-and-invariants', student() + main('''
        Student early("Alice", "19000001", 1900);
        Student late("Bob", "21000001", 2100);
        assert(early.getName() == "Alice" && late.getID() == "21000001");
        assert(!early.graduated(1903) && early.graduated(1904));
        int rejected = 0;
        try { Student bad("", "20260001", 2026); }
        catch (const std::invalid_argument &) { ++rejected; }
        try { Student bad("Alice", "", 2026); }
        catch (const std::invalid_argument &) { ++rejected; }
        try { Student bad("Alice", "20260001", 1899); }
        catch (const std::invalid_argument &) { ++rejected; }
        try { Student bad("Alice", "20260001", 2101); }
        catch (const std::invalid_argument &) { ++rejected; }
        assert(rejected == 4);
    '''))

    check(directory, 'interface-state-and-object-independence', student()
          + main(fragment('use-interface.inc') + '''
        assert(ok1 && !ok2 && s.getName() == "Alicia");
        Student b("Bob", "20280001", 2028);
        s.setName("Alice");
        assert(b.getName() == "Bob");
        assert(s.graduated(2030) && !b.graduated(2030));
    '''), expected='Alicia\n')

    access = fragment('access.inc')
    check(directory, 'public-interface', student()
          + main(access + 'assert(s.getName() == "Alicia");'))
    check(directory, 'private-access-rejected', student()
          + main('Student s("Alice", "20260001", 2026); s.m_name = "";'),
          error=r'private')

    defaults = fragment('default-access.inc')
    check(directory, 'struct-and-class-defaults', defaults + '''
        static_assert(std::is_convertible<Open *, Base *>::value);
        static_assert(!std::is_convertible<Closed *, Base *>::value);
    ''' + main('Record r{2026}; assert(r.m_year == 2026);'))
    check(directory, 'class-default-private', defaults
          + main('Hidden h; h.m_year = 2026;'), error=r'private')

    protected_class, protected_main = split_main(fragment('protected.inc'))
    check(directory, 'protected-derived-access', protected_class
          + main(protected_main + 'assert(value == 1);'))
    external_access = protected_main.replace('// d.m_value = 2;', 'd.m_value = 2;')
    assert external_access != protected_main, 'protected access probe was not uncommented'
    check(directory, 'protected-external-access-rejected', protected_class
          + main(external_access + '(void)value;'), error=r'protected')
    private_base = protected_class.replace('protected:', 'private:', 1)
    assert private_base != protected_class, 'private base probe did not change its access'
    check(directory, 'private-derived-access-rejected', private_base
          + main(protected_main + 'assert(value == 1);'), error=r'private')

    public_class, public_main = fragment('public-data.inc').split('Student s{2026};', 1)
    check(directory, 'public-data-bypasses-invariant', public_class
          + main('Student s{2026};' + public_main
                 + 'assert(s.m_entranceYear == -1);'))

    method, calls = split_main(fragment('this.inc'))
    check(directory, 'this-selects-current-object', student(graduation=method)
          + main('''Student a("Alice", "20260001", 2026);
                    Student b("Bob", "20280001", 2028);
          ''' + calls + 'assert(a.graduated(2030) && !b.graduated(2030));'))

    method, calls = split_main(fragment('const-view.inc'))
    check(directory, 'const-view', student(getter=method) + main(calls),
          expected='Alice\n')
    check(directory, 'returned-name-does-not-expose-state', student() + main('''
        const Student s("Alice", "20260001", 2026);
        std::string name = s.getName();
        name = "Bob";
        assert(s.getName() == "Alice");
    '''))

    method, calls = split_main(fragment('const-error.inc'))
    check(directory, 'missing-const-rejected', student(getter=method) + main(calls),
          error=CONST_ERROR)

    declarations, calls = split_main(fragment('const-exercise.inc'))
    exercise_class = ('class Student {\nprivate:\n' + fields
                      + '\npublic:\n' + constructor + declarations + '\n};\n')
    definitions = ('std::string Student::getID() const { return m_id; }\n'
                   + graduated.replace('bool graduated(', 'bool Student::graduated(', 1)
                   + setter.replace('bool setName(', 'bool Student::setName(', 1))
    exercise = exercise_class + definitions
    check(directory, 'const-exercise', exercise
          + main(calls + 'assert(s.graduated(2030));'))
    check(directory, 'const-setter-rejected', exercise
          + main('const Student s("Alice", "20260001", 2026); s.setName("Bob");'),
          error=CONST_ERROR)

    default_calls = fragment('default-ctor.inc')
    check(directory, 'explicit-student-construction', student()
          + main(default_calls + '(void)a;'))
    check(directory, 'no-default-constructor', student() + main('Student b;'),
          error=DEFAULT_ERROR)
    check(directory, 'initializer-values', student() + main('''
        Student s("Alice", "20260001", 2026);
        assert(s.getName() == "Alice" && s.getID() == "20260001");
        assert(!s.graduated(2029) && s.graduated(2030));
    '''))
    wrong_order = student().replace(
        ': m_name(name), m_id(id), m_entranceYear(year)',
        ': m_entranceYear(year), m_id(id), m_name(name)')
    assert wrong_order != student(), 'initializer order probe did not alter the constructor'
    check(directory, 'initializer-order-warning', wrong_order + main(''), error=r'reorder')

    destructor, lifetime = split_main(fragment('lifetime.inc'))
    check(directory, 'local-object-lifetime', student(destructor=destructor)
          + main(lifetime), expected='Bob leaves\nAlice leaves\n')
    scalar = fragment('new-delete.inc')
    assert re.search(r'new\s+Student\s*\(', scalar), 'scalar example must create a Student'
    assert re.search(r'delete\s+p\s*;', scalar), 'scalar new must pair with scalar delete'
    check(directory, 'dynamic-object-lifetime', student(destructor=destructor)
          + main(scalar + 'assert(p == nullptr);'), expected='Alice\nAlice leaves\n')

    array = fragment('array.inc')
    assert re.search(r'new\s+int\s*\[', array), 'array example must use new[]'
    assert re.search(r'delete\s*\[\s*\]\s*scores\s*;', array), 'new[] must pair with delete[]'
    check(directory, 'dynamic-array-values-and-release', main(array
          + 'assert(scores == nullptr);'), expected='90 95\n')

    available = {path.name for path in CODE.glob('*.inc')}
    assert covered == available, ('uncovered fragments', sorted(available - covered))

positive = passed.count('compiled and ran')
negative = passed.count('expected compilation error')
print(f'All {len(covered)} C++17 fragments passed: '
      f'{positive} compile/run checks and {negative} expected rejections.')
