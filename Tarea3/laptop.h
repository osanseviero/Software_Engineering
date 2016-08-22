class Laptop : public CloneComputer<Computer, Laptop> {
public:
	friend class ComputerFactoryConcrete;

	void addCage(){
		std::cout << "Added the cage" << std::endl;
	}

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
		addCage();
		std::cout << "Ready to go!" << std::endl;
	}	

	virtual ~Laptop(){};

private:
	Laptop(){};
};