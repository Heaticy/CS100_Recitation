mkdir -p build/demo
gcc -std=c17 -g -O0 -Wall -Wextra -Wpedantic -Werror \
    code/c/sum.c -o build/demo/sum
gdb ./build/demo/sum
