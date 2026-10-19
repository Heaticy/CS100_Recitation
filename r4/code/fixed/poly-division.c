/* HW2 P3 classroom polynomial, evaluated at x = (double)3/2. */
#include <stdio.h>

int main(void) {
    const int numerator = 3;
    const int denominator = 2;
    double x = (double)numerator / denominator;
    double value = 1.0 + 2.0 * x + 3.0 * x * x;
    printf("%.3f\n", value);
    return 0;
}

/*
 * 课件位置：第46页整数除法说明的扩展修复；当前课件未展示完整程序。
 * 用途：修复版：除法之前转换为double，输出10.750。
 * 对照源码：code/c/poly-division.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
