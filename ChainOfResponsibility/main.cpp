#include <iostream>
#include <vector>
#include <ctime>
#include "handler1.cpp"
#include "handler2.cpp"

int main()
{
	srand(time(0));
	Handler1 root;
	Handler2 two;

	root.add(&two);
	two.setNext(&root);

	for (int i = 1; i < 10; i++) {
		root.handle(i);
	}
}
