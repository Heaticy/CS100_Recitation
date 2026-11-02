std::vector<int> a{1, 2, 3};
std::vector<int> b = a;
b[0] = 99;
std::cout << a[0] << ' ' << b[0] << '\n'; // 1 99
