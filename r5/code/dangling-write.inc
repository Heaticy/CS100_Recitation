struct Point { int x; int y; };
struct Point *create_point(int x, int y) {
    struct Point point = {x, y};
    return &point;           /* wrong: local object */
}
int main(void) {
    struct Point *p = create_point(10, 15);
    struct Point fresh = {20, 30};
    p->x = 99;               /* UB: dangling pointer */
    printf("%d\n", fresh.x); /* no guaranteed output */
    return 0;
}
