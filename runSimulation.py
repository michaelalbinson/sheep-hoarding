import pygame, random, sys

size = width, height = 1400, 700
speed = [2, 2]
color = 0, 255, 0
screen = pygame.display.set_mode(size)

def randomPosition():
	x = random.randint(0+20, width-20)
	y = random.randint(0+20, height-20)
	return (x,y)


def setup():
	pass

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]

	screen.fill(color)
	screen.blit(sheep, ballrect)
	pygame.display.flip()
