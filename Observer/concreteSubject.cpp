#include "subject.cpp"

class ConcreteSubject : public Subject
{
public:
    void ChangePrice(float price) {
    	Notify(price);
    }
};