// In main():
Student *p = new Student("Alice", "20260001", 2026);
std::cout << p->getName() << '\n';
delete p;
p = nullptr;
