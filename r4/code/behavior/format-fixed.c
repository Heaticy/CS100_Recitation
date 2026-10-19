#include <stdio.h>

int main(void) {
    double value = 9.0;
    printf("%.2f\n", value / 4);
    return 0;
}

/*
 * 课件位置：第48页：printf格式修复。
 * 用途：修复版：%.2f匹配double，输出2.25。
 * 对照源码：code/behavior/format-mismatch.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
