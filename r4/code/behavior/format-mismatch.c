#include <stdio.h>

int main(void) {
    double value = 9.0;
    printf("%d\n", value / 4);
    return 0;
}

/*
 * 课件位置：第48页：printf格式必须匹配实参类型。
 * 用途：错误版：%d与double不匹配；仅检查编译诊断，不运行预测输出。
 * 对照源码：code/behavior/format-fixed.c
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
