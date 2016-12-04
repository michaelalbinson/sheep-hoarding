from random import randint
from math import pow, sqrt

TIME = 0.1 #s/frame

def randomPosition():
	x = randint(50, 1200)
	y = randint(50, 600)
	return {"x": x, "y": y}

def randomWolfStartingPosition():
	x = randint(-100, -20)
	y = randint(-100, -20)
	return {"x": x, "y": y}

def randomDroneStartingPosition():
	x = randint(400, 800)
	y = randint(100, 500)
	return {"x": x, "y": y}

def setPos(position):
	return (int(position["x"]), int(position["y"]))

def magnitude(v1, v2):
	mag_x = int(v1["x"]) - int(v2["x"])
	mag_y = int(v1["y"]) - int(v2["y"])
	total_magnitude = sqrt(pow(mag_x, 2) + pow(mag_y, 2))
	return total_magnitude


def directionalVector(v1, v2, op):
	mag_x = int(v1["x"]) - int(v2["x"])
	mag_y = int(v1["y"]) - int(v2["y"])
	total_magnitude = sqrt(pow(mag_x, 2) + pow(mag_y, 2))
	if (total_magnitude == 0):
		return [0, 0]

	temp_v = [0,0]
	temp_v[0] = op*mag_x/total_magnitude
	temp_v[1] = op*mag_y/total_magnitude
	return temp_v