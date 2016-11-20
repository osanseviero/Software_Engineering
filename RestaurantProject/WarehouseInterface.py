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
			quantity  = raw_input("What's the quantity? ").lower()
			checkIngredient = helper.findIngredient(name)
			if(checkIngredient != None):
				print "se debe agregar la cantidad al ingrediente"
			else:
				helper.newIngredient(name, price, quantity)
			another = raw_input("Do you want to add another ingredient?" + t.bold("[y/n]")).lower()
			if(another == 'n'):
				anotherRecipe = False
				helper.clearWindow()

	def interface(self):
		helper.clearWindow()
		print "Warehouse interface"
		anotherCommand = True
		while(anotherCommand):
			print "What do you want to do?"
			print t.blink(t.bold("(1)")), "Add ingredient"
			print t.blink(t.bold("(2)")), "Print all ingredients"
			print t.blink(t.bold("(3)")), "Take ingredient"
			print t.blink(t.red("(4)")), "Exit warehouse interface"
			option = input(t.bold("1|2|3|4"))
			if(option == 1):
				self.addIngredient()
			elif(option == 2):
				helper.printIngredients()
			elif(option == 4):
				anotherCommand = False
			else:
				helper.clearWindow()
				print "I did not understand you. Please just write the number"


