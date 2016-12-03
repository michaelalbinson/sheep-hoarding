from pygame import image
from random import random
from util import randomDroneStartingPosition, setPos, TIME, magnitude, directionalVector

droneImg = image.load("drone.gif")

class Drone():

	def __init__(self, numSheep):
		self.position = randomDroneStartingPosition()
		self.numberOfSheep = numSheep
		self.detectionRadius = 200
		self.speed = 4
		self.avoidanceRadius = 50
		self.image = droneImg
		self.allCreatures = {}
		self._pos = (self.position["x"], self.position["y"])

	def setCreatures(self, creatures):
		self.allCreatures = creatures;

	def findThings(self):
		tooClose = list()
		for elem in self.allCreatures:
			for i in self.allCreatures[elem]:
				mag = magnitude(i.position, self.position)
				if (elem == "Tree" and mag < self.detectionRadius + self.avoidanceRadius):
					tooClose.append((i, mag))
				elif (elem != "Tree" and mag < self.detectionRadius):
					tooClose.append((i, mag))

		return tooClose

	def determineMostImportant(self, thingsFound):
		mostImportant = [0, 0, 200]
		for elem in thingsFound:
			if (type(elem) is "Tree.Tree" and elem[1] < mostImportant[2]):
				mostImportant[0] = elem[0]
				mostImportant[1] = "Tree"
				mostImportant[2] = elem[1]
			elif (type(elem) is "Wolf.Wolf" and elem[1] < mostImportant[2] and mostImportant[1] != "Tree.Tree"):
				mostImportant[0] = elem[0]
				mostImportant[1] = "Wolf"
				mostImportant[2] = elem[1]
			elif (type(elem) is "Sheep.Sheep" and elem[1] < mostImportant[2] and (mostImportant[1] != "Tree.Tree" and mostImportant[1] != "Wolf.Wolf")):
				mostImportant[0] = elem[0]
				mostImportant[1] = "Sheep"
				mostImportant[2] = elem[1]
			elif (type(elem) is "Drone.Drone" and elem[1] < mostImportant[2] and (mostImportant[1] != "Tree.Tree" and mostImportant[1] != "Wolf.Wolf" and mostImportant[1] != "Sheep.Sheep")):
				mostImportant[0] = elem[0]
				mostImportant[1] = "Drone"
				mostImportant[2] = elem[1]

		return mostImportant

	def alert(self, wolf):
		pass

	def react(self, mostImportant):
		if (type(mostImportant[0]) is int):
			self.move([random(), random()])
			return

		if (mostImportant[1] == "Tree"):
			self.move(directionalVector(mostImportant[0].position, self.position, op=-1))
		elif(mostImportant[1] == "Wolf"):
			self.move(directionalVector(mostImportant[0].position, self.position, op=-1))
			self.alert(mostImportant[0])
		elif(mostImportant[1] == "Sheep"):
			if (mostImportant[2] < 5):
				self.move([0, 0])
			else:
				self.move(directionalVector(mostImportant[0].position, self.position))
		else:
			if(mostImportant[2] < 15):
				self.move(directionalVector(mostImportant[0].position, self.position, op=-1))
			else:
				self.move(directionalVector(mostImportant[0].position, self.position))

	def scan(self):
		thingsFound = self.findThings()

		if (thingsFound == []):
			self.move([0, 0])
			return

		mostImportant = self.determineMostImportant(thingsFound);

		self.react(mostImportant)


	def move(self, direction):
		self.position["x"] = direction[0]*self.speed*TIME + self.position["x"]
		self.position["y"] = direction[1]*self.speed*TIME + self.position["y"]
		self._pos = setPos(self.position)

	def updatePosition(self):
		self.scan()