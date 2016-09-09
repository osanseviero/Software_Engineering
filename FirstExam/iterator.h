template<class T>
class Iterator
{
public:
    Iterator(Aggregate<T>* aggregate) : idx(0), aggregate(aggregate)
    {}
    
    T next()
    {
        if(hasNext())
            return aggregate->lista[idx++];
        else
            return 0;
    }
    
    bool hasNext()
    {
        return (idx < aggregate->getPos());
    }
    ~Iterator(){}

private:
    Iterator(){}
    Aggregate<T>* aggregate;
    int idx;
};