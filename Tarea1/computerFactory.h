#include "computer.h"
#include "laptop.h"
#include "desktop.h"
#include "netbook.h"
#include "tablet.h"

class ComputerFactory {
public:
	static void process(Computer* c) {
		c->selectComponents();
		c->assemble();
		c->installSoftware();
		c->package();
	}

	static Computer* create(std::string type) {
		if(type == "laptop") {
			Laptop* l =  new Laptop;
			process(l);
			return l;
		}
		else if(type == "desktop") {
			Desktop* l =  new Desktop;
			process(l);
			return l;
		}
		else if(type == "netbook") {
			Netbook* l =  new Netbook;
			process(l);
			return l;
		}
		else if(type == "tablet") {
			Tablet* l =  new Tablet;
			process(l);
			return l;
		}
		else {
			std::cout << "Type not recognized." << std::endl;
			return NULL;
		}	
	}
};