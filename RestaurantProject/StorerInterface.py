from config import *

class Storer():

	def __init__(self):
		helper.clearWindow()
		self.interface()

	def receiveIngredient(self):
		helper.printIngredients()
		anotherIngredient = True
		while(anotherIngredient):
			name = raw_input("What's the name of the ingredient? ").lower()
			ingredient = helper.findIngredient(name)
			if(ingredient == None):
				print "Sorry, this ingredient does not exist"
			else:
				quantity = input('How many of this ingredient are you registering? ')
				expire = raw_input("Which is the expiration date? ")
				helper.registerIngredient(ingredient['_id'], quantity, expire)
			another = raw_input("Do you want to add another ingredient?" + t.bold("[y/n]")).lower()
			if(another == 'n'):
				anotherIngredient = False
				helper.clearWindow()

	def fulfillKitchenRequests(self):
		helper.printKitchenRequests()
		requestId = input('Which request do you want to fulfill? ')
		request = helper.getRequestById(int(requestId))
		ingredient = helper.findStoredIngredientById(request[0])
		if ingredient == None:
			print "This ingredient is not in the warehouse, please request more."
		print request[1]

		# If there is more of this instance of the ingredient at the warehouse than the requested
		if ingredient['quantity'] > request[1]:
			ingredient['quantity'] -= request[1]
			helper.updateStoredIngredient(ingredient['_id'], ingredient['quantity'])


	def interface(self):
		helper.clearWindow()
		print "Warehouse interface"
		anotherCommand = True
		while(anotherCommand):
			print "What do you want to do?"
			print t.blink(t.bold("(1)")), "Receive Ingredient"
			print t.blink(t.bold("(2)")), "Print all stored ingredients"
			print t.blink(t.bold("(3)")), "Fullfill kitchen Requests"
			print t.blink(t.red("(4)")), "Get kitchen requests"
			print t.blink(t.red("(5)")), "Exit warehouse interface"
			option = raw_input(t.bold("1|2|3|4|5 "))
			if(option == '1'):
				self.receiveIngredient()
			elif(option == '2'):
				helper.printStoredIngredients()
			elif(option == '3'):
				self.fulfillKitchenRequests()
			elif(option == '4'):
				helper.printKitchenRequests()
			elif(option == '5'):
				anotherCommand = False
			else:
				helper.clearWindow()
				print "I did not understand you. Please just write the number"


