#include <stdio.h>
#include <limits.h>

int main(void) {
    int value = INT_MAX - 2;
    value += 3;
    printf("%d\n", value);
    return 0;
}

/*
 * 课件位置：第47页：有符号溢出与无符号回绕。
 * 用途：错误版：INT_MAX减2后加3，有符号溢出属于UB。
 * 对照源码：code/behavior/unsigned-wrap.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
