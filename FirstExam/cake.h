class Cake {
public:
		std::string state;
		std::string name;
		std::vector<Ingredient*> ingredients;

		virtual void batido() = 0;
		virtual void amasado() = 0;
		virtual void horneado() = 0;
		virtual void decorado() = 0;
		virtual void empacado() = 0;

		virtual ~Cake() {};
};

