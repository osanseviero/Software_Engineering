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

	def interface(self):
		helper.clearWindow()
		print "Warehouse interface"
		anotherCommand = True
		while(anotherCommand):
			print "What do you want to do?"
			print t.blink(t.bold("(1)")), "Receive Ingredient"
			print t.blink(t.bold("(2)")), "Print all stored ingredients"
			print t.blink(t.bold("(3)")), "Check requests from the kitchen"
			print t.blink(t.red("(4)")), "Exit warehouse interface"
			option = raw_input(t.bold("1|2|3|4 "))
			if(option == '1'):
				self.receiveIngredient()
			elif(option == '2'):
				helper.printStoredIngredients()
			elif(option == '3'):
				db.drop_collection(helper.getStoredIngredients())
			elif(option == '4'):
				anotherCommand = False
			else:
				helper.clearWindow()
				print "I did not understand you. Please just write the number"

