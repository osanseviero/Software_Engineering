class Builder {
public:
	Aggregate<Cake*> getCakes() {
		return this->p;
	}

	virtual void orderCake(std::string t) = 0;
	
	virtual void addCakeType(std::string t) = 0;

	void addCake(Cake* c) {
		p.push_back(c);
	}

	Aggregate<Cake*> p;
};