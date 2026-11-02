std::string hello{"hello"};
std::string result = hello + " world" + "!";
result += " C++";

const char *cstr = "hello";
// std::string bad = cstr + " world"; // 错误：两侧都不是string
