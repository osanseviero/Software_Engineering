#include <iostream>
#include <ctime>
#include "base.cpp"

class Handler1: public Base
{
public:
	void handle(int i) {
		if(rand() % 2) {
			std::cout << "Handler 1 got " << i << "and passed it" << std::endl;
			Base::handle(i);
		}
		else {
			std::cout << "Handler 1 got " << i << std::endl;
		}
	}
};