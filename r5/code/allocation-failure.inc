int *a = malloc(n * sizeof *a);
if (a == NULL) {
    return; /* handle failure */
}
/* use a, then free(a) */
