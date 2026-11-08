bool graduated(int year) const {
    int years = year - m_entranceYear;
    return years >= 4;
}
