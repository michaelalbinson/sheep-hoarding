from pygame import image
from util import randomPosition
from math import pow


sheep = image.load("small-sheep.gif")
leaderSheep = image.load("leaderSheep.gif")

class Sheep():

	def __init__(self, isLeader):
		self.isLeader = isLeader
		self.position = randomPosition()
		self.detectionRadius = 1
		self.speed = 3;
		self.neighbor = none
		self.velocity = [0, 0]
		self.allCreatures = {}
		self._pos = (self.position["x"], self.position["y"])
		if (isLeader):
			self.image = leaderSheep.convert()
		else:
			self.image = sheep.convert()
		self.imRect = self.image.get_rect()


	def detectDrone(self):
		### dectect if DRONE is in range
        if self.allCreatures == {}:
            return
        for drone in self.allCreatures["drones"]:
            closest_drone_dist = 6000
            temp_drone = drone
            temp_drone_dist = pow((pow(temp_drone.position["x"]-self.position["x"], 2))+(pow(drone.position["y"]-self.position,2)), 0.5)
            if(closest_drone_dist > temp_drone_dist):
                closest_drone = temp_drone ## finds the closest drone to sheep
		if (pow((pow(closest_drone.position["x"]-self.position["x"], 2))+pow(closest_drone.position["y"]-self.position,2), 0.5) < self.detectionRadius:
			temp_vector = [-(closest_drone.position["x"]-self.position["x"]), -(closest_drone.position["y"] - self.position["y"])]
		else:
			temp_vector = [0, 0]
		return temp_vector

	def setCreatures(self, creatures):
		self.allCreatures = creatures;

	def detectWolf(self):
		## need to detect if a wolf is close enough and use that instead of WOLF
        if self.allCreatures = {}:
            return
        for wolf in self.allCreatures["wolves"]:
            closest_wolf_dist = 6000
            temp_wolf = wolf
            temp_wolf_dist = pow((pow(temp_wolf.position["x"]- self.position["x"], 2) + pow(temp_wolf.position["y"] - self.position["y"],2)), 0.5)
            if(closest_wolf_dist> temp_wolf_dist):
                closest_wolf = temp_wolf
            
		if (pow((pow(closest_wolf.position["x"]-self.position["x"], 2)+pow(closest_wolf.position["y"]-self.position,2)), 0.5)) < self.detectionRadius:
			temp_vector = [-(closest_wolf.position["x"]-self.position["x"]), -(closest_wolf.position["y"] - self.position["y"])]
		else:
			temp_vector = [0, 0]
            
		return temp_vector

	def findNeighbor(self):
		if self.allCreatures = {}:
            return
            
        for sheep in self.allCreatures["sheep"]:
            if sheep == self:
                continue
            else:
                closest_sheep_dist_1 = 6000
                closest_sheep_dist_2 = 6000
                temp_sheep = sheep
                temp_sheep_dist = pow((pow(temp_sheep.position["x"]- self.position["x"], 2) + pow(temp_sheep.position["y"] - self.position["y"],2)), 0.5)
                if(closest_sheep_dist2 > temp_sheep_dist and closest_sheep_dist_1 > temp_wolf_dist):
                        closest_sheep_1 = temp_sheep
                    else:
                        closest_sheep_2 = temp_sheep
            
        return self.neighbor = [closest_sheep_1, closest_sheep_2]
            
	def followNeighbor(self):
		self.findNeighbor()
        if self.neighbor[0].velocity != [0, 0]:
            return self.neighbor[0].velocity/speed
        else:
            return [0,0]


	def move_sheep(self, temp_vector):
		self.velocity = [temp_vector[0]*self.speed, temp_vector[1]*self.speed]
        self.position = [self.position["x"] + self.velocity[0]*TIME, self.position["y"] + self.velocity[0]*TIME]

            
    def updatePosition(self):
        i = 0
        if(self.detectWolf == [0,0])
        move_sheep(self, self.detectWolf())
        move_sheep(self, self.detectDrone())
        followNeighbor(self)
            
            
            
            
            
            
