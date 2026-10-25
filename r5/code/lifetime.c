#include <stdio.h>
int global = 10;
void tick(void) {
    int local = 0;
    static int count = 0;
    ++local;
    ++count;
    ++global;
    printf("%d %d %d\n", local, count, global);
}
int main(void) {
    tick();
    tick();
    return 0;
}
