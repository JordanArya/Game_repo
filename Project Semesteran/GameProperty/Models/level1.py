import pygame
from GameProperty.Models.platform import Platform
from random import randint

class Level1(Platform):
	def __init__(self,parrent):
		self.start_y = 400
		self.app = parrent
		super().__init__(parrent)
		
		#self.image = pygame.transform.scale(self.image,(self.settings.SCREEN_WIDTH,self.settings.SCREEN_HEIGHT//20))
		self.rect = self.image.get_rect()

		#self.rect.y = self.start_y
		#self.rect.x = -1
		#self.rect.width = 500

	def Random_platform(self):
		PLATFORM_LAST_RECT_Y = 500
		rect_y_list = []

		number_of_platform = 0
		gap = self.settings.SCREEN_HEIGHT//8
		while PLATFORM_LAST_RECT_Y > 0 + self.settings.SCREEN_HEIGHT//12:
			distance = randint(gap,gap*2)
			PLATFORM_LAST_RECT_Y -= distance
			if PLATFORM_LAST_RECT_Y > 0 + self.settings.SCREEN_HEIGHT//12:
				number_of_platform += 1
				rect_y_list.append(PLATFORM_LAST_RECT_Y)

		return number_of_platform ,rect_y_list

	def changing_platform_size(self,width):
		if width > self.settings.SCREEN_WIDTH - 300:
			self.image = pygame.image.load(self.settings.BRICK_PLATFORM)
		else:
			self.image = pygame.image.load(self.settings.BRICK_PLATFORM_SMALL)

		self.image = pygame.transform.scale(self.image,(width,self.settings.SCREEN_HEIGHT//20))
		self.rect = self.image.get_rect()
