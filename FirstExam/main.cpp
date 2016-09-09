#include <iostream>
#include <vector>
#include "ingredient.h"
#include "aguascalientesIngredients.h"
#include "dfIngredients.h"
#include "aggregate.h"
#include "iterator.h"
#include "cakeFactoryConcrete.h"
#include "builder.h"
#include "aguascalientesBuilder.h"
#include "dfBuilder.h"
#include "director.h"




int main() {
	Director* d = new Director();
	d->setBuilder(new dfBuilder());
	d->orderCake("sacher");
	d->orderCake("tresLeches");
	d->orderCake("imposible");
	d->orderCake("imposible");
	d->orderCake("imposible");
	d->printCakes();
	std::cout << "Tenemos " << d->getCakesCount() << " pasteles" << std::endl;
	std::cout << "Hay un imposible en la posicion " << d->searchCake("imposible") << std::endl;
	d->searchCake("tresLeches");
	return 0;
}