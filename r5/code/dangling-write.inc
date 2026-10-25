struct Point { int x; int y; };
struct Point *create_point(int x, int y) {
    struct Point point = {x, y};
    return &point;           /* wrong: local object */
}
void later(struct Point *p) {
    struct Point fresh = {20, 30};
    p->x = 99;               /* UB: dangling pointer */
    printf("%d\n", fresh.x); /* no guaranteed output */
}
/* caller: struct Point *p = create_point(10, 15); */
/*         later(p); */
