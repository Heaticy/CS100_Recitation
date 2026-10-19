#include <stdio.h>

void show(void) {
    printf("%d\n", number);
}

int main(void) {
    int number = 17;
    show();
    return 0;
}

/*
 * 课件位置：第50页：数组越界与编译错误要分开。
 * 用途：预期编译失败：show看不到main的局部变量number。
 * 对照源码：code/behavior/scope-fixed.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
