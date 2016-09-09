class aguascalientesBuilder: public Builder {
public:
	void orderCake(std::string t) {
		if(t == "tresLeches"){
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