Student *group = new Student[2]{
    Student("Alice", "20260001", 2026),
    Student("Bob", "20260002", 2026)
};
delete[] group;
group = nullptr;
