class Student {
public:
    explicit Student(int studentId)
        : m_id(studentId) {}

    int getId() const { return m_id; }

private:
    int m_id;
};
