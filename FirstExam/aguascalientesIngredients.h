class AguascalientesIngredient : public ClonIngredient<Ingredient, AguascalientesIngredient>
{   
public:
    void datos()
    {
        std::cout << "Soy un ingrediente de Aguascalientes." << std::endl;
    }
};


class Leche : public ClonIngredient<AguascalientesIngredient, Leche>
{
public:
    void datos()
    {
        std::cout << "Vengo de la vaca." << std::endl;
    }
};


class Huevo : public ClonIngredient<AguascalientesIngredient, Huevo>
{
public:
    void datos()
    {
        std::cout << "Vengo de la gallina" << std::endl;
    }
};


class Mantequilla: public ClonIngredient<AguascalientesIngredient, Mantequilla>
{
public:
    void datos()
    {
        std::cout << "Soy suave." << std::endl;
    }
};
