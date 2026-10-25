int *remember(void) {
    int old = 10;
    return &old;             /* dangling after return */
}
void later(int *p) {
    int fresh = 20;
    *p = 99;                 /* UB: not a valid way to reach fresh */
    printf("%d\n", fresh); /* no guaranteed output */
}
/* caller: int *p = remember(); later(p); */
