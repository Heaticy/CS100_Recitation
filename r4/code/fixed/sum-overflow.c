/* HW1 P3 sum-accumulation excerpt, using a wider accumulator for this input. */
#include <stdio.h>

int main(void) {
    long long sum = 0;
    int x = 0;
    while (scanf("%d", &x) == 1 && x != 0) {
        sum += x;
    }
    printf("%lld\n", sum);
    return 0;
}

/*
 * 课件位置：补充示例：独立累加溢出的修复；当前课件未展示。
 * 用途：修复版：long long累计，边界输入输出2147483648；中间结果须可表示。
 * 对照源码：code/sanitizer/sum-overflow.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
