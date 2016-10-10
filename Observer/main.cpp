#include "concreteSubject.cpp"

int main()
{
    ConcreteSubject product;
                    
    ConcObs shop1("Shop 1");
    ConcObs shop2("Shop 2");
    ConcObs shop2("Shop 3");

    product.Attach(&shop1);
    product.Attach(&shop2);
    product.Attach(&shop3);

    product.ChangePrice(23.0f);
    product.Detach(&shop2);            
    product.ChangePrice(26.0f);

    return 0;
}
