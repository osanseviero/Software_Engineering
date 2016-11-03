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
		
	def clearWindow(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	def newRecipe(self, name, price):
		newRecipe = {"name" : name, "price" : price}
		self.recipes.insert(newRecipe)
		print "Created recipe for: " , t.bold(name)

	def createRecipe(self):
		anotherRecipe = True
		while(anotherRecipe):
			name = raw_input("What's the name of the recipe? ")
			price = raw_input("What's the price of the recipe? ")
			self.newRecipe(name, price)
			another = raw_input("Do you want to create another recipe?" + t.bold("[y/n]"))
			if(another == 'n'):
				anotherRecipe = False
				self.clearWindow()

	def clearRecipes(self):
		sure = raw_input(t.red("Are you sure you want to erase all your recipes?") + t.bold("[y/n]"))
		if(sure == 'y'):
			db.drop_collection(self.recipes)
		self.clearWindow()
		print "All your recipes were erased"

	def findRecipe(self, name):
		recipe = self.recipes.find_one({"name": name})

	def printRecipes(self):
		t.bold("List of Recipes")
		for recipe in self.recipes.find():
			print recipe

	def recipesInterface(self):
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
				print "Not implemented"
			elif(option == 4):
				print "Not implemented"
			elif(option == 5):
				self.clearRecipes()
			elif(option == 6):
				anotherCommand = False
			else:
				self.clearWindow()
				print "I did not understand you. Please just write the number"


	








	
