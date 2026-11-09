// Inside class Student: missing const!
std::string getName() { return m_name; }

// In main():
const Student s("Alice", "20260001", 2026);
std::cout << s.getName(); // Compile error
