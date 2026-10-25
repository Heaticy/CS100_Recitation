int *make_number(void) {
    int x = 42;
    return &x;       /* wrong: x will stop existing */
}
/* caller: int *p = make_number(); */
/*         printf("%d\n", *p);    */
