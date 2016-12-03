from random import randint

def randomPosition():
	x = randint(20, 1380)
	y = randint(20, 680)
	return {"x": x, "y": y}

def randomWolfStartingPosition():
	x = randint(-40, -10)
	y = randint(-40, -10)
	return {"x": x, "y": y}