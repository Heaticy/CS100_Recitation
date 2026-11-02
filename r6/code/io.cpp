#include <iostream>

int main() {
  int a;
  int b;
  if (!(std::cin >> a >> b)) {
    std::cerr << "expected two integers\n";
    return 1;
  }
  std::cout << a + b << '\n';
}
