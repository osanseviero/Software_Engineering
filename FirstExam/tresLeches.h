class tresLeches: public Cake {
	friend class CakeFactoryConcrete;

	void batido(){
		std::cout << "Batiendo mucha leche" << std::endl;
	}

	void amasado(){
		std::cout << "Amasando el tres leches." << std::endl;
	}

	void horneado(){
		std::cout << "Horneando el tres leches." << std::endl;
	}

	void decorado(){
		std::cout << "Haciendo que se vea bonito." << std::endl;
	}

	void empacado(){
		std::cout << "Empaquetando el tres leches." << std::endl;
	}

	virtual ~tresLeches(){};

private:
	tresLeches(){
		state = "Aguascalientes";
		name = "tresLeches";
	};
};