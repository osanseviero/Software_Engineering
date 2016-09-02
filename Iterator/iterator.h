class Iterator {
public:
	virtual Object* first() = 0;
	virtual Object* next() = 0;
	virtual bool isDone() = 0;
	virtual Object* CurrentItem() = 0;
}