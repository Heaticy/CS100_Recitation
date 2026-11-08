// Inside class Student
Student(const std::string &name,
        const std::string &id, int year)
    : m_name(name), m_id(id), m_entranceYear(year) {
    if (name.empty() || id.empty()
        || year < 1900 || year > 2100) {
        throw std::invalid_argument("invalid student");
    }
}
