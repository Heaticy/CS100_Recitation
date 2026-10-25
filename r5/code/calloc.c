#include <stdio.h>
#include <stdlib.h>
int main(void) {
    size_t n = 5;
    int *a = calloc(n, sizeof *a);
    if (a == NULL) return EXIT_FAILURE;
    printf("%d %d\n", a[0], a[4]);
    free(a);
    return 0;
}
