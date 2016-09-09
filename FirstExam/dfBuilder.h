class dfBuilder: public Builder {
public:
	void orderCake(std::string t) {
		if(t == "sacher" || t == "imposible"){
			addCakeType(t);
		}
		else {
			std::cout << "This cake is not from this state" << std::endl;
			return;
		}
	}

	void addCakeType(std::string t) {
		addCake(CakeFactoryConcrete::GetInstance()->create(t));
	}
};