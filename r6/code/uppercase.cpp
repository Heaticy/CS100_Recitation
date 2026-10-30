#include <cctype>
#include <iostream>
#include <string>
#include <vector>

int main() {
  std::vector<std::string> words{"Hello", "World", "C++"};
  for (const std::string &word : words) {
    for (char c : word) {
      if (std::isupper(static_cast<unsigned char>(c)) != 0)
        std::cout << c;
    }
    std::cout << '\n';
  }
}
