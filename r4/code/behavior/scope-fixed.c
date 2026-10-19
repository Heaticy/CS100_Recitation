#include <stdio.h>

void show(int number) {
    printf("%d\n", number);
}

int main(void) {
    int number = 17;
    show(number);
    return 0;
}

/*
 * 课件位置：第50页：作用域示例的配套修复。
 * 用途：修复版：通过函数形参传递number，输出17。
 * 对照源码：code/behavior/scope.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
