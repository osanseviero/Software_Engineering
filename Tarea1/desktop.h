class Desktop : public Computer {
public:
	void assemble(){
		std::cout << "Assembling desktop parts." << std::endl;
	}

	void selectComponents(){
		std::cout << "Selecting desktop components." << std::endl;
	}

	void installSoftware(){
		std::cout << "Installing software of the desktop." << std::endl;
	}

	void package(){
		std::cout << "Ready to go!" << std::endl;
	}

	virtual ~Desktop(){};
};