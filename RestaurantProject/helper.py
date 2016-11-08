from requirements import *

def getWorkers():
	return db.workers

def getRecipes():
	return db.recipes 

def getTables():
	return db.tables

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

def findRecipe(name):
	'''Finds a recipe. Returns None if not found'''
	return getRecipes().find_one({"name": name})

def checkPassword(username, password):
	hash = db.workers.find_one({"user": username})["password"]
	return sha256_crypt.verify(password, hash)