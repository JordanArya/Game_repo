import pygame
from pygame.sprite import Sprite

class Label(Sprite):

	def __init__(self,parrent,text):
		super().__init__()
		self.settings = parrent.settings
		self.my_screen = parrent.my_screen
		self.text = text
		self.font = pygame.font.SysFont(self.settings.LABEL_FONT, self.settings.LABEL_FONT_SIZE)
		self.image = self.font.render(self.text,True,self.settings.LABEL_FONT_COLOR)

		self.rect = self.image.get_rect()



	def blit(self):
		self.my_screen.screen.blit(self.image,self.rect)