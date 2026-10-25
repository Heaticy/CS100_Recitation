int global;
void f(void) {
    int local = 0;
    int *p = malloc(3 * sizeof *p);
    if (p == NULL) return;
    /* free(&local);  wrong */
    /* free(&global); wrong */
    /* free(p + 1);   wrong */
    free(p);         /* correct */
    /* free(p);       wrong: already freed */
}
