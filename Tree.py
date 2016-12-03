from pygame import image
from util import randomPosition

tree = image.load("tree.gif")

class Tree():
	def __init__(self):
		self.position = randomPosition()
		self.image = tree.convert()
		self.rect = self.image.get_rect()
		self._pos = (self.position["x"], self.position["y"])