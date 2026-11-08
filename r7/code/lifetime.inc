// Inside class Student
~Student() { std::cout << m_name << " leaves\n"; }

// In main():
{
    Student a("Alice", "20260001", 2026);
    Student b("Bob", "20260002", 2026);
} // b is destroyed first, then a
