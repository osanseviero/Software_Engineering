class Director {
public:
	Director() {};

	Builder* builder;

	void setBuilder(Builder* b) {
		this->builder = b;
	}

	void orderCake(std::string cakeType) {
		this->builder->orderCake(cakeType);
	}

	Aggregate<Cake*> getCakes() {
		return builder->getCakes();
	}

	int getCakesCount() {
		return this->builder->p.size;
	}

	void printCakes() {
		Iterator<Cake*>* i;
		for(i = this->builder->p.getIterator(); i->hasNext(); )
			{
				std::cout << (i->next())->name;
		}

	}

	int searchCake(std::string name) {
		Iterator<Cake*>* i;
		int c = 1;
		for(i = this->builder->p.getIterator(); i->hasNext(); )
			{
				if((i->next())->name == name ) {
					return c;
				}
				c++;
		}
		std::cout << "Cake not found" << std::endl;
	}

	Cake* getCake(std::string name) {
		Iterator<Cake*>* i;
		for(i = this->builder->p.getIterator(); i->hasNext(); )
			{
				if((i->next())->name == name ) {
					return i->next();
				}
		}
		std::cout << "Cake not found" << std::endl;
		return NULL;
	}

private:
	Builder* b;

};