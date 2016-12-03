class Drone():

	def __init__(self, startingPosition, numberOfSheep):
		self.position = startingPosition
		self.numberOfSheep = numberOfSheep
		self.detectionRadius = 10
		self.speed = 10;
		pass

	def scan(self):
		self.findThings()

	def findThings(self):
		pass #find and identify things

	def identify(self, obj):
		pass

	def move(self):
		pass