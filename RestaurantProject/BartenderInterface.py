from config import *

class Bartender():
	def __init__(self):
		helper.clearWindow()
		self.recipesInterface()

	def createRecipe(self):
		'''Asks the input to create the recipe and validates it.'''
		anotherRecipe = True
		while(anotherRecipe):
			name = raw_input("What's the name of the drink? ").lower()
			checkRecipe = helper.findRecipe(name)
			if(name == ''):
				print "Sorry, we're missing important information about the drink, try again"
			elif(checkRecipe != None):
				print "Sorry, a drink recipe with this name is already in the database"
			else:
				price = 0
				helper.printStoredIngredients()
				ingredients = helper.selectIngredients()
				for ingredientId in ingredients:
					ingredient = helper.findIngredientById(ingredientId)
					price += int(ingredient['price'])
				helper.newRecipe(name, price, "drink", ingredients)
			another = raw_input("Do you want to create another drink?" + t.bold("[y/n]")).lower()
			if(another == 'n'):
				anotherRecipe = False
				helper.clearWindow()

	def clearDrinks(self):
		'''Erases all the recipes'''
		sure = raw_input(t.red("Are you sure you want to erase all your drinks?") + t.bold("[y/n]")).lower()
		if(sure == 'n'):
			helper.clearWindow()
		elif(sure != 'y'):
			helper.clearWindow()
			print "Sorry, I didn't understand, please write [y/n]"
		elif(sure == 'y'):
			helper.getRecipes().remove({"type": "drink"})
			helper.clearWindow()
			print "All your drinks were erased"

	def findRecipeByName(self):
		'''Finds a recipe given a name.'''
		helper.clearWindow()
		name = raw_input("What's the name of the recipe? ").lower()
		recipe = helper.findRecipe(name)
		if recipe == None:
			print t.red("Recipe was not found")
		else:
			print recipe

	def deleteByName(self):
		'''Deletes a recipe given a name.'''
		helper.clearWindow()
		name = raw_input("What's the name of the recipe? ").lower()
		recipe = helper.findRecipe(name)
		if recipe == None:
			print t.red("Recipe was not found")
		else:
			helper.getRecipes().remove({"name": name})
			print "Recipe for ", t.bold(name), " was deleted"

	def generatePopularyReport(self):
		'''Lists all the recipes with their respective popularity'''
		helper.clearWindow()
		print t.bold("Name") , t.bold("Popularity")
		for recipe in helper.getRecipes().find():
			print recipe['name'] , recipe['pop']


	def recipesInterface(self):
		'''Main interface to manage recipes'''
		anotherCommand = True
		while(anotherCommand):
			print "What do you want to do?"
			print t.blink(t.bold("(1)")), "Create a new drink"
			print t.blink(t.bold("(2)")), "Show all drinks"
			print t.blink(t.bold("(3)")), "Find a drink by name"
			print t.blink(t.bold("(4)")), "Make ingredient request"
			print t.blink(t.bold("(5)")), "Generate popularity report"
			print t.blink(t.red("(6)")), "Delete a drink by name"
			print t.blink(t.red("(7)")), "Delete all drink"
			print t.blink(t.red("(8)")), "Exit drink interface"
			option = raw_input(t.bold("1|2|3|4|5|6|7 "))
			if option == '1':
				self.createRecipe()
			elif option == '2':
				helper.printDrinks()
			elif option == '3':
				self.findRecipeByName()
			elif option == '4':
				helper.requestIngredients()
			elif option == '5':
				self.generatePopularyReport()
			elif option == '6':
				self.deleteByName()
			elif option == '7':
				self.clearDrinks()
			elif option == '8':
				anotherCommand = False
			else:
				helper.clearWindow()
				print "I did not understand you. Please just write the number"