#include <stdio.h>

long long power(int x, int y) {
    long long result = 1;
    for (int i = 0; i < y; ++i) {
        result *= x;
    }
    return result;
}

int main(void) {
    printf("%lld\n", power(50000, 2));
    return 0;
}

/*
 * 课件位置：第39页：power修复验证。
 * 用途：修复版：乘积、返回值使用long long，输出2500000000；本例结果须可表示。
 * 对照源码：code/sanitizer/power.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
