#include <stdio.h>
#define BAD_MUL(a, b) a * b
#define MUL(a, b) ((a) * (b))
int main(void) {
    printf("%d\n", 16 / BAD_MUL(1 + 1, 3 - 1));
    printf("%d\n", 16 / MUL(1 + 1, 3 - 1));
    return 0;
}
