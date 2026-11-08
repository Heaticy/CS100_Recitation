class Student {
private:
    std::string m_name;
    std::string m_id;
    int m_entranceYear;
public:
    bool setName(const std::string &name);
    bool graduated(int year) const;
};
