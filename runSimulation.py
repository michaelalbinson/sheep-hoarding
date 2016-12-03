import pygame, sys, Tree, Drone, Sheep, Wolf

size = width, height = 1400, 700
speed = [2, 2]
color = 0, 255, 0
screen = pygame.display.set_mode(size)

num_trees = 0
num_sheep = 0
num_wolves = 0
num_drones = 0


def startSim(criteria):
	pass

def getObjects():
	trees = set()
	sheep = set()
	wolves = set()
	drones = set()

	for i in range(num_trees):
		trees.add(Tree.Tree())

	for i in range(num_drones):
		drones.add(Drone.Drone(num_sheep))

	for i in range(num_wolves):
		if (i == num_wolves-1):
			wolves.add(Wolf.Wolf(True))
		else:
			wolves.add(Wolf.Wolf(False))

	for i in range(num_sheep):
		if (i == num_sheep-1):
			sheep.add(Sheep.Sheep(True))
		else:
			sheep.add(Sheep.Sheep(False))

	return {"trees": trees, "sheep": sheep, "wolves": wolves, "drones": drones}


def start(trees, sheep, wolves, drones):
	global num_trees, num_sheep, num_wolves, num_drones
	num_trees = trees
	num_sheep = sheep
	num_wolves = wolves
	num_drones = drones
	criteria = getObjects()
	startSim(criteria)


while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]

	# screen.fill(color)
	# screen.blit(sheep, ballrect)
	# pygame.display.flip()
