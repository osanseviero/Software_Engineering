#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include "concreteObserver.cpp"
using namespace std;

class Subject {
    std::vector<ConcObs*> list;

public:
    void Attach(ConcObs *product) {
        list.push_back(product);
    }

    void Detach(ConcObs *product) {
         list.erase(std::remove(list.begin(), list.end(), product), list.end());    
    }
    void Notify(float price) {
        for(vector<ConcObs*>::const_iterator iter = list.begin(); iter != list.end(); ++iter)
        {
            if(*iter != 0)
            {
                (*iter)->Update(price);
            }
        }
    }
};