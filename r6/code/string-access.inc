std::string s{"abc"};
char first = s[0];
char second = s.at(1);
s[0] = 'A';
// s[10] = 'x';   // 未定义行为
// s.at(10) = 'x'; // 抛出std::out_of_range
