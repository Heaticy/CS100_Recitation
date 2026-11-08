// Student has the three-argument constructor.
Student a("Alice", "20260001", 2026); // OK
// Student b; // Error: no default constructor

// A separate design with a valid empty state:
class StudentDraft {
    std::string m_name{};
    int m_entranceYear{0}; // 0 means "not entered"
public:
    StudentDraft() = default;
};
