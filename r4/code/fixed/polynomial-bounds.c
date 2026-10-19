/* HW2 P3 classroom variant: a fixed polynomial, no heap and no math.h. */
#include <stdio.h>

double evaluate(const double *coef, int count, double x) {
    double value = 0.0;
    for (int i = count - 1; i >= 0; --i) {
        value = value * x + coef[i];
    }
    return value;
}

int main(void) {
    const double coef[3] = {1.0, 2.0, 3.0};
    printf("%.3f\n", evaluate(coef, 3, 2.0));
    return 0;
}

/*
 * 课件位置：第35—36页：HW2数组越界的配套修复。
 * 用途：修复版：从count-1开始，处理至下标0，输出17.000。
 * 对照源码：code/sanitizer/polynomial.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
