#include <iostream>
#include <vector>

int main() {
  int n;
  if (!(std::cin >> n) || n < 0)
    return 1;
  std::vector<int> values;
  for (int i = 0; i < n; ++i) {
    int x;
    if (!(std::cin >> x))
      return 1;
    values.push_back(x);
  }
  for (std::size_t i = values.size(); i > 0; --i) {
    if (i != values.size())
      std::cout << ' ';
    std::cout << values[i - 1];
  }
  std::cout << '\n';
}
