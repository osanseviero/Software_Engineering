#include <iostream>
#include <string>
#include "engine.h"
#include "wings.h"
#include "pilot.h"
#include "plane.h"
#include "builder.h"
#include "boeingBuilder.h"
#include "airbusBuilder.h"
#include "director.h"


int main() {
	Director* d = new Director();
	d->setBuilder(new BoeingBuilder());
	d->construct();

	Plane* p = d->getPlane();
	std::cout << p->getSerie() << std::endl;
	return 0;
}