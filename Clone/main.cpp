#include <iostream>
using namespace std;

class Personaje
{
public:
    virtual void correr() = 0;
    virtual Personaje* clonar() = 0;
};

template <class Base, class SubClase>
class ClonPersonaje : public Base
{
public:
    virtual Base* clonar()
    {
        return new SubClase(dynamic_cast<SubClase&>(*this));    
    }
};

class Principe : public ClonPersonaje<Personaje, Principe>
{   
public:
    void seleccionarArma();
    void atacar();
    void correr()
    {
        cout << "El principe corre rápido" << endl;
    }
};

class Princesa : public ClonPersonaje<Personaje, Princesa>
{
public:
    void gritar();
    void correr()
    {
        cout << "La princesa corre medio lento" << endl;
    }
};

class Villano : public ClonPersonaje<Personaje, Villano>
{
public:
    void atacar();
    void atraparPricnesa();
    void correr()
    {
        cout << "El villano no necesita correr" << endl;
    }
};

class VillanoVolador : public ClonPersonaje<Villano, VillanoVolador>
{
public:
    void correr()
    {
        cout << "También puede volar" << endl;
    }
};

int main()
{
    VillanoVolador vv;
    Villano v;
    Princesa p;
    Principe pri;
    
    Personaje* pe = vv.clonar();
    pe->correr();
    
    return 1;
}