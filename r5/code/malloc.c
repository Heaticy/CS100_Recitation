#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int *p = malloc(sizeof(int));
    if (p == NULL) {
        return EXIT_FAILURE;
    }
    *p = 42;
    printf("%d\n", *p);
    free(p);
    return 0;
}
