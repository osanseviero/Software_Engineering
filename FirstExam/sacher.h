class sacher: public Cake {
	friend class CakeFactoryConcrete;

	void batido(){
		std::cout << "Batiendo el chocolate." << std::endl;
	}

	void amasado(){
		std::cout << "Amasando el sacher." << std::endl;
	}

	void horneado(){
		std::cout << "Horneando el sacher...caliente!" << std::endl;
	}

	void decorado(){
		std::cout << "Decorándolo." << std::endl;
	}

	void empacado(){
		std::cout << "El sacher está empaquetado." << std::endl;
	}

	virtual ~sacher(){};

private:
	sacher(){
		state = "DF";
		name = "sacher";
	};

	
};