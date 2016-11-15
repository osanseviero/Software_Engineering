from config import *

def getWorkers():
	return db.workers

def getRecipes():
	return db.recipes 

def getMenus():
	return db.menu

def getTables():
	return db.tables

def newRecipe(name, price, type):
	'''Creates a recipe document and saves it to the recipes collection'''
	newRecipe = {"name" : name, "price" : price, "pop" : 0, "type" : type}
	getRecipes().insert(newRecipe)
	print "Created recipe for: " , t.bold(name)

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
		for recipe in getRecipes().find():
			print "Recipe " , recipe['name'], " cost: "  , recipe['price']

def findRecipeById(id):
	'''Finds a recipe. Returns None if not found'''
	return getRecipes().find_one({"_id": id})

def findRecipe(name):
	'''Finds a recipe. Returns None if not found'''
	return getRecipes().find_one({"name": name})

def findTable(num):
	'''Finds a table. Returns None if not found'''
	return getTables().find_one({"num": num})

def checkPassword(username, password):
	hash = db.workers.find_one({"user": username})["password"]
	return sha256_crypt.verify(password, hash)

def getMaxTables():
	return 10