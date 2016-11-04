import WaiterInterface

from pymongo import MongoClient
from passlib.hash import sha256_crypt
from blessings import Terminal
client = MongoClient()
db = client.test_database	
t = Terminal()

import os

class Table():
	def __init__(self, tables, table):
		self.tables = tables
		self.table = table
		self.interface()

	def clearWindow(self):
		'''Clears the console window'''
		os.system('cls' if os.name == 'nt' else 'clear')

	def registerTable(self):
		'''Registers people to the new table'''
		option = int(input(t.bold("How many persons do you want to register in the table? ")))
		max_people = int(self.table["persons"])

		if(option > max_people):
			print "Table can't have more than " + t.bold(self.table["persons"]) + " persons."
		elif(option < 1):
			print "The number needs to be bigger than 0"
		else:
			self.tables.update({"_id" : self.table['_id'] },{'$set' : {"numPeople": 10}})
			print "Registered the people"

	def interface(self):
		self.clearWindow()
		print "Table interface of table " + self.table["num"]
		anotherCommand = True
		while(anotherCommand):
			print "What do you want to do?"
			print t.blink(t.bold("(1)")), "Register new people"
			print t.blink(t.bold("(2)")), "Register new order"
			print t.blink(t.bold("(3)")), "Change order"
			print t.blink(t.bold("(4)")), "Get account"
			print t.blink(t.bold("(4)")), "Close account."
			print t.blink(t.red("(6)")), "Exit order interface"
			option = input(t.bold("1|2|3|4|5|6 "))
			if(option == 1):
				self.registerTable()
			elif(option == 6):
				anotherCommand = False
			else:
				self.clearWindow()
				print "I did not understand you. Please just write the number"


