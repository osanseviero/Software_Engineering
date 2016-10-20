/*
    Command pattern applied to a generic array.
    Different actions can be defined as children of the Command.
    An array of commanders can hold all the info. A map is a better implementation for good interface.
    
*/

#include <map>
#include <string>
#include <iostream>
using namespace std;

template<class T>
class Command
{
    public:
        virtual T execute(T*, int) = 0;
};

template<class T>
class Sum : public Command<T>
{
    T execute(T* arr, int size) {
        T acum = 0;
        for (int i = 0; i < size; i++) {
            acum += arr[i];
        }
        return acum;
    }
};

template<class T>
class Operation
{
    map<string, Command<T>*> operation;  
    public:
        Operation(){}
        
        void insert(string s, Command<T>* func) {
            operation.insert(make_pair(s, func));
        }
        
        Command<T>* getOp(string op) {
            typename map<string, Command<T>*>::iterator it;
            it  = operation.find(op);
            if(it != operation.end()) {
                return it->second;
            }
            return NULL;
        }
};

int main()
{
    
    Operation<double> op;
    op.insert("suma", new Sum<double>);
    
    double* arrD = new double[5]{2.1,3.5, 2.3,4.3,1.4};
    Command<double>* c = op.getOp("suma");
    cout << c->execute(arrD, 5);
}