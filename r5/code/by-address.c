#include <stdio.h>
void set_number(int *p) {
    *p = 42;
}
int main(void) {
    int n = 10;
    set_number(&n);
    printf("%d\n", n);
    return 0;
}
