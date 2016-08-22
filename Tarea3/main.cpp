#include <string>
#include <iostream>
#include "computerFactoryConcrete.h"

int main() {
	Computer* l = ComputerFactoryConcrete::GetInstance()->create("laptop");
	Computer* d = ComputerFactoryConcrete::GetInstance()->create("desktop");
	Computer* n = ComputerFactoryConcrete::GetInstance()->create("netbook");
	Computer* t = ComputerFactoryConcrete::GetInstance()->create("tablet");
	//Computer* m = ComputerFactoryConcrete::GetInstance()->create("mb");
	Computer* wrongType = ComputerFactoryConcrete::GetInstance()->create("burguer");
}