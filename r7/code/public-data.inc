struct Student {
    int m_entranceYear;
};
// In main():
Student s{2026};
s.m_entranceYear = -1; // Compiles!
