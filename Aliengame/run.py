import sys
import pygame
from Aliengame.settings import Settings
from Aliengame.game_stats import Gamestats
from Aliengame.ship import Ship
from Aliengame.bullet import Bullet
from Aliengame.alien import Alien
from Aliengame.button import Button
from Aliengame.score_board import ScoreBoard
import time

#from rain_drop import RainDrop
#from genangan import Genangan
#from raindrop import RainDrop as RAINDROP
#from random import randint
class AlienGame:

	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.stats = Gamestats(self)
		self.full_screen_mode_status = False
		self.normal_screen_mode()
		self.score_board = ScoreBoard(self)
		#self.full_screen_mode()

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		#self.rains = pygame.sprite.Group()
		#self.genangs = pygame.sprite.Group()
		#self.raindrops = pygame.sprite.Group()
		self._create_fleet()
		#self._rain_mode()
		self.title = pygame.display.set_caption("ALIEN GAME")
		self.play_button = Button(self,"Play")
		#screenmode flag
		
		

	def run(self):

		while True :
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self.bullets.update()
				self._update_aliens()
				#self._update_rain()
				self._update_bullets()
			self._update_screen()
			
	#refactoring methods
	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()			
			elif self.stats.game_active:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						sys.exit()
					elif self.stats.game_active:
						self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)

			elif not self.stats.game_active :
				if event.type == pygame.MOUSEBUTTONDOWN:
					mouse_position = pygame.mouse.get_pos()
					self._check_play_button(mouse_position)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_SPACE :
			self._fire_bullet()

		#elif event.key == pygame.K_f and self.full_screen_mode_status == False:
			#self.full_screen_mode()
		#elif event.key == pygame.K_n and self.full_screen_mode_status:
			#self.normal_screen_mode()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False

	def _check_play_button(self,mouse_position):
		if self.play_button.rect.collidepoint(mouse_position):
			self.score_board.check_high_score()
			self.stats.reset_stats()
			self.score_board.update_score_image()
			self.score_board.update_ship_image()


			self.settings.init_dynamic_settings()
			self.stats.game_active = True

			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.ship.center_ship()			
			pygame.mouse.set_visible(False)
	"""
	def full_screen_mode(self):
		self.full_screen_mode_status = True
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.SCREEN_WIDTH = self.screen.get_rect().width
		self.settings.SCREEN_HEIGHT = self.screen.get_rect().height
		self.ship = Ship(self)
		self.aliens.empty()
		self._create_alien(14,8)
	"""
		
		

	def normal_screen_mode(self):
		self.full_screen_mode_status = False
		self.settings.SCREEN_WIDTH = 600
		self.settings.SCREEN_HEIGHT = 400
		self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))

	def _fire_bullet(self):
		if len(self.bullets) < self.settings.BULLETS_ALLOWED:
			bullet = Bullet(self)
			self.bullets.add(bullet)

	def _update_bullets(self):
		for bullet in self.bullets.sprites():
				if bullet.rect.bottom < 0:
					self.bullets.remove(bullet)
		self._check_bullets_aliens_collisions()

	def _check_bullets_aliens_collisions(self):
		collisons = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
		if collisons:
			number_alien = 0 
			for alien in collisons.values():
				number_alien += len(alien)
				

			self.stats.score += self.settings.ALIEN_POINTS * number_alien
			self.score_board.update_score_image()

		
		if not self.aliens:
			self._create_fleet()
			self.bullets.empty()
			self.settings.speed_scale = 2
			self.settings.increase_speed()
			self.stats.level += 1
			self.score_board.update_level_image()

	def _create_fleet(self):
		alien = Alien(self)
		ship = Ship(self)
		alien_height = alien.rect.height
		alien_width = alien.rect.width

		available_space_x = self.settings.SCREEN_WIDTH - (2 * alien_width)
		number_alien_x = available_space_x // (2*alien_width)

		available_space_y = self.settings.SCREEN_HEIGHT  - (3 * ship.rect.height)
		number_alien_y = available_space_y // (2 * alien_height)

		for row_number in range(number_alien_y):
			for alien_number in range(number_alien_x):
				self._create_alien(alien_number, row_number)
				
		self.aliens.add(alien)

	def _create_alien(self,alien_number,row_number):
		alien = Alien(self)
		alien_height = alien.rect.height
		alien_width = alien.rect.width

		alien.rect.x =alien_width + 2 * alien_width * alien_number
		alien.rect.y = alien_height + 2* alien_height *row_number
		self.aliens.add(alien)

	def _update_aliens(self):
		self._check_fleet_edge()
		self.aliens.update()

		collisons = pygame.sprite.spritecollideany(self.ship,self.aliens)
		if collisons:
			self._ship_hit()



	def _ship_hit(self):
		self.settings.SHIP_LIMIT -= 1
		self.score_board.update_ship_image()


		if self.settings.SHIP_LIMIT >= 0:

			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.ship.center_ship()


			time.sleep(1)

		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)



	def _check_fleet_edge(self):
		for alien in self.aliens.sprites():
			if alien.check_edges() :
				for alien in self.aliens.sprites():
					alien.drop()
				if alien.check_bottom_edges():
					self.settings.ALIEN_DROP *= -1
					pass
				self.settings.ALIEN_SPEED *= -1
				break
	
	def _rain_mode(self):
		rain = RainDrop(self)

		rain_height = rain.rect.height
		rain_width = rain.rect.width

		available_space_x = self.settings.SCREEN_WIDTH - (2 * rain_width)
		number_rain_x = available_space_x // (2*rain_width)



		available_space_y = self.settings.SCREEN_HEIGHT
		self.number_rain_y = available_space_y // (rain_height//2)
		for rain_number in range(number_rain_x):
			self.create_rain(rain_number)
		
		
	

	#	for row_number in range(number_rain_y):
	#		for rain_number in range(number_rain_x):
	#			self.create_rain(row_number,rain_number)
		
		


	def create_rain(self,rain_number):
		rain = RainDrop(self)

		rain_height = rain.rect.height
		rain_width = rain.rect.width

		rain.rect.x = rain_width +2 *rain_width*rain_number
		rain.rect.y = 0 

		self.rains.add(rain)

	def _update_rain(self):
		self.rain_continues()
		self.check_edges()
		self.check_changes_rain()
		self.rains.update()
		#for all_genang in self.genangs:
		#	self.genangs.remove(all_genang)

	def rain_continues(self):
		for rain in self.rains.sprites():
			if rain.rain_continues():
				self._rain_mode()
				break
		
	def check_changes_rain(self):
		for rain in self.rains.sprites():
			if rain.rect.y == 60:
				self.current_y = 60
				self.minus_point = 90
				for rain in self.rains.sprites():
					if rain.rect.y == self.current_y:
						self.rains.remove(rain)
				self.change_rain_shape()
				break

		for rain in self.rains.sprites():
			if rain.rect.y == 150:
				self.current_y = 150
				self.minus_point = 90
				for rain in self.rains.sprites():
					if rain.rect.y == self.current_y:
						self.rains.remove(rain)
				self.change_rain_shape()
				break

		for rain in self.rains.sprites():
			if rain.rect.y == 230:
				self.current_y =  230
				self.minus_point = 180
				for rain in self.rains.sprites():
					if rain.rect.y == self.current_y:
						self.rains.remove(rain)
				self.change_rain_shape()
				break

		for rain in self.rains.sprites():
			if rain.rect.y == 220:
				self.current_y = 220
				self.minus_point = 270
				for rain in self.rains.sprites():
					if rain.rect.y == self.current_y:
						self.rains.remove(rain)
				self.change_rain_shape()
				break

	def check_edges(self):
		for rain in self.rains.sprites():
			if rain.check_edges():
				if len(self.genangs.sprites()) < 4:
					self.make_genang(rain)
				self.rains.remove(rain)

			elif rain.check_ship_touch():
				self.rains.remove(rain)

	#def make_genangs(self):
		#rain = RainDrop(self)

		#available_space_x = self.settings.SCREEN_WIDTH - (2 * rain_width)
		#number_rain_x = available_space_x // (2*rain_width)


		#for rain_number in range(number_rain_x):
