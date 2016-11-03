import Worker

from pymongo import MongoClient
from passlib.hash import sha256_crypt
from blessings import Terminal
client = MongoClient()
db = client.test_database	
t = Terminal()

import os

class Waiter(Worker.WorkerManager):
	max_tables = 10

	def __init__(self, workers, recipes, tables):
		self.workers = workers
		self.recipes = recipes
		self.tables = tables
		self.interface()

	def findTable(self, num):
		'''Finds a table. Returns None if not found'''
		return self.tables.find_one({"num": num})

	def printTables(self):
		'''Prints all the tables in document format'''
		self.clearWindow()
		if(self.tables.count() == 0):
			print "There are no recipes"
		else:
			print t.bold("List of Tables")
			for table in self.tables.find():
				print table

	def printRecipes(self):
		'''Prints all the recipes in document format'''
		self.clearWindow()
		if(self.recipes.count() == 0):
			print "There are no recipes"
		else:
			print t.bold("List of Recipes")
			for recipe in self.recipes.find():
				print recipe	

	def newTable(self, num, persons):
		'''Creates a table document and saves it to the tables collection'''
		newTable = {"num" : num, "persons" : persons}
		self.tables.insert(newTable)
		print "Created table: " , t.bold(num)

	def createTable(self):
		'''Asks the input to create the table and validate it.'''
		anotherTable= True
		while(anotherTable):
			num = raw_input("What's the number of the table? ")
			persons = raw_input("What's the number of max persons in table?")
			checkTable = self.findTable(num)
			if(checkTable != None):
				print "Sorry, a table with this number is already in the database"
			else:
				if(self.tables.count() == self.max_tables):
					print "Sorry, the max number of tables was reached"
					anotherTable = False
				else:
					self.newTable(num, persons)
			another = raw_input("Do you want to create another table?" + t.bold("[y/n]")).lower()
			if(another == 'n'):
				anotherTable = False
				self.clearWindow()

	def interface(self):
		anotherCommand = True
		while(anotherCommand):
			print "What do you want to do?"
			print t.blink(t.bold("(1)")), "List all recipes"
			print t.blink(t.bold("(2)")), "Create a new table"
			print t.blink(t.red("(6)")), "Exit recipes interface"
			option = input(t.bold("1|2|3|4|5|6 "))
			if(option == 1):
				self.printRecipes()
			elif(option == 2):
				self.createTable()
			elif(option == 6):
				anotherCommand = False
			else:
				self.clearWindow()
				print "I did not understand you. Please just write the number"

