class Engine {
public:
	Engine(std::string brand, int series, int power) {
		this->brand = brand;
		this->series = series;
		this->power = power;
	}

	std::string getBrand() {
		return this->brand;
	}

	int getSeries() {
		return this->series;
	}

	int getPower() {
		return this->power;
	}

private:
	std::string brand;
	int series;
	int power;
};