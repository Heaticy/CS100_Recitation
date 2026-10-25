#include <stdio.h>
void move(int *p) {
    p = p + 1;
}
int main(void) {
    int a[2] = {4, 6};
    int *p = &a[0];
    move(p);
    printf("%d %d\n", *a, *p);
    return 0;
}
