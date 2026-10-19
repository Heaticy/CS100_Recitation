/* HW2 P3 classroom variant with fixed data. */
#include <stdio.h>

/* coef[0] is the constant term. */
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
 * 课件位置：第53页：练习解答，不能漏掉常数项。
 * 用途：修复版：循环包含下标0，输出17.000。
 * 对照源码：code/exercise/polynomial.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
