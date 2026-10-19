/* Classroom fix; inputs and running totals must fit in long long. */
#include <stdio.h>

long long updateMaximum(long long maximum, long long value) {
    long long result = maximum;
    if (value > result) {
        result = value;
    }
    return result;
}

int main(void) {
    long long sum = 0;
    long long maximum = 0;
    int hasValue = 0;
    long long x = 0;
    while (scanf("%lld", &x) == 1 && x != 0) {
        sum += x;
        if (!hasValue) {
            maximum = x;
        } else {
            maximum = updateMaximum(maximum, x);
        }
        hasValue = 1;
    }
    if (hasValue) {
        printf("%lld %lld\n", sum, maximum);
    }
    return 0;
}

/*
 * 课件位置：补充示例：HW1完整程序的宽类型修复；当前课件未展示。
 * 用途：同时修正实参和读写类型；输入及中间总和均须可由long long表示。
 * 对照源码：code/homework/hw1-p3.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
