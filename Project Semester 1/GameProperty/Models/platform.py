import pygame

class Platform(pygame.sprite.Sprite):

	def __init__(self,parrent):
		super().__init__()
		self.settings = parrent.settings
		self.my_screen = parrent.my_screen 
		self.app = parrent

		self.up = True
		self.down = False

		self.image = pygame.image.load(self.settings.PLATFORM)
		self.image = pygame.transform.scale(self.image,(self.settings.SCREEN_WIDTH,self.settings.SCREEN_HEIGHT//10))
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.my_screen.rect.midbottom

	def show(self):
		self.my_screen.screen.blit(self.image,self.rect)

	def moving_up(self):
		if self.rect.y > self.app.slime.rect.height and self.up:
			self.rect.y -= 2
			if self.rect.y <= self.app.slime.rect.height:
				self.up = False
				self.down = True

		if self.rect.bottom <= self.my_screen.rect.bottom and self.down:
			self.rect.y += 2
			if self.rect.bottom  > self.my_screen.rect.bottom:
				self.app.my_platforms.empty()
				self.app.create_challange_platfrom()
				self.up = True
				self.down = False
				self.app.stats.score += 1
				if self.app.stats._check_high_score():
					self.app.Db.update_high_score(self.app.player.USERNAME,self.app.stats.high_score)
				

