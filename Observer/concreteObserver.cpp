#include "Observer.cpp"

class ConcObs : Observer
{
    std::string name;
    float price;
public:
    ConcObs(std::string n) {
         this->name = name;
    }
    void Update(float price) {
        this->price = price;
        std::cout << "Price at "<< name << " is now "<< price << "\n";
    }
};
