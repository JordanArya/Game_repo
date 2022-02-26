import pygame 
from pygame.sprite import Sprite 
import random
#Punya sir Anas
class Raindrop(Sprite):

	def __init__(self,AlienGame):
		super().__init__()
		self.screen = AlienGame.screen
		self.settings = Aliengame.settings
		self.image = pygame.image.load("assets/raindrop.png")
		self.rect = self.image.get_rect()
		self.rect = pygame.transform.scale(self.image,(self.rect.width//50,self.rect.height//50))
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += self.settings.RAINDROP_SPEED
		self.check_bottom_screen()

	def check_bottom_screen(self):
		if self.rect.y >= self.settings.SCREEN_HEIGHT:
			self.rect.y  = random.randint(-self.settings.SCREEN_HEIGHT,-5)
			self.rect.x = random.randint(0,self.settings.SCREEN_WIDTH)