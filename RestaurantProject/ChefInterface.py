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
			checkRecipe = helper.findRecipe(name)
			if(checkRecipe != None):
				print "Sorry, a recipe with this name is already in the database"
			else:
				price = 0
				helper.printIngredients()
				ingredients = helper.selectIngredients()
				for ingredientId in ingredients:
					ingredient = helper.findIngredientById(ingredientId)
					price += int(ingredient['price'])
				helper.newRecipe(name, price, "food", ingredients)
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

	def createMenuTime(self, time):
		'''Generate an array with products'''
		helper.printRecipes()
		dishes = []
		product = ''
		print t.bold("Enter products for " + time)
		while(product != 'e' and product != 's'):
			product = raw_input("What's the name of the product for first dish? Press s to save. Press e to exit. ").lower()
			if product != 'e' and product != 's':
				recipe = helper.findRecipe(product)
				if recipe == None:
					print t.red("Recipe was not found")
				else:
					print recipe['name'], " was added to the order."
					dishes.append(recipe['_id'])
					print "Current order: "
					for dish in dishes:
						print helper.findRecipeById(dish)
		if product == 's':
			return dishes
		else:
			return None

	def createMenu(self):
		'''Generate the menu'''
		helper.clearWindow()

		firstDishes = []
		secondDishes = []
		desserts = []

		name = raw_input("What's the name of the menu?").lower()
		disc = input("What's discount is going to be given in this menu?")	

		firstDishes = self.createMenuTime("first dish")
		secondDishes = self.createMenuTime("second dish")
		desserts = self.createMenuTime("dessert")

		newMenu = {"name" : name, "disc" : disc, "pop" : 0, "first" : firstDishes, "second" : secondDishes, "desserts" : desserts}

		helper.getMenus().insert(newMenu)
		print "Menu saved"

	def recipesInterface(self):
		'''Main interface to manage recipes'''
		anotherCommand = True
		while(anotherCommand):
			print "What do you want to do?"
			print t.blink(t.bold("(1)")), "Create a new recipe"
			print t.blink(t.bold("(2)")), "Create a new menu"
			print t.blink(t.bold("(3)")), "Show all recipes"
			print t.blink(t.bold("(4)")), "Find a recipe by name"
			print t.blink(t.bold("(5)")), "Request ingredients to warehouse"
			print t.blink(t.red("(6)")), "Print ingredients stored at the warehouse"
			print t.blink(t.bold("(7)")), "Generate popularity report"
			print t.blink(t.red("(8)")), "Delete a recipe by name"
			print t.blink(t.red("(9)")), "Delete all recipes"
			print t.blink(t.red("(10)")), "Exit chef interface"
			option = raw_input(t.bold("1|2|3|4|5|6|7|8|9|10 "))
			if(option == '1'):
				self.createRecipe()
			elif(option == '2'):
				self.createMenu()
			elif(option == '3'):
				helper.printRecipes()
			elif(option == '4'):
				self.findRecipeByName()
			elif(option == '5'):
				helper.requestIngredients()
			elif(option == '6'):
				helper.printKitchenStore()
			elif(option == '7'):
				self.generatePopularyReport()
			elif(option == '8'):
				self.deleteByName()
			elif(option == '9'):
				self.clearRecipes()
			elif(option == '10'):
				helper.clearWindow()
				anotherCommand = False
			else:
				helper.clearWindow()
				print "I did not understand you. Please just write the number"