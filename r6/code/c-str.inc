void legacy_print(const char *text);

std::string s{"hello"};
legacy_print(s.c_str());
// 不修改返回的字符数组，也不要把指针保存到s失效之后。
