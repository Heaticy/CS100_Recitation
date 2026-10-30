#include <cctype>
#include <iostream>
#include <string>

std::string rstrip(std::string text) {
  while (!text.empty() &&
         std::isspace(static_cast<unsigned char>(text.back())) != 0)
    text.pop_back();
  return text;
}

int main() {
  std::string line;
  if (!std::getline(std::cin, line))
    return 1;
  std::cout << '[' << rstrip(line) << "]\n";
}
