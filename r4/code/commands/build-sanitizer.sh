mkdir -p build/demo
gcc -std=c17 -g -O0 -Wall -Wextra -Wpedantic -Werror \
    -fsanitize=address,undefined \
    code/sanitizer/polynomial.c -o build/demo/polynomial-bounds
