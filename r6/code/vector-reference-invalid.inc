std::vector<int> values{1, 2, 3};
int &last = values.back();
values.push_back(4); // 若重新分配，last失效
std::cout << last;   // 若last已失效：未定义行为
