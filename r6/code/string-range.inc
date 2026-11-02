std::string text{"Hello C++"};
for (char c : text) {
  if (std::isupper(static_cast<unsigned char>(c)) != 0)
    std::cout << c;
}
