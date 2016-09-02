class BoeingBuilder: public Builder {
public:
	void getWings() {
		std::cout << "hi" << std::endl;
		Wings* w = new Wings("MegaWings", 1, 20);
		p->setWings(w);
	}

	void getEngine() {
		p->setEngine(new Engine("GE", 1, 200));
	}

	void getSerie() {
		p->setSeries(1);
	}

	void getBrand() {
		p->setBrand("Boeing");
	}
};