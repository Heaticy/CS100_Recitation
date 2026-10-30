#include <iostream>
#include <string>

int main() {
  std::string greeting{"Hello"};
  std::string copy = greeting;
  greeting += ", C++!";
  std::cout << greeting << '\n';
  std::cout << copy << '\n';
  std::cout << "size=" << greeting.size() << '\n';
}
