// Inside class Student
std::string getName() const {
    return m_name;
}

// In main():
const Student s("Alice", "20260001", 2026);
std::cout << s.getName() << '\n'; // OK
