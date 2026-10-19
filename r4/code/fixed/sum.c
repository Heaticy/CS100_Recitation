/* Classroom variant of the HW1 accumulation operation. */
#include <stdio.h>

void addValue(int *sum, int x) {
    *sum += x;
}

int main(void) {
    int sum = 3;
    addValue(&sum, 5);
    printf("%d\n", sum);
    return 0;
}

/*
 * 课件位置：第43页、第45页：按值传递示例的配套修复，3+5。
 * 用途：修复版：传入&sum，通过*sum修改调用者，输出8。
 * 对照源码：code/c/sum.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
