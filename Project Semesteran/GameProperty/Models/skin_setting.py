import pygame
#from GameProperty.main_game import MainGame
from GameProperty.Models.slime import Slime

class SkinSettings():
	def __init__(self,parrent):
		self.settings = parrent.settings
		self.my_screen = parrent.my_screen
		self.app = parrent
		self.slimes = pygame.sprite.Group()
		self.image_and_rect = []
		self.make_slime_picture()

	def make_slime_picture(self):
		for step in range(len(self.settings.STAND_SLIME_IMAGES)):
			slime = Slime(self.app)
			slime.image = pygame.image.load(self.settings.STAND_SLIME_IMAGES[step])
			slime.image = pygame.transform.scale(slime.image,(self.my_screen.rect.width//3,self.my_screen.rect.height//6))
			slime.rect = slime.image.get_rect()
			if step == 0:
				slime.rect.midtop = self.my_screen.rect.midtop
				slime.rect.x +=  step*slime.rect.width 
			elif step <= 2:
				slime.rect.midleft = self.my_screen.rect.midleft
			else:
				slime.rect.bottomleft = self.my_screen.rect.bottomleft
				slime.rect.y -= 20

			if step % 2 == 0 and step != 0:
				slime.rect.x = 266

			self.slimes.add(slime)

	def blit(self):
		self.slimes.draw(self.my_screen.screen)

