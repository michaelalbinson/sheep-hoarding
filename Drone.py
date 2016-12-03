from pygame import image
from util import randomPosition

sheep = image.load("drone.gif")

class Drone():

	def __init__(self, numSheep):
		self.position = randomPosition()
		self.numberOfSheep = numSheep
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