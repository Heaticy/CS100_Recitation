#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int *p = malloc(2 * sizeof(int));
    if (p == NULL) return EXIT_FAILURE;
    p[0] = 10;
    p[1] = 20;
    int *tmp = realloc(p, 4 * sizeof(int));
    if (tmp == NULL) {
        free(p);
        return EXIT_FAILURE;
    }
    p = tmp;
    p[2] = 30;
    p[3] = 40;
    printf("%d %d %d %d\n", p[0], p[1], p[2], p[3]);
    free(p);
    return 0;
}
