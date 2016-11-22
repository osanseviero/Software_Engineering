from config import *

class Admin:
	'''
		Admin interface
		Allows to create users, generate reporters, and table creation.
	'''

	def __init__(self, collection):
		helper.clearWindow()
		self.workers = collection
		self.interface()

	def createUser(self, user, name, lastname, password, salary, userType):
		if(helper.isUser(user) != None):
			helper.clearWindow()
			print "Sorry, this user already exists"
		else:
			newWorker = {"user" : user, "name" : name, "lastname": lastname, "password": sha256_crypt.encrypt(password), "salary" : salary, "type": userType}
			self.workers.insert(newWorker)
			print "Saved worker with username " , user

	def newUser(self):
		'''Register a new user in the system'''
		helper.clearWindow()
		username = raw_input(t.bold("Which is the username? "))
		name = raw_input(t.bold("Which is the name? "))
		lastName = raw_input(t.bold("Which is the lastname? "))
		salary = raw_input(t.bold("Which is the salary? "))
		password = getpass('Enter your password: ')
		print "Which is the type of user?"
		userType = raw_input(t.bold("(1)Admin (2)Chef (3) Waiter (4)Bartender (5) Warehouse Worker (6)Warehouse Admin "))
		if(username == '' or name == '' or salary =='' or password == '' or userType == ''):
			helper.clearWindow()
			print "Sorry, we're missing some important information from the new user, try again"
		else:
			self.createUser(username, name, lastName, password, int(salary), userType)		

	def count(self):
		print "Total workers: ", self.workers.count()

	def printWorkers(self):
		helper.clearWindow()
		for worker in self.workers.find():
			print worker['user']
			print "Name of worker: " + worker['name'] + " " + worker['lastname']
			print "Hour Salary: " , worker['salary']
			print "------"

	def clearUsers(self):
		helper.clearWindow()
		db.drop_collection(self.workers)

	def findUser(self, username):
		return self.workers.find_one({"user": username})

	def newTable(self, num, persons):
		'''Creates a table document and saves it to the tables collection. Should just be in admin.'''
		newTable = {"num" : num, "persons" : persons, "numPeople" : 0, "order" : [], "check" : "open"}
		helper.getTables().insert(newTable)
		print "Created table: " , t.bold(str(num))

	def clearTables(self):
		'''Drop all tables from collection. Should just be in admin.'''
		db.drop_collection(helper.getTables())

	def createTable(self):
		'''Asks the input to create the table and validate it. Should just be in admin'''
		anotherTable= True
		while(anotherTable):
			num = int(raw_input("What's the number of the table? "))
			persons = int(raw_input("What's the number of max persons in table?"))
			checkTable = helper.findTable(num)
			if(checkTable != None):
				print "Sorry, a table with this number is already in the database"
			else:
				if(persons > 12):
					print "Sorry, there can't be a table with more than 12 persons."
				elif(persons <= 1):
					print "Sorry, the table needs to have at least 2 persons max."
				elif(helper.getTables().count() == helper.getMaxTables()):
					print "Sorry, the max number of tables was reached"
					anotherTable = False
				else:
					self.newTable(num, persons)
			another = raw_input("Do you want to create another table?" + t.bold("[y/n]")).lower()
			if(another == 'n'):
				anotherTable = False
				helper.clearWindow()

	def interface(self):
		'''Main interface to manage the admin'''
		anotherCommand = True
		while(anotherCommand):
			print "What do you want to do?"
			print t.blink(t.bold("(1)")), "Register a new user"
			print t.blink(t.bold("(2)")), "Print all users"
			print t.blink(t.bold("(3)")), "Create new table"
			print t.blink(t.bold("(4)")), "Clear user database"
			print t.blink(t.bold("(5)")), "Erase table database"
			print t.blink(t.red("(6)")), "Exit"
			option = raw_input(t.bold("1|2|3|4|5|6 "))
			if option == '1':
				self.newUser()
			elif option == '2':
				self.printWorkers()
			elif option == '3':
				self.createTable()
			elif option == '4':
				self.clearUsers()
			elif option == '5':
				self.clearTables()
			elif option == '6':
				anotherCommand = False
			else:
				helper.clearWindow()
				print "Sorry, I could not understand your command."


