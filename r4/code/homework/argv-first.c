/* HW2 P4 debugging excerpt: inspect arguments, not a complete descriptor. */
#include <stdio.h>

int main(int argc, char *argv[]) {
    for (int i = 1; i < argc; ++i) {
        printf("%c\n", argv[i][0]);
    }
    return 0;
}

/*
 * 课件位置：补充示例：HW2 argc/argv；当前56页课件未展示。
 * 用途：仅打印每个参数的首字符，供argv-session.gdb观察，不是完整作业答案。
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
