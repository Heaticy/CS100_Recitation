for (int x : values) {
  if (x % 2 == 0)
    values.push_back(x + 1); // 可能使遍历迭代器失效
}
