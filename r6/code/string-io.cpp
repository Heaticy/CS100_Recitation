#include <iostream>
#include <string>

int main() {
  std::string name;
  if (!std::getline(std::cin, name))
    return 1;
  std::cout << "Hello, " << name << "!\n";
}
