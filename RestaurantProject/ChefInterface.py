from config import *

class Chef():
	def __init__(self):
		helper.clearWindow()
		self.recipesInterface()

	def createRecipe(self):
		'''Asks the input to create the recipe and validates it.'''
		anotherRecipe = True
		while(anotherRecipe):
			name = raw_input("What's the name of the recipe? ").lower()
			price = raw_input("What's the price of the recipe? ").lower()
			checkRecipe = helper.findRecipe(name)
			if(checkRecipe != None):
				print "Sorry, a recipe with this name is already in the database"
			else:
				helper.newRecipe(name, price, "food")
			another = raw_input("Do you want to create another recipe?" + t.bold("[y/n]")).lower()
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
			print t.blink(t.bold("(1)")), "Create a new recipe"
			print t.blink(t.bold("(2)")), "Generate popularity report"
			print t.blink(t.bold("(3)")), "Show all recipes"
			print t.blink(t.bold("(4)")), "Find a recipe by name"
			print t.blink(t.bold("(5)")), "Generate popularity report"
			print t.blink(t.red("(6)")), "Delete a recipe by name"
			print t.blink(t.red("(7)")), "Delete all recipes"
			print t.blink(t.red("(8)")), "Exit recipes interface"
			option = input(t.bold("1|2|3|4|5|6|7|8 "))
			if(option == 1):
				self.createRecipe()
			elif(option == 2):
				helper.createMenu()
			elif(option == 3):
				helper.printRecipes()
			elif(option == 4):
				self.findRecipeByName()
			elif(option == 5):
				self.generatePopularyReport()
			elif(option == 6):
				self.deleteByName()
			elif(option == 7):
				self.clearRecipes()
			elif(option == 8):
				anotherCommand = False
			else:
				self.clearWindow()
				print "I did not understand you. Please just write the number"