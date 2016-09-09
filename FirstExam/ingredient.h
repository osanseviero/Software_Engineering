class Ingredient
{
public:
    virtual void datos() = 0;
    virtual Ingredient* clonar() = 0;
    std::string name;
};

template <class Base, class SubClase>
class ClonIngredient : public Base
{
public:
    virtual Base* clonar()
    {
        return new SubClase(dynamic_cast<SubClase&>(*this));    
    }
};
