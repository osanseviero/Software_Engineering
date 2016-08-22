class Tablet : public CloneComputer<Computer, Tablet> {
public:
	friend class ComputerFactoryConcrete;

	void assemble(){
		std::cout << "Assembling tablet parts." << std::endl;
	}

	void selectComponents(){
		std::cout << "Selecting tablet components." << std::endl;
	}

	void installSoftware(){
		std::cout << "Installing software of the tablet." << std::endl;
	}

	void package(){
		std::cout << "Ready to go!" << std::endl;
	}

	virtual ~Tablet(){};

private:
	Tablet(){};
};