from pygame import image


sheep = image.load("small-sheep.gif")
leaderSheep = image.load("leaderSheep.gif")

class Sheep():

	def __init__(self, isLeader, startingPosition):
		self.isLeader = isLeader
		self.position = startingPosition
		self.detectionRadius = 1
		self.speed = 3;
		if (isLeader):
			self.image = leaderSheep.convert()
		else:
			self.image = sheep.convert()

		self.

	def detectDrone(self):
		pass

	def detectWolf(self):
		pass

	def followNeighbor(self, neighborPos):
		pass

	def move(self):
		pass

