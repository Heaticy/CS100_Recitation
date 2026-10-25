#include <stdio.h>
#include <stdlib.h>
struct Point { int x; int y; };
struct Point *create_point(int x, int y) {
    struct Point *point;
    point = malloc(sizeof *point);
    if (point == NULL) return NULL;
    point->x = x;
    point->y = y;
    return point;
}
int main(void) {
    struct Point *p = create_point(10, 15);
    if (p == NULL) return EXIT_FAILURE;
    struct Point new_point = {20, 30};
    p->x = 99;
    printf("%d %d\n", p->x, p->y);
    printf("%d %d\n",
           new_point.x, new_point.y);
    free(p);
    return 0;
}
