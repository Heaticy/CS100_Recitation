int *p = malloc(sizeof(int));
if (p == NULL) return EXIT_FAILURE;
*p = 42;
free(p);
p = NULL;
