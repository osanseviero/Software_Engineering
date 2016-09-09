#include "cake.h"
#include "tresLeches.h"
#include "sacher.h"
#include "imposible.h"


class CakeFactory {
public:
	virtual Cake* createCake(std::string type) = 0;

	Cake* create(std::string type) {
		Cake* c = createCake(type);
		if(c != NULL) {
			c->batido();
			c->amasado();
			c->horneado();
			c->decorado();
			c->empacado();
			return c;
		}
		std::cout << type <<  " cake was not recognized" << std::endl;
		return NULL;
	}
};
