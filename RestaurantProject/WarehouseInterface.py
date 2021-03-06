from config import *

class Warehouse():

	def __init__(self):
		helper.clearWindow()
		self.interface()

	def addIngredient(self):
		anotherIngredient = True
		while(anotherIngredient):
			name = raw_input("What's the name of the ingredient? ").lower()
			price = raw_input("What's the price of the ingredient? ").lower()
			if(name == '' or price == ''):
				helper.clearWindow()
				print "Sorry, important information on the ingredient is missing, try again"
				break
			elif(price.isalpha()):
				print "Make sure you're using numbers in the price, try again"
				break
			checkIngredient = helper.findIngredient(name)
			if(checkIngredient != None):
				print "The ingredient already exists"
			else:
				helper.newIngredient(name, price)
			another = raw_input("Do you want to add another ingredient?" + t.bold("[y/n]")).lower()
			if(another == 'n'):
				anotherIngredient = False
				helper.clearWindow()

	def updateIngredient(self):
		name = raw_input("What's the name of the ingredient? ").lower()
		ingredient = helper.findIngredient(name)
		if(ingredient == None):
			helper.clearWindow()
			print "Sorry, this ingredient does not exist"
		else:
			print "Previous price is: " , ingredient['price']
			price = raw_input("What's the price of the ingredient? ").lower()
			if(price.isalpha() or price == ''):
				helper.clearWindow()
				print "Make sure you're using numbers in the price, try again"
			else:
				helper.getIngredients().update({"name" : ingredient['name'] },{ '$set': {"price": str(price)}})

	def clearIngredients(self):
		db.drop_collection(helper.getIngredients())

	def interface(self):
		helper.clearWindow()
		print "Warehouse admin interface"
		anotherCommand = True
		while(anotherCommand):
			print "What do you want to do?"
			print t.blink(t.bold("(1)")), "Add ingredient"
			print t.blink(t.bold("(2)")), "Print all ingredients"
			print t.blink(t.bold("(3)")), "Change price of ingredient"
			print t.blink(t.red("(4)")), "Erase ingredients database [ERROR PRONE]"
			print t.blink(t.bold("(5)")), "Check kitchen requests"
			print t.blink(t.red("(6)")), "Exit warehouse interface"
			option = raw_input(t.bold("1|2|3|4|5|6 "))
			if(option == '1'):
				self.addIngredient()
			elif(option == '2'):
				helper.printIngredients()
			elif(option == '3'):
				helper.printIngredients()
				self.updateIngredient()
			elif(option == '4'):
				self.clearIngredients()
			elif(option == '5'):
				helper.printKitchenRequests()
			elif(option == '6'):
				anotherCommand = False
			else:
				helper.clearWindow()
				print "I did not understand you. Please just write the number"


