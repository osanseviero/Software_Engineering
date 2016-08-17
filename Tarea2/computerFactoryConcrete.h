#include "computerFactory.h"

class ComputerFactoryConcrete: public ComputerFactory {
public:

	Computer* createComputer(std::string type) {
		if(type == "laptop") {
			return new Laptop;
		}
		else if(type == "desktop") {
			return new Desktop;
		}
		else if(type == "netbook") {
			return new Netbook;
		}
		else if(type == "tablet") {
			return new Tablet;
		}
		return NULL;
	}

	static ComputerFactoryConcrete* GetInstance(){
		//if (!isInstance) {
			// std::cout << "Hi"; // Uncomment to check that it only creates the instance once
			return new ComputerFactoryConcrete();
		//}
		//return isInstance;
	}

private:
	static ComputerFactoryConcrete* isInstance;
	ComputerFactoryConcrete(){ isInstance=NULL;};
};

