import Worker

from pymongo import MongoClient
from passlib.hash import sha256_crypt
from blessings import Terminal
client = MongoClient()
db = client.test_database	
t = Terminal()

import os

class Chef(Worker.WorkerManager):
	def __init__(self, workers, recipes):
		self.workers = workers
		self.recipes = recipes
		self.recipesInterface()

	def findRecipe(self, name):
		'''Finds a recipe. Returns None if not found'''
		return self.recipes.find_one({"name": name})
		
	def clearWindow(self):
		'''Clears the console window'''
		os.system('cls' if os.name == 'nt' else 'clear')

	def newRecipe(self, name, price):
		'''Creates a recipe document and saves it to the recipes collection'''
		newRecipe = {"name" : name, "price" : price}
		self.recipes.insert(newRecipe)
		print "Created recipe for: " , t.bold(name)

	def createRecipe(self):
		'''Asks the input to create the recipe and validates it.'''
		anotherRecipe = True
		while(anotherRecipe):
			name = raw_input("What's the name of the recipe? ").lower()
			price = raw_input("What's the price of the recipe? ").lower()
			checkRecipe = self.findRecipe(name)
			if(checkRecipe != None):
				print "Sorry, a recipe with this name is already in the database"
			else:
				self.newRecipe(name, price)
			another = raw_input("Do you want to create another recipe?" + t.bold("[y/n]")).lower()
			if(another == 'n'):
				anotherRecipe = False
				self.clearWindow()

	def clearRecipes(self):
		'''Erases all the recipes'''
		sure = raw_input(t.red("Are you sure you want to erase all your recipes?") + t.bold("[y/n]")).lower()
		if(sure == 'y'):
			db.drop_collection(self.recipes)
		self.clearWindow()
		print "All your recipes were erased"

	def findRecipeByName(self):
		'''Finds a recipe given a name.'''
		self.clearWindow()
		name = raw_input("What's the name of the recipe? ").lower()
		recipe = self.findRecipe(name)
		if recipe == None:
			print t.red("Recipe was not found")
		else:
			print recipe

	def deleteByName(self):
		'''Deletes a recipe given a name.'''
		self.clearWindow()
		name = raw_input("What's the name of the recipe? ").lower()
		recipe = self.findRecipe(name)
		if recipe == None:
			print t.red("Recipe was not found")
		else:
			self.recipes.remove({"name": name})
			print "Recipe for ", t.bold(name), " was deleted"

	def printRecipes(self):
		'''Prints all the recipes in document format'''
		self.clearWindow()
		if(self.recipes.count() == 0):
			print "There are no recipes"
		else:
			print t.bold("List of Recipes")
			for recipe in self.recipes.find():
				print recipe

	def recipesInterface(self):
		'''Main interface to manage recipes'''
		anotherCommand = True
		while(anotherCommand):
			print "What do you want to do?"
			print t.blink(t.bold("(1)")), "Create a new recipe"
			print t.blink(t.bold("(2)")), "Show all recipes"
			print t.blink(t.bold("(3)")), "Find a recipe by name"
			print t.blink(t.red("(4)")), "Delete a recipe by name"
			print t.blink(t.red("(5)")), "Delete all recipes"
			print t.blink(t.red("(6)")), "Exit recipes interface"
			option = input(t.bold("1|2|3|4|5 "))
			if(option == 1):
				self.createRecipe()
			elif(option == 2):
				self.printRecipes()
			elif(option == 3):
				self.findRecipeByName()
			elif(option == 4):
				self.deleteByName()
			elif(option == 5):
				self.clearRecipes()
			elif(option == 6):
				anotherCommand = False
			else:
				self.clearWindow()
				print "I did not understand you. Please just write the number"