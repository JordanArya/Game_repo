import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

	def __init__(self,AlienGame):
		super().__init__()

		self.screen = AlienGame.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = AlienGame.settings
		self.image = pygame.image.load('Aliengame/assets/alien.png')
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image,(int(self.settings.Screen_width//30),int(self.settings.Screen_height//13.34)))
		self.rect = self.image.get_rect()
		

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

	def update(self):
		self.rect.x += self.settings.ALIEN_SPEED

	def drop(self):
		self.rect.y += self.settings.ALIEN_DROP
	def check_edges(self):
		if (self.rect.right >= self.screen_rect.right) or (self.rect.left <= 0):
			return True
	def check_bottom_edges(self):
		if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
			return True


