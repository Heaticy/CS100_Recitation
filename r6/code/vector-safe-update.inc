const std::size_t original_size = values.size();
for (std::size_t i = 0; i != original_size; ++i) {
  int x = values[i];
  if (x % 2 == 0)
    values.push_back(x + 1);
}
