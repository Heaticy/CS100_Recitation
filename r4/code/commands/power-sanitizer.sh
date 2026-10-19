mkdir -p build/demo
gcc -std=c17 -g -O0 -Wall -Wextra -Wpedantic -Werror \
    -fsanitize=undefined \
    code/sanitizer/power.c -o build/demo/power-ubsan
./build/demo/power-ubsan
