#include <stdio.h>

int main(void) {
    int data[6] = {0};
    for (int i = 0; i < 6; ++i) {
        data[i]++;
    }
    printf("%d\n", data[0]);
    return 0;
}

/*
 * 课件位置：第50页：数组边界示例的配套修复。
 * 用途：修复版：i<6，输出1。
 * 对照源码：code/behavior/bounds.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
