int g = 7;
int z;
void f(void) {
    static int count;
    int local = 1;
    int *p = malloc(sizeof *p);
    /* ... */
    free(p);
}
