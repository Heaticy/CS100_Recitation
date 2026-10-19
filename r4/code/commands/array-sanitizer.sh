mkdir -p build/demo
gcc -std=c17 -g -O0 -Wall -Wextra -Wpedantic -Werror \
    -fsanitize=address \
    code/sanitizer/array_loop.c -o build/demo/array-loop-asan
./build/demo/array-loop-asan
