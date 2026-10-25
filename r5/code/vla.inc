/* Suppose n > 0; headers omitted. */
void show_first(size_t n) {
    int a[n];       /* VLA: size known at run time */
    a[0] = 42;
    printf("%d\n", a[0]);
}                   /* a stops existing here */
/* Reading example only: VLAs are banned in homework. */
