class Agregate {
public:
	virtual void createIterator() = 0;
	virtual Iterator getIterator() = 0;

	virtual void addObject(Object o);
	virtual bool find(Object o);

	int size;
	int capacity;
}