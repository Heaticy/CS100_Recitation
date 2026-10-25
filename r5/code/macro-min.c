#include <stdio.h>
#define MIN(a, b) ((a) < (b) ? (a) : (b))
static inline int min_int(int a, int b) {
    return a < b ? a : b;
}
int main(void) {
    int i = 1;
    int result = MIN(i++, 5);
    printf("%d %d\n", result, i);
    printf("%d\n", min_int(3, 5));
    return 0;
}
