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
		self.speed = 20;
		self.allCreatures = {}
		self._pos = (self.position["x"], self.position["y"])
		self.temp_position_picked = 0
		self.random_next_pos = [0, 0]
		self._class = "Wolf"
		if(isAlpha):
			self.image = alphaWolf.convert()
		else:
			self.image = wolf.convert()

	def setCreatures(self, creature):
		self.allCreatures = creature

	def detectObject(self, creature):
		if self.allCreatures == {}:
			return

		closest_object_dist = 200000
		closest_object = None
		for animal in self.allCreatures[creature]:
			temp_magnitude = magnitude(animal.position, self.position)

			if(temp_magnitude < closest_object_dist):
				closest_object = animal
				closest_object_dist = temp_magnitude


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
		closest_drone = self.detectObject("drones")
		mag = magnitude(closest_drone.position, self.position)

		if (mag < self.detectionRadius):
			temp = directionalVector(closest_drone.position, self.position, -1)
		else:
			temp = [0, 0]

		return temp
	
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
		v = self.findLeader(self.findLeaderPos())
		self.move_pack(v)
		   
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
			if (self.isDronePresent() != [0, 0]):
				self.move_pack(self.isDronePresent())
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
			self.followLeader()
				

		   
		   
