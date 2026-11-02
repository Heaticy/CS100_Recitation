for (std::size_t i = 0; i != v.size(); ++i)
  std::cout << v[i] << '\n';

// v[v.size()] = 42;   // 未定义行为
// v.at(v.size()) = 42; // 抛出std::out_of_range
