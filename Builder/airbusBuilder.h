class AirbusBuilder: public Builder {
public:
	void getWings() {
		p->setWings(new Wings("ExaWings", 1, 10));
	}

	void getEngine() {
		p->setEngine(new Engine("GE", 1, 100));
	}

	void getSerie() {
		p->setSeries(1);
	}

	void getBrand() {
		p->setBrand("Airbus");
	}
};