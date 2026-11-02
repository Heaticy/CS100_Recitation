std::vector<int> v;
v.reserve(100);
std::cout << v.size() << ' ' << v.capacity() << '\n';
// size仍为0；capacity至少为100。
// v[0] = 42; // 未定义行为：元素尚不存在
