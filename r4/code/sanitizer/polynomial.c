/* HW2 P3 classroom variant: a fixed polynomial, no heap and no math.h. */
#include <stdio.h>

double evaluate(const double *coef, int count, double x) {
    double value = 0.0;
    for (int i = count; i >= 0; --i) {
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
 * 课件位置：第33—37页：HW2 P3、ASan数组越界。
 * 用途：错误版：i=count使首次读取访问coef[count]。
 * 对照源码：code/fixed/polynomial-bounds.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
