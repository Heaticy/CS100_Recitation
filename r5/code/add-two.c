#include <stdio.h>
int add_two(int *x) {
    int old = *x;
    *x += 2;
    return old;
}
int main(void) {
    int x = 0;
    int old = add_two(&x);
    printf("%d %d\n", old, x);
    return 0;
}
