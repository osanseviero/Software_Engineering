class imposible: public Cake {
	friend class CakeFactoryConcrete;

	void batido(){
		std::cout << "Batiendo lo imposible." << std::endl;
	}

	void amasado(){
		std::cout << "Esto es imposible." << std::endl;
	}

	void horneado(){
		std::cout << "Horneando imposiblemente." << std::endl;
	}

	void decorado(){
		std::cout << "Qué decorado más imposible." << std::endl;
	}

	void empacado(){
		std::cout << "Imposiblemente...fue empaquetado." << std::endl;
	}

	virtual ~imposible(){};

private:
	imposible(){
		state = "DF";
		name = "imposible";
	};
	
};