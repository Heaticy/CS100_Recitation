void f(void) {
    int *p = malloc(100 * sizeof(int));
    if (p == NULL) return;
    p[0] = 42;
} /* p disappears; nobody kept the allocation */
