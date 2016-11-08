from pymongo import MongoClient
from passlib.hash import sha256_crypt
from blessings import Terminal
client = MongoClient()
db = client.test_database	
t = Terminal()

from getpass import getpass
import os

class Admin:
	'''API to interact with workers.
		This is just a test, some of this functions are for the login system and admin.
	'''

	def __init__(self, collection):
		helper.clearWindow()
		self.workers = collection
		self.interface()

	def clearWindow(self):
		'''Clears the console window'''
		os.system('cls' if os.name == 'nt' else 'clear')

	def createUser(self, user, name, lastname, password, salary, userType):
		newWorker = {"user" : user, "name" : name, "lastname": lastname, "password": sha256_crypt.encrypt(password), "salary" : salary, "type": userType}
		self.workers.insert(newWorker)
		print "Saved worker with username " , user

	def newUser(self):
		'''Register a new user in the system'''
		self.clearWindow()
		username = raw_input(t.bold("Which is the username? "))
		name = raw_input(t.bold("Which is the name? "))
		lastName = raw_input(t.bold("Which is the lastname? "))
		salary = int(raw_input(t.bold("Which is the salary? ")))
		password = getpass('Enter your password: ')
		print "Which is the type of user?"
		userType = raw_input(t.bold("(1)Admin (2)Chef (3) Waiter"))
		self.createUser(username, name, lastName, password, salary, userType)		

	def count(self):
		print "Total workers: ", self.workers.count()

	def printWorkers(self):
		self.clearWindow()
		for worker in self.workers.find():
			print worker

	def clearUsers(self):
		self.clearWindow()
		db.drop_collection(self.workers)

	def findUser(self, username):
		return self.workers.find_one({"user": username})

	def interface(self):
		'''Main interface to manage the admin'''
		anotherCommand = True
		while(anotherCommand):
			print "What do you want to do?"
			print t.blink(t.bold("(1)")), "Register a new user"
			print t.blink(t.bold("(2)")), "Print all users"
			print t.blink(t.bold("(3)")), "Clear user database"
			print t.blink(t.red("(4)")), "Exit admin interface"
			option = input(t.bold("1|2|3|4 "))
			if option == 1:
				self.newUser()
			elif option == 2:
				self.printWorkers()
			elif option == 3:
				self.clearUsers()
			elif option == 4:
				anotherCommand = False
			else:
				print "Sorry, I could not understand your command."