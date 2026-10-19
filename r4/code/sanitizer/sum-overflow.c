/* HW1 P3 sum-accumulation excerpt, deliberately using a narrow type. */
#include <stdio.h>

int main(void) {
    int sum = 0;
    int x = 0;
    while (scanf("%d", &x) == 1 && x != 0) {
        sum += x;
    }
    printf("%d\n", sum);
    return 0;
}

/*
 * 课件位置：补充示例：HW1累加溢出；当前56页课件未展示。
 * 用途：错误版：32位int累计INT_MAX和1，用UBSan观察诊断。
 * 对照源码：code/fixed/sum-overflow.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
