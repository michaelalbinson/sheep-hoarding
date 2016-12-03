from pygame import image
from util import randomWolfStartingPosition, setPos, TIME, directionalVector
from math import pow, sqrt

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

	def setCreatures(self, creature):
		self.allCreatures = creature;

	def detectObject(self, creature):
		if self.allCreatures == {}:
			return
		
		for object in self.allCreatures[creature]:
			closest_object_dist = 6000
			temp_object = creature
			temp_object_dist_x = pow(temp_object.position["x"]- self.position["x"], 2)
			temp_object_dist_y = pow(temp_object.position["y"]- self.position["y"], 2)
			temp_object_dist = sqrt(temp_object_dist_x +temp_object_dist_y)

			if(closest_object_dist > temp_object_dist):
				closest_object = temp_object

		return closest_object
	
	def isSheepPresent(self):
		closest_sheep = self.detectObject(, "sheep")
		closest_sheep_x = pow(closest_sheep.position[x], 2)
		closest_sheep_y = pow(closest_sheep.position[y], 2)
		
		if(sqrt(closest_sheep_x + closest_sheep_y) < self.detectionRadius:
		   closest_sheep_x_dist = closest_sheep.position["x"] - self.position["x"]
		   closest_sheep_y_dist = closest_sheep.position["y"] - self.position["y"]
		   temp_vector = [closest_sheep_x_dist, closest_sheep_y_dist]
		else:
		   temp_vector = [0,0]
		   
		return temp_vector
		   
	def isDronePresent(self):
		closest_drones = self.detectObject(, "drones")
		closest_sheep_x = pow(closest_sheep.position[x], 2)
		closest_sheep_y = pow(closest_sheep.position[y], 2)
		   
		if(sqrt( closest_sheep_x + closest_sheep_y) < self.detectionRadius:
			closest_sheep_x_dist = closest_sheep.position["x"] - self.position["x"]
			closest_sheep_y_dist = closest_sheep.position["y"] - self.position["y"]
			temp_vector = [closest_sheep_x_dist, closest_sheep_y_dist]
		else:
			temp_vector = [0,0]
		   
		return temp_vector
	
	def findLeaderPos():
		if self.allCreatures = {}:
			return
		for object in self.allCreatures[creature]:
		   if self.isAlpha:
				return self.position
		   
	def findLeader(self, leaderPos):
		if self.allCreatures == {}:
		   return
		if leaderPos["x"]== self.position["x"] and leaderPos["y"] == self.position["y"]:
		   return [0,0]
		else:
		   return directionalVector(leaderPos, self.position)
		   
	def followLeader(self):
		return self.findLeader(, findLeaderPos())
		   
	def move_pack(self, temp_vector):
		self.position["x"] = self.position["x"] + self.speed*TIME*temp_vector[0]
		self.position["y"] = self.position["y"] + self.speed*TIME*temp_vector[1]
		self._pos = setPos(self.position)
		   
	def updatePosition(self):
		if (self.isAlpha):
		   if(isSheepPresent(self) == [0,0]):
				random_next_pos["x"] = randint(0, 1400)
				random_next_pos["y"] = randint(0, 700)
				move_pack(self, random_next_pos)
		   else:
				move_pack(self, isSheepPresent(self))
		
		else:
		   if(isSheepPresent(self) == [0,0]):
				followLeader(self)
		   else:
				move_pack(self, isSheepPresent(self))
				
		   
		   
		   
		   
		   
		   
		   
		   
		   
		   
		   
		   
		   
		   
		   
		   
