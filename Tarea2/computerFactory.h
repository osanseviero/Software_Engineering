#include "computer.h"
#include "laptop.h"
#include "desktop.h"
#include "netbook.h"
#include "tablet.h"


class ComputerFactory {
public:
	virtual Computer* createComputer(std::string type) = 0;

	Computer* create(std::string type) {
		Computer* c = createComputer(type);
		if(c != NULL) {
			c->selectComponents();
			c->assemble();
			c->installSoftware();
			c->package();
			return c;
		}
		std::cout << type <<  " computer type not recognized" << std::endl;
		return NULL;
	}
};

