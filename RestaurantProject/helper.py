from config import *

def getWorkers():
	return db.workers

def getRecipes():
	return db.recipes 

def getMenus():
	return db.menu

def getTables():
	return db.tables

def getIngredients():
	return db.ingredients

def newRecipe(name, price, type):
	'''Creates a recipe document and saves it to the recipes collection'''
	newRecipe = {"name" : name, "price" : price, "pop" : 0, "type" : type}
	getRecipes().insert(newRecipe)
	print "Created recipe for: " , t.bold(name)


def newIngredient(name, price, quantity):
	'''Creates a recipe document and saves it to the recipes collection'''
	newIngredient = {"name" : name, "price" : price, "pop" : 0, "quantity" : quantity}
	getIngredients().insert(newIngredient)
	print " Added  : " , t.bold(name), " to the database."

def clearWindow():
	'''Clears the console window'''
	os.system('cls' if os.name == 'nt' else 'clear')

def printRecipes():
	'''Prints all the recipes in document format'''
	clearWindow()
	if(getRecipes().count() == 0):
		print "There are no recipes"
	else:
		print t.bold("List of Recipes")
		for recipe in getRecipes().find({"type":"food"}):
			print "Recipe " , recipe['name'], " cost: "  , recipe['price']

def printDrinks():
	'''Prints all the drinks in document format'''
	clearWindow()
	if(getRecipes().count() == 0):
		print "There are no recipes"
	else:
		print t.bold("List of Drinks")
		for recipe in getRecipes().find({"type":"drink"}):
				print "Drink " , recipe['name'], " cost: "  , recipe['price']

def printIngredients():
	clearWindow()
	if(getIngredients().count() == 0):
		print "There are no ingredients in warehouse"
	else:
		print t.bold("List of Ingredients")
		for ingredient in getIngredients().find():
				print "Ingredient: " , ingredient['name'], " cost: "  , ingredient['price'], " quantity: ", ingredient['quantity']


def findRecipeById(id):
	'''Finds a recipe. Returns None if not found'''
	return getRecipes().find_one({"_id": id})

def findRecipe(name):
	'''Finds a recipe. Returns None if not found'''
	return getRecipes().find_one({"name": name})

def findIngredient(name):
	'''Finds a Ingredient. Returns None if not found'''
	return getIngredients().find_one({"name": name})

def findTable(num):
	'''Finds a table. Returns None if not found'''
	return getTables().find_one({"num": num})

def checkPassword(username, password):
	hash = db.workers.find_one({"user": username})["password"]
	return sha256_crypt.verify(password, hash)

def getMaxTables():
	return 10