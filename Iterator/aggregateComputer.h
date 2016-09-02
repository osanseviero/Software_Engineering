class Agregate {
public:
	friend class computerIterator

	void createIterator() = 0;
	void addObject(Computer o);
	vector<Computer> objectList;
	int capacity;
}