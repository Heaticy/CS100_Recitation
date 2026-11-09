// Inside class Student
bool setName(const std::string &name) {
    if (name.empty()) {
        return false;
    }
    m_name = name;
    return true;
}
