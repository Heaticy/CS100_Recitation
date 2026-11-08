bool graduated(int year) const {
    return year - this->m_entranceYear >= 4;
}

// In main():
a.graduated(2030); // this == &a
b.graduated(2030); // this == &b
