#include <iostream>
#include <ctime>


class Handler2: public Base
{
public:
	void handle(int i) {
		if(rand() % 2) {
			std::cout << "Handler 2 got " << i << " and passed it" << std::endl;
			Base::handle(i);
		}
		else {
			std::cout << "Handler 2 got " << i << std::endl;
		}
	}
};