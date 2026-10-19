#include <stdio.h>

int main(void) {
    char value = -1;
    printf("%d\n", value);
    return 0;
}

/*
 * 课件位置：第49页：char的符号属性由实现定义。
 * 用途：使用-fsigned-char或-funsigned-char；8位char、32位int环境分别输出-1和255。
 * 页码按PDF页脚1/56至56/56；完整索引见code/README.md。
 */
