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
		static ComputerFactoryConcrete* instance = new ComputerFactoryConcrete;	// Just runs one time because it is static
		return instance;
	}
	

private:
	ComputerFactoryConcrete(){};
	ComputerFactoryConcrete(const ComputerFactoryConcrete &old);
	const ComputerFactoryConcrete &operator=(const ComputerFactoryConcrete &old);
	
};