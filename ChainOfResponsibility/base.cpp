#include <iostream>
#include <vector>
#include <ctime>

class Base
{
public:
	Base *next;

	Base() {
		next = 0;
	}

	void setNext(Base *n) {
		next = n;
	}

	void add(Base *n) {
		if(next == NULL) {
			next = n;
		}
		else {
			next->add(n);
		}
	}

	virtual void handle(int i) {
		next->handle(i);
	}
};