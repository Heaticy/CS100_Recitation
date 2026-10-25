int *p = malloc(sizeof *p);
if (p == NULL) return EXIT_FAILURE;
*p = 42;
free(p);
p = NULL;
