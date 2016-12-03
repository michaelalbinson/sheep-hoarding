from pygame import image
from util import randomDroneStartingPosition, setPos, TIME

droneImg = image.load("drone.gif")

class Drone():

	def __init__(self, numSheep):
		self.position = randomDroneStartingPosition()
		self.numberOfSheep = numSheep
		self.detectionRadius = 10
		self.speed = 10
		self.avoidanceRadius = 50
		self.image = droneImg
		self.allCreatures = {}
		self._pos = (self.position["x"], self.position["y"])

	def setCreatures(self, creatures):
		self.allCreatures = creatures;

	def scan(self):
		self.findThings()

	def findThings(self):
		pass #find and identify things

	def identify(self, obj):
		pass

	def move(self):
		pass

	def updatePosition(self):
		pass