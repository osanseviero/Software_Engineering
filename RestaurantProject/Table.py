from config import *

class Table():
	def __init__(self, table):
		self.table = table
		self.interface()

	def registerPeople(self):
		'''Registers people to the new table'''
		option = int(input(t.bold("How many persons do you want to register in the table? ")))
		max_people = int(self.table["persons"])

		if(option > max_people):
			print "This table can't have more than " + t.bold(str(self.table["persons"])) + " persons."
		elif(option < 1):
			print "The number needs to be bigger than 0"
		else:
			helper.getTables().update({"_id" : self.table['_id'] },{'$set' : {"numPeople": option, "check" : "open"}})
			print "Registered " + str(option) +  " people"


	def closeCheck(self):
		helper.clearWindow()
		"""Conseguir precio final de todas las ordenes"""
		helper.getTables().update({"_id" : self.table['_id'] },{'$set' : {"numPeople": 0,"order" : [], "check" : "closed"}})
		print self.table["order"]
		print str(self.table["_id"]) + "'s check has been closed"

	def getCheck(self):
		helper.clearWindow()
		table = helper.findTableById(self.table["_id"])
		order = table["order"]
		totalPrice = 0
		for recipe in order:
			print "Product: " + recipe["name"] + "| price: " + str(recipe["price"])
			totalPrice += recipe["price"]

		print "The total price is " + str(totalPrice)
		option = raw_input(t.bold("Do you wish to split? [y/n]"))
		if(option == 'y'):
			people = table["numPeople"]
			print "Number of people: " + str(people)
			split = totalPrice/float(people)
			print "The account will be split into " + str(split)




	def interface(self):
		helper.clearWindow()
		anotherCommand = True
		madeCheck = False
		if(self.table["numPeople"] == 0 or self.table["check"] == "closed"):
			people = False
		else:
			people = True
		while(anotherCommand):
			while(people):
				if(self.table["numPeople"] == 0 or self.table["check"] == "closed"):
					people = False
					break
				print "Table interface of table " + str(self.table["num"])
				print "What do you want to do?"
				print t.blink(t.bold("(1)")), "Order products"
				print t.blink(t.bold("(2)")), "Get check"
				print t.blink(t.bold("(3)")), "Close check"
				print t.blink(t.red("(4)")), "Exit order interface"
				option = raw_input(t.bold("1|2|3|4|5 "))
				if(option == '1'):
					order.newOrder(self.table['_id'])
				elif(option == '2'):
					self.getCheck()
					madeCheck = True
				elif(option == '3'):
					if(madeCheck == True):
						self.closeCheck()
						people = False
					else:
						helper.clearWindow()
						print "First you must get check"
				elif(option == '4'):
					helper.clearWindow()
					anotherCommand = False
					break
				else:
					helper.clearWindow()
					print "I did not understand you. Please just write the number"
			while(people !=  True):
				print "Table interface of table " + str(self.table["num"])
				print "What do you want to do?"
				print t.blink(t.bold("(1)")), "Register new people"
				print t.blink(t.red("(2)")), "Exit order interface"
				option = raw_input(t.bold("1|2"))
				if(option == '1'):
					helper.clearWindow()
					self.registerPeople()
					if(self.table["numPeople"] > 0):
						people = True

					break
				elif(option == '2'):
					helper.clearWindow()
					anotherCommand = False
					break
				else:
					helper.clearWindow()
					print "I did not understand you. Please just write the number"

	'''def interfaceWithoutPeople(self):'''
