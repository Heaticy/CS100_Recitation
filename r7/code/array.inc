// In main():
int *scores = new int[2]{90, 95};
std::cout << scores[0] << ' ' << scores[1] << '\n';
delete[] scores;
scores = nullptr;
