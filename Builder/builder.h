class Builder {
public:
	Plane* getPlane() {
		return this->p;
	}

	Plane* p;
	

	Plane* createPlane() {
		return new Plane();
	}

	virtual void getWings() = 0;
	virtual void getEngine() = 0;

	virtual void getSerie() = 0;
	virtual void getBrand() = 0;
};