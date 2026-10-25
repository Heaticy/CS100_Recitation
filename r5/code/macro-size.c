#include <stdio.h>
#define PS(type) \
    printf("Size of " #type ": %zu\n", sizeof(type))
int main(void) {
    PS(long long);
    PS(int);
    return 0;
}
