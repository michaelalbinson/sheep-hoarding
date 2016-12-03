from pygame import image
from util import randomWolfStartingPosition, setPos, TIME, directionalVector, magnitude
from math import pow, sqrt
from random import randint

wolf = image.load("wolf.gif")
alphaWolf = image.load("alpha-wolf.gif")

class Wolf():
	
	def __init__(self, isAlpha):
		self.isAlpha = isAlpha
		self.position = randomWolfStartingPosition()
		self.detectionRadius = 500;
		self.speed = 30;
		self.allCreatures = {}
		self._pos = (self.position["x"], self.position["y"])
		self.temp_position_picked = 0
		self.random_next_pos = [0, 0]
		if(isAlpha):
			self.image = alphaWolf.convert()
		else:
			self.image = wolf.convert()

	def setCreatures(self, creature):
		self.allCreatures = creature

	def detectObject(self, creature):
		if self.allCreatures == {}:
			return

		for object in self.allCreatures[creature]:
			closest_object = None
			closest_object_dist = 2000
			temp_magnitude = magnitude(object.position, self.position)

			if(closest_object_dist < self.detectionRadius or temp_magnitude < closest_object_dist):
				closest_object = object


		return closest_object
	
	def isSheepPresent(self):
		closest_sheep = self.detectObject("sheep")

		mag = magnitude(closest_sheep.position, self.position)

		if(mag < self.detectionRadius):
			temp = directionalVector(closest_sheep.position, self.position, 1)
		else:
			temp = [0,0]
		   
		return temp
		   
	def isDronePresent(self):
		closest_drones = self.detectObject("drones")
		closest_sheep_x = pow(closest_drones.position["x"], 2)
		closest_sheep_y = pow(closest_drones.position["y"], 2)
		   
		if(sqrt( closest_sheep_x + closest_sheep_y) < self.detectionRadius):
			closest_sheep_x_dist = closest_drones.position["x"] - self.position["x"]
			closest_sheep_y_dist = closest_drones.position["y"] - self.position["y"]
			temp_vector = [closest_sheep_x_dist, closest_sheep_y_dist]
		else:
			temp_vector = [0,0]
		   
		return temp_vector
	
	def findLeaderPos(self):
		if (self.allCreatures == {}):
			return
		if self.isAlpha:
			return self.position

		for object in self.allCreatures["wolves"]:
			if (object.isAlpha):
				return object.position
		   
	def findLeader(self, leaderPos):
		if self.allCreatures == {}:
			return

		if self.isAlpha:
			return [0,0]
		else:
			return directionalVector(leaderPos, self.position, 1)
		   
	def followLeader(self):
		return self.findLeader(self.findLeaderPos())
		   
	def move_pack(self, temp_vector):
		self.position["x"] = self.position["x"] + self.speed*TIME*temp_vector[0]
		self.position["y"] = self.position["y"] + self.speed*TIME*temp_vector[1]
		self._pos = setPos(self.position)

	def generateRandomDirection(self):
		next_direction = [0, 0]
		next_x = randint(0, 1400)
		next_y = randint(0, 700)
		mag = magnitude({"x": next_x, "y": next_y}, self.position)
		if (mag == 0):
			return [0, 0]

		next_direction[0] = next_x/mag
		next_direction[1] = next_y/mag
		return next_direction


		   
	def updatePosition(self):
		if (self.isAlpha):
			if(self.isSheepPresent() == [0, 0]):
				if(self.temp_position_picked == 0):
					self.random_next_pos = self.generateRandomDirection()
					self.temp_position_picked = 1
					self.move_pack(self.random_next_pos)
				else:
					self.move_pack(self.random_next_pos)
			else:
				self.move_pack(self.isSheepPresent())
				self.temp_position_picked = 0
				self.random_next_pos = 0
		else:
			if(self.isSheepPresent() == [0,0]):
				self.followLeader()
			else:
				self.move_pack(self.isSheepPresent())
				

		   
		   
