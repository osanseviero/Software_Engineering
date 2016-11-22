from config import *

class System:
	''' Class to manage the whole system'''

	def __init__(self):
		helper.clearWindow()
		print t.underline("Welcome to the restaurant")

	def logInUser(self):
		'''Code to log in the user and authenticate'''
		anotherCommand = True
		workers = db.workers

		while anotherCommand:
			username = raw_input(t.bold("Which is the username?(q for quit) "))

			if username == 'q':
				anotherCommand = False

			elif(helper.isUser(username) == None):
				print "Sorry there's no user with that name, try another one"

			else:
				password = getpass('Enter your password: ')
				if helper.checkPassword(username, password):
					userType = int(workers.find_one({"user": username})["type"])
					if(userType == 1):
						AdminInterface.Admin(workers)
					elif(userType == 2):
						ChefInterface.Chef()
					elif(userType == 3):
						WaiterInterface.Waiter()
					elif(userType == 4):
						BartenderInterface.Bartender()
					elif(userType == 5):
						StorerInterface.Storer()
					elif(userType == 6):
						WarehouseInterface.Warehouse()
				else:
					print "Wrong password"


a = System()
a.logInUser()