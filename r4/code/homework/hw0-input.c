#include <stdio.h>

int main(void) {
    int x, y;
    if (scanf("%d %d", &x, &y) != 2) {
        return 1;
    }
    printf("%d\n", x + y);
    return 0;
}

/*
 * 课件位置：补充示例：HW0输入检查；当前56页课件未展示。
 * 用途：scanf返回值不是2时退出；小输入123 500输出623。
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
