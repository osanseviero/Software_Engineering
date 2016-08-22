class MacBook : public CloneComputer<Laptop, MacBook> {
public:
	friend class ComputerFactoryConcrete;

	void addCage(){
		std::cout << "Added the nice cage" << std::endl;
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
		std::cout << "Your mac is ready." << std::endl;
	}

	virtual ~MacBook(){};

private:
	MacBook(){};
};