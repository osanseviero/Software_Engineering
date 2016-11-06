from pymongo import MongoClient
from passlib.hash import sha256_crypt
from blessings import Terminal
client = MongoClient()
db = client.test_database	
t = Terminal()

import ChefInterface
import WaiterInterface

class System:
	''' Class to manage the whole system'''

	userLogged = False

	def __init__(self):
		print t.underline("Welcome to the restaurant")

	def isUserLogged(self):
		return self.userLogged

	def enter(self):
		if (not self.isUserLogged()):
			self.logInUser()
		else:
			ChefInterface.Chef()

	def logInUser(self):
		'''Code to log in the user and authenticate'''
		WaiterInterface.Waiter()



a = System()
a.enter()