/*
    Command pattern applied to a generic array.
    Command receives a receiver (object) and an action related to it.
    Base class (commander) has an execute method that calls the specific action of the receiver.
*/

#include <iostream>
using namespace std;

class Command
{
    public:
        template<class T, class Func>
        T execute(T* arr , int size, Func fun) {
            return fun(arr, size);
        }
};


template<class T>
T sum(T* arr, int size)
{
    T acum = 0;
    for(int i = 0; i < size; i++)
        acum += arr[i];
    return acum;
}

typedef int(*signature)(int*, int);

int main()
{
    double* arrD = new double[5]{2.1,3.5, 2.3,4.3,1.4};
    char* arrC = new char[5]{'A','R','I','E','L'};
    int* arrI = new int[2]{12, 22};
    Command c;
    
    cout << c.execute<double, double(*)(double*,int)>(arrD, 5, sum) << endl; 
    
    cout << c.execute<char, char(*)(char*, int)>(arrC, 5, sum)<< endl; 
    
    cout << c.execute<int, signature>(arrI, 5, sum)<< endl;
}