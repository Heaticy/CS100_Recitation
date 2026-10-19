#include <stdio.h>

int main(void) {
    int data[6] = {0};
    for (int i = 0; i <= 6; ++i) {
        data[i]++;
    }
    printf("%d\n", data[0]);
    return 0;
}

/*
 * 课件位置：第50页：数组越界与编译错误要分开。
 * 用途：错误版：data[6]越界；与第40页同一边界问题，用于行为分类。
 * 对照源码：code/behavior/bounds-fixed.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
