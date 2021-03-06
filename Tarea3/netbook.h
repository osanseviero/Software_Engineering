class Netbook : public CloneComputer<Computer, Netbook> {
public:
	friend class ComputerFactoryConcrete;

	void assemble(){
		std::cout << "Assembling netbook parts." << std::endl;
	}

	void selectComponents(){
		std::cout << "Selecting netbook components." << std::endl;
	}

	void installSoftware(){
		std::cout << "Installing software of the netbook." << std::endl;
	}

	void package(){
		std::cout << "Ready to go!" << std::endl;
	}

	virtual ~Netbook(){};

private:
	Netbook(){};
};