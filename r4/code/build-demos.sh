#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
mkdir -p build/demo
c_compiler=${CC:-gcc}
c_flags=(-std=c17 -g -O0 -Wall -Wextra -Wpedantic -Werror)
sanitizer=(-fsanitize=address,undefined)
"$c_compiler" "${c_flags[@]}" code/homework/hw0-input.c -o build/demo/hw0-input
"$c_compiler" "${c_flags[@]}" code/homework/argv-first.c -o build/demo/argv-first
for name in grades hw1-p3; do
    case "$name" in
        grades) source_file=code/gdb/grades.c ;;
        hw1-p3) source_file=code/homework/hw1-p3.c ;;
    esac
    "$c_compiler" "${c_flags[@]}" "$source_file" -o "build/demo/$name"
    "$c_compiler" "${c_flags[@]}" "code/fixed/$name.c" -o "build/demo/$name-fixed"
done
for name in sum sum-three poly-division; do
    "$c_compiler" "${c_flags[@]}" "code/c/$name.c" -o "build/demo/$name"
    "$c_compiler" "${c_flags[@]}" "code/fixed/$name.c" -o "build/demo/$name-fixed"
done
"$c_compiler" "${c_flags[@]}" code/fixed/hw1-p3-wide.c -o build/demo/hw1-p3-wide
"$c_compiler" "${c_flags[@]}" code/exercise/polynomial.c -o build/demo/exercise
"$c_compiler" "${c_flags[@]}" code/fixed/polynomial.c -o build/demo/exercise-fixed
for name in polynomial-bounds sum-overflow; do
    case "$name" in
        polynomial-bounds) source_file=code/sanitizer/polynomial.c ;;
        sum-overflow) source_file=code/sanitizer/sum-overflow.c ;;
    esac
    "$c_compiler" "${c_flags[@]}" "${sanitizer[@]}" "$source_file" -o "build/demo/$name"
    "$c_compiler" "${c_flags[@]}" "${sanitizer[@]}" "code/fixed/$name.c" -o "build/demo/$name-fixed"
done
for name in power array_loop; do
    case "$name" in
        power) sanitizer_flag=-fsanitize=undefined; binary_name=power-ubsan ;;
        array_loop) sanitizer_flag=-fsanitize=address; binary_name=array-loop-asan ;;
    esac
    "$c_compiler" "${c_flags[@]}" "$sanitizer_flag" "code/sanitizer/$name.c" -o "build/demo/$binary_name"
    "$c_compiler" "${c_flags[@]}" "$sanitizer_flag" "code/fixed/$name.c" -o "build/demo/$binary_name-fixed"
done
# This standalone, deliberately faulty example may also receive a compiler warning.
# Keep the warning visible so the runtime diagnostic can still be demonstrated.
"$c_compiler" -std=c17 -g -O0 -Wall -Wextra -Wpedantic "${sanitizer[@]}" \
    code/sanitizer/use-after-free.c -o build/demo/use-after-free
"$c_compiler" "${c_flags[@]}" "${sanitizer[@]}" \
    code/fixed/use-after-free.c -o build/demo/use-after-free-fixed
echo 'Built C17 homework-based classroom variants in build/demo/'
