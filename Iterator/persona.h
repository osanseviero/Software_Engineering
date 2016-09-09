class Persona
{
public:
    Persona(){}
    Persona(int edad){this->edad = edad;}
    ~Persona(){}
    int getEdad()
    {
        return edad;
    }
private:
    int edad;
};