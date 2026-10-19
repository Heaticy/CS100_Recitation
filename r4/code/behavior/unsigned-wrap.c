#include <stdio.h>
#include <limits.h>

int main(void) {
    unsigned int value = UINT_MAX - 2;
    value += 3;
    printf("%u\n", value);
    return 0;
}

/*
 * 课件位置：第47页：有符号溢出与无符号回绕。
 * 用途：有定义行为：无符号运算按类型取值个数取模，输出0。
 * 对照源码：code/behavior/signed-overflow.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
