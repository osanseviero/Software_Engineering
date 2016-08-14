#include <string>
#include <iostream>
#include "computerFactory.h"

int main() {
	Computer* d = ComputerFactory::create("desktop");
	Computer* l = ComputerFactory::create("laptop");
	Computer* n = ComputerFactory::create("netbook");
	Computer* t = ComputerFactory::create("tablet");
}