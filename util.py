from random import randint

def randomPosition():
	x = randint(50, 1300)
	y = randint(50, 600)
	return {"x": x, "y": y}

def randomWolfStartingPosition():
	x = randint(50, 500)
	y = randint(50, 500)
	return {"x": x, "y": y}