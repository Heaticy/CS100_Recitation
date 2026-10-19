#include <stdio.h>

int power(int x, int y) {
    int result = 1;
    for (int i = 0; i < y; ++i) {
        result *= x;
    }
    return result;
}

int main(void) {
    printf("%d\n", power(50000, 2));
    return 0;
}

/*
 * 课件位置：第38—39页：power乘法溢出、UBSan与GDB。
 * 用途：错误版：32位int不能表示50000的平方；不依赖UB后的输出。
 * 对照源码：code/fixed/power.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
