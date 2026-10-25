int *p = malloc(2 * sizeof *p);
int *q = p;
p[0] = 10;
p[2] = 20;
free(p);
p = NULL;
printf("%d\n", q[0]);
free(q);
