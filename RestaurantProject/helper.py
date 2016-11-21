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

def getStoredIngredients():
	return db.storedIngredients

def getKitchenIngredients():
	return db.kitchenIngredients

def newRecipe(name, price, type, ingredients):
	'''Creates a recipe document and saves it to the recipes collection'''
	newRecipe = {"name" : name, "price" : price, "pop" : 0, "type" : type, "ingredients" : ingredients}
	getRecipes().insert(newRecipe)
	print "Created recipe for: " , t.bold(name)

def newIngredient(name, price):
	'''Creates an ingredient document and saves it to the recipes collection'''
	newIngredient = {"name" : name, "price" : price, "pop" : 0}
	getIngredients().insert(newIngredient)
	print " Added  : " , t.bold(name), " to the database."

def registerIngredient(ingredient_id, quantity, expiration):
	'''Save an instance of ingredient with an associated quantity and expiration date'''
	ingredientCopy = {"ingredient_id" : ingredient_id, "quantity" : quantity, "expiration" : expiration}
	getIngredients().update({"_id" : ingredient_id },{'$inc' : {"pop": quantity}})
	getStoredIngredients().insert(ingredientCopy)

def clearWindow():
	'''Clears the console window'''
	os.system('cls' if os.name == 'nt' else 'clear')

def printRecipes():
	'''Prints all the recipes in full format, including every ingredient it has'''
	clearWindow()
	if(getRecipes().count() == 0):
		print "There are no recipes"
	else:
		print t.bold("List of Recipes")
		for recipe in getRecipes().find({"type":"food"}):
			print "Recipe " , recipe['name'], " cost: "  , recipe['price']
			for ingredientId in recipe['ingredients']:
				ingredient = findIngredientById(ingredientId)
				print "\tIngredient: " , ingredient['name'], " popularity: ", ingredient['pop']

def printDrinks():
	'''Prints all the drinks in document format'''
	clearWindow()
	if(getRecipes().count() == 0):
		print "There are no drinks"
	else:
		print t.bold("List of Drinks")
		for recipe in getRecipes().find({"type":"drink"}):
			print "Drink " , recipe['name'], " cost: "  , recipe['price']
			for ingredientId in recipe['ingredients']:
				ingredient = findIngredientById(ingredientId)
				print "\tIngredient: " , ingredient['name'], " popularity: ", ingredient['pop']

def printIngredients():
	clearWindow()
	if(getIngredients().count() == 0):
		print "There are no ingredients in warehouse"
	else:
		print t.bold("List of Ingredients")
		for ingredient in getIngredients().find():
				print "Ingredient: " , ingredient['name'], " cost: "  , ingredient['price'], " popularity: ", ingredient['pop']

def printStoredIngredients():
	clearWindow()
	if(getStoredIngredients().count() == 0):
		print "There are no ingredients stored at warehouse"
	else:
		print t.bold("List of Ingredients Stored")
		for storedIngredient in getStoredIngredients().find():
			ingredient = findIngredientById(storedIngredient['ingredient_id'])
			print "Ingredient: " , ingredient['name']
			print "\t cost: "  , ingredient['price'], " popularity: ", ingredient['pop']	
			print "\t quantity: "  , storedIngredient['quantity'], " expiration: ", storedIngredient['expiration']	

def isUser(name):
	'''finds if theres a user with such name'''
	if(getWorkers().find_one({"name": name})):
		return 1
	else:
		return None

def findRecipeById(id):
	'''Finds a recipe. Returns None if not found'''
	return getRecipes().find_one({"_id": id})

def findRecipe(name):
	'''Finds a recipe. Returns None if not found'''
	return getRecipes().find_one({"name": name})

def findIngredientById(id):
	'''Finds an ingredient by ID. Returns None if not found'''
	return getIngredients().find_one({"_id": id})

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

def selectIngredients():
	'''Propmts the user to select ingredients and returns an array of ingredient ids'''
	name = ''
	order = []
	while(True):
		name = raw_input("What's the name of the ingredient? Press s to save. ").lower()
		if(name == 's'):
			print order , " was added to the product"
			return order

		ingredient = findIngredient(name)
		if ingredient == None:
			print t.red("Ingredient was not found")
		else:
			print ingredient['name'] + ' was added to the product'
			order.append(ingredient['_id'])

def requestIngredients():
	print 'hello'





