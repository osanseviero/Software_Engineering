class Laptop : public Computer {
public:
	friend class ComputerFactoryConcrete;

	void assemble(){
		std::cout << "Assembling laptop parts." << std::endl;
	}

	void selectComponents(){
		std::cout << "Selecting laptop components." << std::endl;
	}

	void installSoftware(){
		std::cout << "Installing software of the laptop." << std::endl;
	}

	void package(){
		std::cout << "Ready to go!" << std::endl;
	}

	virtual ~Laptop(){};

private:
	Laptop(){};
};