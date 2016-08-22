class Computer {
public:
	
	virtual void selectComponents() = 0;
	virtual void assemble() = 0;
	virtual void installSoftware() = 0;
	virtual void package() = 0;
	
	virtual ~Computer() {};
};