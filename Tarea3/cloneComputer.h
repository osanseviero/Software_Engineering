template <class Base, class SubClass>
class CloneComputer : public Computer {
public:
	virtual Base* clone() {
		return new SubClass(static_cast<SubClass&>(*this));
	}
};