#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
int main(void) {
    size_t n;
    if (scanf("%zu", &n) != 1 || n == 0 ||
        n > SIZE_MAX / sizeof(int)) {
        return EXIT_FAILURE;
    }
    int *a = malloc(n * sizeof *a);
    if (a == NULL) return EXIT_FAILURE;
    for (size_t i = 0; i < n; ++i) a[i] = 0;
    printf("%d\n", a[n - 1]);
    free(a);
    return 0;
}
