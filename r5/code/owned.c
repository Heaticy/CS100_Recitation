#include <stdio.h>
#include <stdlib.h>
/* Caller owns the returned block; NULL means failure. */
int *make_number(int value) {
    int *p = malloc(sizeof(int));
    if (p != NULL) *p = value;
    return p;
}
int main(void) {
    int *p = make_number(42);
    if (p == NULL) return EXIT_FAILURE;
    printf("%d\n", *p);
    free(p);
    return 0;
}
