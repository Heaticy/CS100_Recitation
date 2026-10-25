/* p owns an allocated block */
p = realloc(p, 100 * sizeof *p);
if (p == NULL) {
    /* Where is the old block now? */
}
