from config import *	

def selectRecipe(tableId):
	name = ''
	table = helper.findTableById(tableId)
	order = table["order"]

	while(name != 'e'):
		name = raw_input("What's the name of the product? Press s to save. Press e to exit. ").lower()
		recipe = helper.findRecipe(name)
		if name != 'e':
			if(name == 's'):
				print "Sent the orders."
				for recipe in order:
					helper.getRecipes().update({"_id" : recipe['_id'] },{'$inc' : {"pop": 1}})
				helper.getTables().update({"_id" : tableId },{'$set' : {"order": order}})
				name = 'e'
			elif recipe == None:
				print t.red("Recipe was not found")
			else:
				print recipe['name'], " was added to the order."
				order.append(recipe)
				print "Current order: "
				for recipe in order:
					print recipe["name"]

def newOrder(tableId):
	helper.clearWindow()
	print "Register the new order"
	anotherCommand = True
	while(anotherCommand):
		print "What do you want to do?"
		print t.blink(t.bold("(1)")), "Select dishes."
		print t.blink(t.bold("(2)")), "Select drinks."
		print t.blink(t.bold("(3)")), "Exit order interface"
		option = raw_input(t.bold("1|2|3 "))
		if(option == '1'):
			helper.clearWindow()
			helper.printRecipes()
			selectRecipe(tableId)
		elif(option == '2'):
			helper.clearWindow()
			helper.printDrinks()
			selectRecipe(tableId)
		elif(option == '3'):
			helper.clearWindow()
			anotherCommand = False
		else:
			helper.clearWindow()
			print "I did not understand you. Please just write the number"