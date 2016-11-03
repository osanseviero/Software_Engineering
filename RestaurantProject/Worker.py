import os

class WorkerManager:
	'API to interact with workers'

	def __init__(self, collection):
		self.workers = collection

	def clearWindow(self):
		'''Clears the console window'''
		os.system('cls' if os.name == 'nt' else 'clear')

	def createWorker(self, user, name, lastname, password, salary):
		newWorker = {"user" : user, "name" : name, "lastname": lastname, "password": sha256_crypt.encrypt(password), "salary" : salary}
		self.workers.insert(newWorker)
		print "Saved worker with username " , user

	def count(self):
		print "Total workers: ", self.workers.count()

	def printWorkers(self):
		for worker in self.workers.find():
			print worker

	def clearUsers(self):
		db.drop_collection(self.workers)

	def findUser(self, username):
		return self.workers.find_one({"user": username})

	def checkPassword(self, username, password):
		hash = self.workers.find_one({"user": username})["password"]
		return sha256_crypt.verify(password, hash)

'''
wm = WorkerManager(db.workers)
wm.clearUsers()
wm.createWorker("osanseviero", "osan", "seviero", "hello", 182)
wm.createWorker("testuser", "test", "lastname", "world", 20)
wm.count()
wm.printWorkers()
print wm.checkPassword("osanseviero", "hello")
print wm.checkPassword("osanseviero", "hell")
'''