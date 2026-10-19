mkdir -p build/demo
gcc -std=c17 -g -O0 -Wall -Wextra -Wpedantic -Werror \
    -fsanitize=address,undefined \
    code/c/poly-division.c -o build/demo/poly-division-san
./build/demo/poly-division-san

gcc -std=c17 -g -O0 -Wall -Wextra -Wpedantic -Werror \
    -fsanitize=address,undefined \
    code/fixed/poly-division.c -o build/demo/poly-division-san-fixed
./build/demo/poly-division-san-fixed
