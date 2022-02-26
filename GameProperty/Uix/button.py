import pygame
from pygame import font

class Button:

	def __init__(self,parrent,text):
		self.app = parrent
		self.settings = parrent.settings
		self.my_screen = parrent.my_screen
		self.stats = parrent.stats

		self.color = self.settings.ENTRY_TEXT_COLOR_INACTIVE 

		self.rect = pygame.Rect(0,0,self.settings.BUTTON_WIDTH,self.settings.BUTTON_HEIGHT)
		self.rect.center = self.my_screen.rect.center
		self.rect.y -= self.settings.SCREEN_HEIGHT//6

		self.text_to_image(text)


	def text_to_image(self,text):
		self.font = font.SysFont(self.settings.SCORE_FONT,self.settings.SCORE_FONT_SIZE)
		
		self.font_image = self.font.render(text,True,self.settings.SCORE_TEXT_COLOR)

		self.font_rect = self.font_image.get_rect()

	def draw(self):
		self.font_rect.center = self.rect.center
		if not self.stats.pregame and not self.app.message_screen_active:
			self.rect.width = self.font_rect.width
			self.rect.left = self.font_rect.left
		pygame.draw.rect(self.my_screen.screen, self.color,self.rect)
		self.my_screen.screen.blit(self.font_image,self.font_rect)

class PlayButton:

	def __init__(self,parrent):
		self.Sound_index = 0
		self.app = parrent
		self.settings = parrent.settings
		self.my_screen = parrent.my_screen
		self._make_pause_play_button()
		self._make_sound_image()

	def _make_pause_play_button(self):
		self.image = pygame.image.load(self.settings.BUTTON_PICTURE[int(self.app.GamePause)])

		self.rect =self.image.get_rect()

		self.image = pygame.transform.scale(self.image,(self.rect.width//3,self.rect.height//3))
		self.rect = self.image.get_rect()

		self.rect.topright = self.my_screen.rect.topright
		self.rect.x -= 10

	def _make_sound_image(self):
		self.sound_image = pygame.image.load(self.settings.SOUND_PICTURE[self.Sound_index])

		self.sound_image_rect = self.sound_image.get_rect()
		self.sound_image = pygame.transform.scale(self.sound_image,(self.sound_image_rect.width//3,self.sound_image_rect.height//3))

		self.sound_image_rect = self.sound_image.get_rect()

		self.sound_image_rect.topright = self.my_screen.rect.topright
		self.sound_image_rect.x -= self.rect.width*2

	def blit(self):
		self.my_screen.screen.blit(self.image,self.rect)
		self.my_screen.screen.blit(self.sound_image,self.sound_image_rect)

class BackButton:
	def __init__(self,parrent):
		self.my_screen = parrent.my_screen
		self.settings =parrent.settings
		self.make_back_button()

	def make_back_button(self):
		self.image = pygame.image.load(self.settings.BACK_BUTTON_PICTURE)
		self.image = pygame.transform.scale(self.image,(self.settings.BACK_BUTTON_WIDTH,self.settings.BACK_BUTTON_HEIGHT))
		self.rect = self.image.get_rect()
		self.rect.topleft = self.my_screen.rect.topleft

	def blit(self):
		self.my_screen.screen.blit(self.image,self.rect)

