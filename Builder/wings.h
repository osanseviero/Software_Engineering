class Wings {
public:
	Wings(std::string brand, int series, int hiper) {
		this->brand = brand;
		this->series = series;
		this->hiper = hiper;
	}

	void setBrand(std::string brand) {
		this->brand = brand;
	}

	std::string getBrand() {
		return this->brand;
	}

	int getSeries() {
		return this->series;
	}

	int getHiper() {
		return this->hiper;
	}

private:
	std::string brand;
	int series;
	int hiper;
};