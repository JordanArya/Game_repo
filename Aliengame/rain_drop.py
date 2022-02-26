import pygame
from pygame.sprite import Sprite

class RainDrop(Sprite):
	def __init__(self,AlienGame):

		super().__init__()
		self.aliengame = AlienGame
		self.screen = AlienGame.screen
		self.settings = AlienGame.settings
		self.ship = AlienGame.ship
		

		self.rect = pygame.Rect(0,0 ,self.settings.RAIN_WIDTH,self.settings.RAIN_HEIGHT)
		#self.windy_rect = pygame.Rect(0,0,self.settings.RAIN_WIDTH,self.settings.RAIN_HEIGHT)
		#self.rect = pygame.transform.rotate(self.rect,-30)

	def draw(self):
		pygame.draw.ellipse(self.screen,self.settings.RAIN_COLOUR,self.rect,width=2)

	def draw_wind(self):
		pass

	def update(self):
		self.rect.y += self.settings.RAIN_SPEED
		
	def rain_continues(self):
		if self.rect.y == 30 :
			return True

	def check_edges(self):
		if self.rect.bottom >= self.settings.SCREEN_HEIGHT:
			return True
	
	def check_ship_touch(self):
		if self.rect.bottom-20 == (self.ship.rect.top-self.ship.rect.top % 3) and self.rect.x in range(self.ship.rect.x,self.ship.rect.x+self.ship.rect.width):
			return True

	def rain_changes(self):
		if self.rect.y % 60 == 0 and self.rect.y <= self.settings.SCREEN_HEIGHT - 150 and self.rect.y != 0:
			return True

	def change_draw(self,minus):
		self.rect =  pygame.Rect(0,0 ,(self.settings.RAIN_WIDTH - (minus)),self.settings.RAIN_HEIGHT )

	


		



