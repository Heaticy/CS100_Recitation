/* Classroom debugging variant of HW1 P3; not the original starter solution. */
#include <stdio.h>

int updateMaximum(int maximum, int value) {
    int result = maximum;
    if (value > result) {
        result = value;
    }
    return result;
}

int main(void) {
    int sum = 0;
    int maximum = 0;
    int hasValue = 0;
    int x = 0;
    while (scanf("%d", &x) == 1 && x != 0) {
        sum += x;
        if (!hasValue) {
            maximum = x;
        } else {
            maximum = updateMaximum(maximum, sum);
        }
        hasValue = 1;
    }
    if (hasValue) {
        printf("%d %d\n", sum, maximum);
    }
    return 0;
}

/*
 * 课件位置：第4—8页、第18—30页：HW1求和与最大值、连续GDB演示。
 * 用途：调试用错误版：辅助函数收到累计和sum，而非当前输入x。
 * 对照源码：code/fixed/hw1-p3.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
