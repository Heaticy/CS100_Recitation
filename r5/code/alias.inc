int *p = malloc(sizeof(int));
if (p == NULL) return EXIT_FAILURE;
*p = 42;
int *q = p;
free(p);
p = NULL;
/* printf("%d\n", *q); wrong */
/* free(q);            wrong */
q = NULL;
