class Plane {
public:
	void setSeries(int series) {
		this->series = series;
	}

	int getSerie() {
		return this->series;
	}

	void setWings(Wings* w) {
		this->wings = w;
	}

	void setEngine(Engine* e) {
		this->engine = e;
	}

	void setBrand(std::string brand) {
		this->brand = brand;
	}

private:
	int series;
	std::string brand;
	Wings* wings;
	Engine* engine;
};