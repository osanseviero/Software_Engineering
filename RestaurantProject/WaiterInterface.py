from config import *

class Waiter():
	max_tables = 10

	def __init__(self):
		helper.clearWindow()
		self.interface()

	def printTables(self):
		'''Prints all the tables in document format'''
		helper.clearWindow()
		if(helper.getTables().count() == 0):
			print "There are no recipes"
		else:
			print t.bold("List of Tables")
			for table in helper.getTables().find():
				if(helper.getTables()['numPeople'] == None):
					print "Table " + table['num'] + " | It has no people."
				else:
					print "Table " + str(table['num']) + " | It has " + str(table['numPeople']) + " persons."

	def selectTable(self):
		helper.clearWindow()
		self.printTables()
		tableid = raw_input("Write the table number: ")

		if(tableid.isalpha()):
			helper.clearWindow()
			print "Sorry, you've entered an invalid character"
		else:
			table = helper.findTable(int(tableid))
			if(not table):
				print "Table was not found"
			else:
				Table.Table(table)

	def interface(self):
		anotherCommand = True
		while(anotherCommand):
			print "What do you want to do?"
			print t.blink(t.bold("(1)")), "List all recipes"
			print t.blink(t.bold("(2)")), "List all drinks"
			print t.blink(t.bold("(3)")), "List all tables"
			print t.blink(t.bold("(4)")), "Select table"
			print t.blink(t.red("(5)")), "Exit waiter interface"
			option = raw_input(t.bold("1|2|3|4|5 "))
			if(option == '1'):
				helper.printRecipes()
			elif(option == '2'):
				helper.printDrinks()
			elif(option == '3'):
				self.printTables()
			elif(option == '4'):
				self.selectTable()
			elif(option == '5'):
				anotherCommand = False
			else:
				helper.clearWindow()
				print "I did not understand you. Please just write the number"

