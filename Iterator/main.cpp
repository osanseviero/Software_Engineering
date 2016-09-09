#include <iostream>
#include "persona.h"
#include "aggregate.h"
#include "iterator.h"
using namespace std;

int main()
{
    Persona a(17);
    Persona b(19);
    Persona c(31);
    Aggregate<Persona> p;
    p.add(a);
    p.add(b);
    p.add(c);
    Iterator<Persona>* i;
    for(i = p.getIterator(); i->hasNext(); )
    {
        cout << (i->next()).getEdad();
    }
    delete i;
}