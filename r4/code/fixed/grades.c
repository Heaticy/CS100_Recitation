#include <stdio.h>

int main(void) {
    int n = 0;
    int sum = 0;
    int count = 0;
    if (scanf("%d", &n) != 1 || n < 0 || n > 10000) {
        return 1;
    }
    for (int i = 0; i < n; ++i) {
        int score = 0;
        if (scanf("%d", &score) != 1 || score < 0 || score > 100) {
            return 1;
        }
        if (score >= 60) {
            sum += score;
        }
        if (score >= 60) {
            ++count;
        }
    }
    if (count == 0) {
        printf("No passing scores\n");
    } else {
        printf("%g\n", (double)sum / count);
    }
    return 0;
}

/*
 * 课件位置：第1—2页：成绩统计反例的配套修复。
 * 用途：修复版：求和与计数统一使用score >= 60。
 * 对照源码：code/gdb/grades.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
