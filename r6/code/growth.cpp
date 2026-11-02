#include <iostream>
#include <vector>

int main() {
  std::vector<int> values;
  for (int i = 0; i != 17; ++i) {
    values.push_back(i);
    std::cout << values.size() << ' ' << values.capacity() << '\n';
  }
}
