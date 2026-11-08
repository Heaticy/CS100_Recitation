struct Record { int m_year; }; // public
class Hidden { int m_year; };  // private

struct Open : Base {};   // public inheritance
class Closed : Base {};  // private inheritance
