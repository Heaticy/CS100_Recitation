/* Classroom accumulation fix: add 3 through a pointer. */
#include <stdio.h>

void addValue(int *sum, int x) {
    *sum += x;
}

int main(void) {
    int sum = 3;
    addValue(&sum, 3);
    printf("%d\n", sum);
    return 0;
}

/*
 * 课件位置：第44页：指针更新修复，3+3。
 * 用途：修复版：通过指针修改原变量，输出6；与3+5示例分开。
 * 对照源码：code/c/sum-three.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
