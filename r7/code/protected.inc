class Base {
protected:
    int m_value{1};
};
class Derived : public Base {
public:
    int getValue() const { return m_value; }
};
// In main():
Derived d;
int value = d.getValue(); // OK: value is 1
// d.m_value = 2; // Error: protected
