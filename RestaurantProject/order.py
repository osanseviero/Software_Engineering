from pymongo import MongoClient
from passlib.hash import sha256_crypt
from blessings import Terminal
client = MongoClient()
db = client.test_database	
t = Terminal()

import os
import helper

def printRecipes():
	helper.printRecipes()

def selectRecipe():
	print "Selecting a recipe"

def newOrder():
	helper.clearWindow()
	print "Register the new order"
	anotherCommand = True
	while(anotherCommand):
		print "What do you want to do?"
		print t.blink(t.bold("(1)")), "Print all the products with their respective price."
		print t.blink(t.bold("(2)")), "Select a product."
		print t.blink(t.bold("(3)")), "Exit order interface"
		option = input(t.bold("1|2|3 "))
		if(option == 1):
			printRecipes()
		elif(option == 2):
			selectRecipe()
		elif(option == 3):
			anotherCommand = False
		else:
			helper.clearWindow()
			print "I did not understand you. Please just write the number"