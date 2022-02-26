from pygame import font
import pygame

from Aliengame.ship import Ship 

class ScoreBoard():

	def __init__(self,AlienGame):
		self.game = AlienGame
		self.settings = AlienGame.settings
		self.screen = AlienGame.screen
		self.screen_rect = self.screen.get_rect()
		self.stats = AlienGame.stats
		self.font = font.SysFont(self.settings.SCORE_FONT,self.settings.SCORE_FONT_SIZE)

		self.update_score_image()
		self.update_high_score_image()
		self.update_level_image()

		self.ships = pygame.sprite.Group()
		self.update_ship_image()

	def update_ship_image(self):
		ship = Ship(self.game)
		ship_width,ship_height = ship.rect.width, ship.rect.height
		ship.image = pygame.transform.scale(ship.image,(ship_width//2,ship_height//2))
		ship.rect = ship.image.get_rect()
		ship_width,ship_height = ship.rect.width, ship.rect.height
	
		
		self.ships.empty()
		for every_ship in range(self.settings.SHIP_LIMIT):
			ship = Ship(self.game)
			ship.image = pygame.transform.scale(ship.image,(ship_width//2,ship_height//2))
			ship.rect.x = self.screen_rect.left + 10 + (every_ship*ship_width)
			ship.rect.y = 20
			self.ships.add(ship)

	def update_score_image(self):
		self.score_image = self.font.render(str(self.stats.score),True,self.settings.SCORE_TEXT_COLOR)

		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.topright = self.screen_rect.topright

		self.score_image_rect.y += 20
		self.score_image_rect.x -= 20

	def update_high_score_image(self):
		self.high_score_image = self.font.render(str(self.stats.high_score),True,self.settings.SCORE_TEXT_COLOR)
		
		self.high_score_image_rect = self.high_score_image.get_rect()
		self.high_score_image_rect.midtop = self.screen_rect.midtop

		self.high_score_image_rect.y += 20
		self.high_score_image_rect.x -= 20


	def update_level_image(self):
		self._level_image = self.font.render(str(self.stats.level),True,self.settings.SCORE_TEXT_COLOR)
		
		self._level_image_rect = self._level_image.get_rect()
		self._level_image_rect.midtop = self.score_image_rect.midtop

		self._level_image_rect.y += 40
		

	def blitme(self):
		self.screen.blit(self.score_image,self.score_image_rect)
		self.screen.blit(self.high_score_image,self.high_score_image_rect)
		self.screen.blit(self._level_image,self._level_image_rect)
		self.ships.draw(self.screen)

	def check_high_score(self):
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.update_high_score_image()



