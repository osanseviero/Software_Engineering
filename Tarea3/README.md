# Computer Factory 
API that encapsulates process of computer creation. It needs to be flexible so code does not need to be changed. It need to implement Factory Pattern and Singleton Pattern.

Types of computer (In the future there will be more.)

* Desktop
* Laptop
* Netboot
* Tablet


Process:

* Selection of components.
* Assembly of components.
* Instalation and configuration of Software.
* Packaging of computer.

Implementation 

	Computer is the base class and implementation. It uses pure virtual functions to enforce the overriding of subclasses. 
	
	Computer factory was done separated to keep implementation separated from interface.

	Computer factory works as the base class while there could be many child classes. To avoid this, computerFactoryConcrete has a generic behavior.
	
	If the company needs to add another type of computer, just computerFactory class needs to be changed. 

	To add layers of protection and mantain the Singleton Pattern, copy and assignment were made private. Also, most of the class constructors are now private.
