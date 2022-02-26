import pygame

class Screen:

	def __init__(self,JumpingSlime):
		self.color = 'black'
		self.app = JumpingSlime
		self.stats = JumpingSlime.stats
		self.settings = JumpingSlime.settings
		self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH,self.settings.SCREEN_HEIGHT))
		self.rect = self.screen.get_rect()
		self.bg_Screen = pygame.image.load(self.settings.BG_SCREEN)
		self.bg_Screen = pygame.transform.scale(self.bg_Screen,(self.settings.SCREEN_WIDTH,self.settings.SCREEN_HEIGHT))

	def blit(self):
		if not self.stats.pregame and not self.app.admin and not self.app.message_screen_active:
			self.screen.blit(self.bg_Screen,(0,0))
		elif self.app.message_screen_active:
			self.screen.fill((137,190,203))
		else:
			self.screen.fill(self.color)