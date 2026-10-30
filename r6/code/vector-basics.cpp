#include <iostream>
#include <vector>

int main() {
  std::vector<int> values{2, 3, 5, 7};
  values.push_back(11);
  values.front() = 1;
  ++values.back();
  std::cout << "size=" << values.size() << " front=" << values.front()
            << " back=" << values.back() << '\n';
  for (int value : values)
    std::cout << value << ' ';
  std::cout << '\n';
  values.pop_back();
  std::cout << "size=" << values.size() << " back=" << values.back() << '\n';
}
