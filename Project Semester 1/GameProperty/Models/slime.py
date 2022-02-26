import pygame
from pygame.sprite import Sprite

class Slime(Sprite):
	def __init__(self,parrent):
		super().__init__()
		self.move_right = False
		self.move_left = False
		self.jump = False
		self.down = False

		self.app = parrent
		self.settings = parrent.settings
		self.my_screen = parrent.my_screen

		self.stamina = 30


		

		self.Screen_width = self.settings.SCREEN_WIDTH
		self.Screen_height = self.settings.SCREEN_HEIGHT

		self.standing_animation()
		self.rect = self.image.get_rect()
	
		#self.rect.bottomleft = self.my_screen.rect.bottomleft
		self.rect.bottom = self.app.platform.rect.top

		self.SLIME_SPEED = self.rect.width//6
		self.SLIME_JUMP_SPEED = self.rect.height//2


		self.jump_limit = self.rect.y - self.rect.height*5
		

	def blit(self):
		self.my_screen.screen.blit(self.image,self.rect)

	def move_right_left(self,indicator):
		if indicator.lower() == 'left' and self.rect.bottomleft[0] >= self.my_screen.rect.bottomleft[0]:
			self.rect.x -= self.SLIME_SPEED

		else:
			if self.rect.bottomright[0] <= self.Screen_width:
				self.rect.x +=   self.SLIME_SPEED

		self.walk_animation(indicator)

		if self.app.boost:
			self.dash_animation(indicator)
	 
		
	def move_up_down(self):
		if self.jump:
			if self.rect.y >= self.jump_limit:
				self.rect.y -= self.SLIME_JUMP_SPEED
				self.jump_animation()
			else:
				self.jump = False
				self.down = True
		elif self.down:
			if self.rect.y < self.jump_limit + self.rect.height*2:
				self.rect.y += self.SLIME_JUMP_SPEED
			else:
				self.down = False

	def down_speed(self):
		if self.SLIME_JUMP_SPEED > self.rect.height//3:
			self.SLIME_JUMP_SPEED /= 2
		if self.SLIME_SPEED > self.rect.width//6:
			self.SLIME_SPEED  /= 2

	#LITTLE ANIMATION

	def standing_animation(self):
		if not self.jump and not self.down:
			self.image = pygame.image.load(self.settings.STAND_SLIME_IMAGES[self.settings.IMAGES_INDEX])
			self.image = pygame.transform.scale(self.image,(self.Screen_width//10,self.Screen_height//20)) 

	def dash_animation(self,indicator):
		if not self.jump and not self.down:
			if indicator.lower() == 'left':
				self.image = pygame.image.load(self.settings.SLIME_DASH_LEFT[self.settings.IMAGES_INDEX])	
			else:
				self.image = pygame.image.load(self.settings.SLIME_DASH_RIGHT[self.settings.IMAGES_INDEX])
		
			self.image = pygame.transform.scale(self.image,(self.Screen_width//8,self.Screen_height//22)) 

	def jump_animation(self):
		self.image = pygame.image.load(self.settings.SLIME_JUMP[self.settings.IMAGES_INDEX])	
		self.image = pygame.transform.scale(self.image,(self.Screen_width//8,self.Screen_height//18)) 

	def walk_animation(self,indicator):
		if not self.jump and not self.down:
			if indicator.lower() == 'left':
				self.image = pygame.image.load(self.settings.SLIME_WALK_LEFT[self.settings.IMAGES_INDEX])	
			else:
				self.image = pygame.image.load(self.settings.SLIME_WALK_RIGHT[self.settings.IMAGES_INDEX])
		
			self.image = pygame.transform.scale(self.image,(self.Screen_width//8,self.Screen_height//20)) 