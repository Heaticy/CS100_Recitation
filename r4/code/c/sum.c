/* Classroom variant of the HW1 accumulation operation. */
#include <stdio.h>

void addValue(int sum, int x) {
    sum += x;
}

int main(void) {
    int sum = 3;
    addValue(sum, 5);
    printf("%d\n", sum);
    return 0;
}

/*
 * 课件位置：第43页、第45页：C按值传递，3+5。
 * 用途：错误版：仅修改形参副本，调用者仍输出3，预期为8。
 * 对照源码：code/fixed/sum.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
