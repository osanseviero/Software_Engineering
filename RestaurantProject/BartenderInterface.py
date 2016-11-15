from config import *

class Chef():
	def __init__(self):
		helper.clearWindow()
		self.recipesInterface()

	def newRecipe(self, name, price):
		'''Creates a recipe document and saves it to the recipes collection'''
		newRecipe = {"name" : name, "price" : price, "pop" : 0}
		helper.getRecipes().insert(newRecipe)
		print "Created drink recipe for: " , t.bold(name)

	def createRecipe(self):
		'''Asks the input to create the recipe and validates it.'''
		anotherRecipe = True
		while(anotherRecipe):
			name = raw_input("What's the name of the drink? ").lower()
			price = raw_input("What's the price of the drink? ").lower()
			checkRecipe = helper.findRecipe(name)
			if(checkRecipe != None):
				print "Sorry, a drink recipe with this name is already in the database"
			else:
				self.newRecipe(name, price)
			another = raw_input("Do you want to create another drink?" + t.bold("[y/n]")).lower()
			if(another == 'n'):
				anotherRecipe = False
				helper.clearWindow()

	def clearRecipes(self):
		'''Erases all the recipes'''
		sure = raw_input(t.red("Are you sure you want to erase all your recipes?") + t.bold("[y/n]")).lower()
		if(sure == 'y'):
			db.drop_collection(helper.getRecipes())
		helper.clearWindow()
		print "All your recipes were erased"

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
			print t.blink(t.bold("(4)")), "Generate popularity report"
			print t.blink(t.red("(5)")), "Delete a drink by name"
			print t.blink(t.red("(6)")), "Delete all drink"
			print t.blink(t.red("(7)")), "Exit drink interface"
			option = input(t.bold("1|2|3|4|5|6|7 "))
			if(option == 1):
				self.createRecipe()
			elif(option == 2):
				helper.printRecipes()
			elif(option == 3):
				self.findRecipeByName()
			elif(option == 4):
				self.generatePopularyReport()
			elif(option == 5):
				self.deleteByName()
			elif(option == 6):
				self.clearRecipes()
			elif(option == 7):
				anotherCommand = False
			else:
				self.clearWindow()
				print "I did not understand you. Please just write the number"