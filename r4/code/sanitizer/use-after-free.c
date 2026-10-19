/* Independent C lifetime example; not a homework implementation. */
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *score = malloc(sizeof *score);
    if (score == NULL) {
        return 1;
    }
    *score = 90;
    free(score);
    printf("%d\n", *score);
    return 0;
}

/*
 * 课件位置：补充示例：独立C内存生命周期；当前56页课件未展示。
 * 用途：错误版：free后解引用，ASan报告heap-use-after-free；不属于作业实现。
 * 对照源码：code/fixed/use-after-free.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
