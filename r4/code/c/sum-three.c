/* Classroom variant of the HW1 accumulation operation. */
#include <stdio.h>

void addValue(int sum, int x) {
    sum += x;
}

int main(void) {
    int sum = 3;
    addValue(sum, 3);
    printf("%d\n", sum);
    return 0;
}

/*
 * 课件位置：第44页：实测GDB会话使用的3+3变体。
 * 用途：错误版：形参变为6，返回调用者后原变量仍为3。
 * 对照源码：code/fixed/sum-three.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
