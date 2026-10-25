/* p owns an allocated block */
p = realloc(p, 100 * sizeof(int));
if (p == NULL) {
    /* Where is the old block now? */
}
