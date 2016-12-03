from random import randint

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
	x = randint(1200, 1300)
	y = randint(50, 200)
	return {"x": x, "y": y}

def setPos(position):
	return (int(position["x"]), int(position["y"]))