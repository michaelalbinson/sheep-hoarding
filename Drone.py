from pygame import image
from random import random, randint
from util import randomDroneStartingPosition, setPos, TIME, magnitude, directionalVector

droneImg = image.load("drone.gif")

class Drone():

	def __init__(self, numSheep):
		self.position = randomDroneStartingPosition()
		self.numberOfSheep = numSheep
		self.detectionRadius = 300
		self.speed = 20
		self.avoidanceRadius = 20
		self.image = droneImg
		self._class = "Drone"
		self.allCreatures = {}
		self.randDirection = [0, 0]
		self.randCount = 11
		self._pos = (self.position["x"], self.position["y"])

	def setCreatures(self, creatures):
		self.allCreatures = creatures;

	def generateRandomDirection(self):
		next_direction = [0.5,-0.5]
		next_x = randint(0, 10)
		next_y = randint(0, 10)
		mag = magnitude({"x": next_x, "y": next_y}, self.position)
		if (mag == 0):
			return [0, 0]

		next_direction[0] = next_x/mag
		next_direction[1] = next_y/mag
		return next_direction

	def findThings(self):
		tooClose = list()
		for elem in self.allCreatures:
			for i in self.allCreatures[elem]:
				mag = magnitude(i.position, self.position)
				if (elem != "Tree" and mag < self.detectionRadius):
					tooClose.append((i, mag))

		return tooClose

	def determineMostImportant(self, thingsFound):
		mostImportant = [0, 0, self.detectionRadius]


		for elem in thingsFound:
			if (elem[1] == 0):
				continue

			if (elem[0]._class is "Drone" and elem[1] < mostImportant[2] and mostImportant[1] != "Wolf"):
				mostImportant[0] = elem[0]
				mostImportant[1] = "Drone"
				mostImportant[2] = elem[1]
				print("most", mostImportant[2])
			elif (elem[0]._class is "Sheep" and elem[1] < mostImportant[2] and mostImportant[1] != "Wolf" and mostImportant[1] != "Drone"):
				mostImportant[0] = elem[0]
				mostImportant[1] = "Sheep"
				mostImportant[2] = elem[1]
			elif (elem[0]._class is "Wolf" and elem[1] < mostImportant[2]):
				mostImportant[0] = elem[0]
				mostImportant[1] = "Wolf"
				mostImportant[2] = elem[1]

		return mostImportant

	def alert(self, wolf):
		# wolf.alerted = True
		# wolf.alertCount = 0
		pass

	def react(self, mostImportant):
		if (type(mostImportant[0]) is int):
			self.move([random(), random()])
			return


		if (mostImportant[1] == "Drone"):
			if (mostImportant[2] > 200):
				self.move(self.generateRandomDirection())
			else:
				self.move(directionalVector(mostImportant[0].position, self.position, -1))
		elif(mostImportant[1] == "Sheep"):
			if (mostImportant[2] < 100):
				self.move(self.generateRandomDirection())
			else:
				self.move(directionalVector(mostImportant[0].position, self.position, 1))
		else:
			dir = self.generateRandomDirection()
			self.move(dir)


	def scan(self):
		thingsFound = self.findThings()

		if (thingsFound == []):
			self.move(self.generateRandomDirection())
			return

		mostImportant = self.determineMostImportant(thingsFound);

		self.react(mostImportant)


	def move(self, direction):
		self.position["x"] = direction[0]*self.speed*TIME + self.position["x"]
		self.position["y"] = direction[1]*self.speed*TIME + self.position["y"]
		self._pos = setPos(self.position)

	def updatePosition(self):
		self.scan()