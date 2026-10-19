#include <stdio.h>

int main(void) {
    int score = 90;
    printf("%d\n", score);
    return 0;
}

/*
 * 课件位置：补充示例：生命周期修复；当前课件未展示。
 * 用途：修复版：本例无需堆分配，使用局部变量，输出90。
 * 对照源码：code/sanitizer/use-after-free.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
