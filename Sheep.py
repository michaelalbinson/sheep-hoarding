from pygame import image
from util import randomPosition, TIME, setPos
from math import pow


sheep = image.load("small-sheep.gif")
leaderSheep = image.load("leaderSheep.gif")

class Sheep():

	def __init__(self, isLeader):
		self.isLeader = isLeader
		self.position = randomPosition()
		self.detectionRadius = 1
		self.speed = 3;
		self.neighbor = None
		self.velocity = [0, 0]
		self.allCreatures = {}
		self._pos = (self.position["x"], self.position["y"])
		if (isLeader):
			self.image = leaderSheep.convert()
		else:
			self.image = sheep.convert()


	def detectDrone(self):
		### detect if drone is in range
		if self.allCreatures == {}:
			return
		for drone in self.allCreatures["drones"]:
			closest_drone_dist = 6000
			temp_drone = drone
			temp_drone_dist = pow(((pow(temp_drone.position["x"] - self.position["x"], 2)) + (pow(drone.position["y"] - self.position["y"], 2))), 0.5)
			if(closest_drone_dist > temp_drone_dist):
				closest_drone = temp_drone ## finds the closest drone to sheep
		if ((pow(pow(closest_drone.position["x"] - self.position["x"], 2) + pow(closest_drone.position["y"] - self.position["y"], 2), 0.5)) < self.detectionRadius):
			temp_vector = [-(closest_drone.position["x"]-self.position["x"]), - (closest_drone.position["y"] - self.position["y"])]
		else:
			temp_vector = [0, 0]
		return temp_vector

	def setCreatures(self, creatures):
		self.allCreatures = creatures;

	def detectWolf(self):
		## need to detect if a wolf is close enough and use that instead of WOLF
		if self.allCreatures == {}:
			return
		for wolf in self.allCreatures["wolves"]:
			closest_wolf_dist = 6000
			temp_wolf = wolf
			temp_wolf_dist = pow((pow(int(temp_wolf.position["x"]) - int(self.position["x"]), 2) + pow(int(temp_wolf.position["y"]) - int(self.position["y"]), 2)), 0.5)
			if(closest_wolf_dist> temp_wolf_dist):
				closest_wolf = temp_wolf
            
		if ((pow(pow(closest_wolf.position["x"] - self.position["x"], 2) + pow(closest_wolf.position["y"] - self.position["y"], 2), 0.5)) < self.detectionRadius):
			temp_vector = [-(closest_wolf.position["x"]-self.position["x"]), -(closest_wolf.position["y"] - self.position["y"])]
		else:
			temp_vector = [0, 0]
            
		return temp_vector

	def findNeighbor(self):
		if self.allCreatures == {}:
			return

		for sheep in self.allCreatures["sheep"]:
			if sheep == self:
				continue
			else:
				closest_sheep_dist_1 = 6000
				closest_sheep_dist_2 = 6000
				temp_sheep = sheep
				closestSheep = None
				temp_sheep_dist = pow((pow(temp_sheep.position["x"] - self.position["x"], 2) + pow(temp_sheep.position["y"] - self.position["y"],2)), 0.5)

				if(closest_sheep_dist_2 > temp_sheep_dist and closest_sheep_dist_1 > temp_sheep_dist):
					closestSheep = temp_sheep
				else:
					closestSheep = temp_sheep

		self.neighbor = closestSheep

	def followNeighbor(self):
		self.findNeighbor()
		x_mag =  int(self.neighbor.position["x"]) - int(self.position["x"])
		y_mag = int(self.neighbor.position["y"]) - int(self.position["y"])
		total_magnitude = pow((pow(x_mag, 2) + pow(y_mag, 2)), .5)
		if (total_magnitude == 0):
			return [0, 0]
		directional_vector = [0, 0]
		directional_vector[0] = x_mag/total_magnitude
		directional_vector[1] = y_mag/total_magnitude
		return directional_vector


	def move_sheep(self, temp_vector):
		self.position["x"] = self.position["x"] + self.speed*TIME*temp_vector[0]
		self.position["y"] = self.position["y"] + self.speed*TIME*temp_vector[1]
		self._pos = setPos(self.position)

            
	def updatePosition(self):
		i = self.detectWolf()
		if (i != [0, 0]):
			self.move_sheep(i)
			return


		i = self.detectDrone()
		if (i != [0, 0]):
			self.move_sheep(i)
			return

		self.move_sheep(self.followNeighbor())
            
            
            
            
            
            