#		self.make_genang(rain_number)

	def make_genang(self,rain):
		genang = Genangan(self)

		genang.oval_rect.x = rain.rect.x
		genang.oval_rect.y = 0

		genang.draw_genang()

		self.genangs.add(genang)
		

	def change_rain_shape(self):
		rain = RainDrop(self)

		rain_height = rain.rect.height
		rain_width = rain.rect.width

		available_space_x = self.settings.SCREEN_WIDTH - (2 * rain_width)
		number_rain_x = available_space_x // (2*rain_width)

		

		for rain_number in range(number_rain_x):
			self.create_rains(rain_number)

	def create_rains(self,rain_number):
		rain = RainDrop(self)

		rain_height = rain.rect.height
		rain_width = rain.rect.width
		rain.change_draw(self.current_y//60)
		rain.rect.x = rain_width +2 *rain_width*rain_number
		rain.rect.y = self.current_y


		self.rains.add(rain)
	
	"""
	def _create_rain(self):
		raindrop = RainDrop(self)
		number_of_raindrop = ((self.settings.SCREEN_HEIGHT* self.settings.SCREEN_WIDTH)) // 20 //(raindrop.rect.height * raindrop.rect.width)
		for every_raindrop in range(number_of_raindrop):
			self._crate_raindrop()

	def _create_raindrop(self):
		raindrop = RainDrop(self)
		raindrop.rect.y = randint(-self.settings.SCREEN_HEIGHT, -5)
		raindrop.rect.x = randint(0,self.settings.SCREEN_WIDTH)
		self.raindrops.add(raindrop)

	def _update_raindrop(self):
		self.raindrops.update()
	"""

	def _update_screen(self):
		self.screen.fill(self.settings.BG_COLOR)
		self.score_board.blitme()
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw()
		
		#self.raindrops.draw(self.screen)
		self.aliens.draw(self.screen)
		if not self.stats.game_active:
			self.play_button.draw()

		#for rain in self.rains.sprites():
		#	rain.draw()

	

		pygame.display.flip()
		pygame.time.Clock().tick(30)



if __name__ == '__main__':
	my_game = AlienGame()
	my_game.run()