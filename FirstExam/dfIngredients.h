class DFIngredient : public ClonIngredient<Ingredient, DFIngredient>
{   
public:
    void datos()
    {
        std::cout << "Soy un ingrediente del Distrito Federal." << std::endl;
    }
};

class Chocolate: public ClonIngredient<DFIngredient, Chocolate>
{
public:
    void datos()
    {
        std::cout << "Yo soy dulce." << std::endl;
    }
};

class Fruta: public ClonIngredient<DFIngredient, Fruta>
{
public:
    void datos()
    {
        std::cout << "Soy una fruta." << std::endl;
    }
};



class Merengue: public ClonIngredient<DFIngredient, Merengue>
{
public:
    void datos()
    {
        std::cout << "Tengo mucha azucar" << std::endl;
    }
};













