int *a = malloc(n * sizeof(int));
if (a == NULL) {
    return; /* handle failure */
}
/* use a, then free(a) */
