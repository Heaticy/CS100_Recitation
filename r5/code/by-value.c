#include <stdio.h>
void set_number(int x) {
    x = 42;
    printf("inside: %d\n", x);
}
int main(void) {
    int n = 10;
    set_number(n);
    printf("outside: %d\n", n);
    return 0;
}
