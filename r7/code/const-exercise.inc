std::string getID() const;
bool graduated(int year) const;
bool setName(const std::string &name);

// In main():
const Student s("Alice", "20260001", 2026);
s.graduated(2030); // A
// s.setName("Bob"); // B: compile error
