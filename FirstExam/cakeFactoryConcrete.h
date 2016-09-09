#include "cakeFactory.h"

class CakeFactoryConcrete: public CakeFactory {
public:

	Cake* createCake(std::string type) {
		if(type == "tresLeches") {
			tresLeches* t = new tresLeches; 
			t->ingredients.push_back(new Leche);
			t->ingredients.push_back(new Huevo);
			t->ingredients.push_back(new Mantequilla);
			return t;
		}
		else if(type == "sacher") {
			sacher* s = new sacher; 
			s->ingredients.push_back(new Chocolate);
			return s;
		}
		else if(type == "imposible") {
			imposible* i = new imposible; 
			i->ingredients.push_back(new Merengue);
			i->ingredients.push_back(new Fruta);
			return i;
		}
		return NULL;
	}

	static CakeFactoryConcrete* GetInstance(){
		static CakeFactoryConcrete* instance = new CakeFactoryConcrete;	// Just runs one time because it is static
		return instance;
	}
	

private:
	CakeFactoryConcrete(){};
	CakeFactoryConcrete(const CakeFactoryConcrete &old);
	const CakeFactoryConcrete &operator=(const CakeFactoryConcrete &old);
	
};