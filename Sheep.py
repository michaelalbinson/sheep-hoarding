from pygame import image
<<<<<<< Updated upstream
from util import randomPosition
=======
import math import pow

>>>>>>> Stashed changes

sheep = image.load("small-sheep.gif")
leaderSheep = image.load("leaderSheep.gif")

class Sheep():

	def __init__(self, isLeader, drones, wolves):
		self.isLeader = isLeader
		self.position = randomPosition()
		self.detectionRadius = 1
		self.speed = 3;
		self.neighbor = [0, 0]
		self.velocity = [0, 0]
		self.allCreatures = {}
		if (isLeader):
			self.image = leaderSheep.convert()
		else:
			self.image = sheep.convert()
		self.imRect = self.image.imageRect()


	def detectDrone(self):
		### dectect if DRONE is in range

		if (pow((pow(Drone.position[x]-self.position[x], 2))+pow(Drone.position[y]-self.position, 0.5))) < self.detectionRadius:
			temp_vector = [-(Drone.position[x]-self.position[x]), -(Drone.position[y] - self.position[y])]
		else:
			temp_vector = [0, 0]

		return temp_vector

	def update(self, creatures):
		self.allCreatures = creatures;

	def detectWolf(self):
		## need to detect if a wolf is close enough and use that instead of WOLF


		if (pow((pow(Wolf.position[x]-self.position[x], 2))+pow(Wolf.position[y]-self.position, 0.5))) < self.detectionRadius:
			temp_vector = [-(Wolf.position[x]-self.position[x]), -(Wolf.position[y] - self.position[y])]
		else:
			temp_vector = [0, 0]
		return temp_vector

	def findNeighbor(self):
		pass

	def followNeighbor(self):
		self.findNeighbor()


	def move(self, temp_vector):
		self.velocity = [temp_vector[0]*self.speed, temp_vector[1]*self.speed]
		pass

