import pygame
from pygame import font

class ScoreBoard:
	def __init__(self,parrent):
		self.my_screen = parrent.my_screen
		self.settings = parrent.settings
		self.stats = parrent.stats
		self.font = font.SysFont(self.settings.SCORE_FONT,self.settings.SCORE_FONT_SIZE)
		self.make_score_image()
		self.make_time_board()
		self.blitme()

	def make_score_image(self):
		self.score_image = self.font.render(str(self.stats.score),True,self.settings.SCORE_TEXT_COLOR)

		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.midtop = self.my_screen.rect.midtop
		self.score_image_rect.y += 10

	def make_time_board(self):
		self.time_image = self.font.render("time : " +str(self.stats.time),True,self.settings.SCORE_TEXT_COLOR)

		self.time_image_rect = self.score_image.get_rect()
		self.time_image_rect.topleft = self.my_screen.rect.topleft
		self.time_image_rect.y += 10
		self.time_image_rect.x += 30

	def blitme(self):
		self.my_screen.screen.blit(self.score_image,self.score_image_rect)
		self.my_screen.screen.blit(self.time_image,self.time_image_rect)
