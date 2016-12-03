from pygame import image
from util import randomWolfStartingPosition, setPos, TIME

wolf = image.load("wolf.gif")
alphaWolf = image.load("alpha-wolf.gif")

class Wolf():

	def __init__(self, isAlpha):
		self.isAlpha = isAlpha
		self.position = randomWolfStartingPosition()
		self.detectionRadius = 20;
		self.slowSpeed = 7;
		self.fastSpeed = 10;
		self.allCreatures = {}
		self._pos = (self.position["x"], self.position["y"])
		if(isAlpha):
			self.image = alphaWolf.convert()
		else:
			self.image = wolf.convert()

	def setCreatures(self, creatures):
		self.allCreatures = creatures;

	def isSheepPresent(self):
		pass

	def isDronePresent(self):
		pass

	def findLeader(self, leaderPos):
		pass

	def followLeader(self):
		pass

	def move(self):
		pass

	def updatePosition(self):
		pass