/* HW2 P3 classroom polynomial, evaluated at x = 3/2. */
#include <stdio.h>

int main(void) {
    const int numerator = 3;
    const int denominator = 2;
    double x = numerator / denominator;
    double value = 1.0 + 2.0 * x + 3.0 * x * x;
    printf("%.3f\n", value);
    return 0;
}

/*
 * 课件位置：第46页整数除法说明的扩展程序；当前课件未展示完整程序。
 * 用途：逻辑错误版：3/2先做整数除法，多项式输出6.000。
 * 对照源码：code/fixed/poly-division.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
