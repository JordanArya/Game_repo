import pygame
from pygame.sprite import Sprite

class Genangan(Sprite):
	def __init__(self,AlienGame):

		super().__init__()
		self.aliengame = AlienGame
		self.screen = AlienGame.screen
		self.settings = AlienGame.settings
		self.ship = AlienGame.ship
		self.oval_rect = pygame.Rect(0,0 ,self.settings.GENANG_WIDTH,self.settings.GENANG_HEIGHT)

	def draw_genang(self):
		pygame.draw.ellipse(self.screen,self.settings.RAIN_COLOUR,self.oval_rect,width=2)