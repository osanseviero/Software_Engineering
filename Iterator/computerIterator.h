class ComputerIterator: public iterator {
	Object* next() {
		return objectList[idx++];
	}

	Object* first() {
		return objectList[0];
	}

	int idx = 0;
}