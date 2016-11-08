from pymongo import MongoClient
from passlib.hash import sha256_crypt
from blessings import Terminal
client = MongoClient()
db = client.test_database	
t = Terminal()
from getpass import getpass

import ChefInterface
import WaiterInterface
import AdminInterface
import helper

class System:
	''' Class to manage the whole system'''

	userLogged = False

	def __init__(self):
		helper.clearWindow()
		print t.underline("Welcome to the restaurant")

	def enter(self):
		if (not self.userLogged):
			self.logInUser()
		else:
			AdminInterface.interface()

	def logInUser(self):
		'''Code to log in the user and authenticate'''
		anotherCommand = True

		while anotherCommand:
			username = raw_input(t.bold("Which is the username?(q for quit) "))
			if username == 'q':
				anotherCommand = False
			else:
				password = getpass('Enter your password: ')
				if helper.checkPassword(username, password):
					userType = int(db.workers.find_one({"user": username})["type"])
					if(userType == 1):
						AdminInterface.Admin(db.workers)
					elif(userType == 2):
						ChefInterface.Chef()
					elif(userType == 3):
						WaiterInterface.Waiter()
				else:
					print "Wrong password"



a = System()
a.enter()