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
 * 课件位置：第40—41页：数组循环、ASan与条件断点。
 * 用途：错误版：i<=6访问六元素数组的data[6]。
 * 对照源码：code/fixed/array_loop.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
