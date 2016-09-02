class Director {
public:
	Director() {};

	Builder* builder;

	void setBuilder(Builder* b) {
		this->builder = b;
	}

	Plane* getPlane() {
		return builder->getPlane();
	}

	void construct() {
		b->createPlane();
		std::cout << "hi" << std::endl;
		b->getWings();
		b->getEngine();
		b->getSerie();
		b->getBrand();
	}

private:
	Builder* b;

};