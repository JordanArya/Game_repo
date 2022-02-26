import pygame
import sys
from random import randint
from datetime import datetime as dt
import bcrypt


from GameProperty.admintrator import Admintrator

from GameProperty.Config.settings import Settings
from GameProperty.Config.screen import Screen
from GameProperty.Config.gamestats import GameStats
from GameProperty.Config.scoreboard import ScoreBoard


from GameProperty.Models.level1 import Level1
from GameProperty.Models.slime import Slime
from GameProperty.Models.platform import Platform
from GameProperty.Models.skin_setting import SkinSettings

from GameProperty.Uix.button import Button,PlayButton,BackButton
from GameProperty.Uix.entry import Entry 
from GameProperty.Uix.label import Label

from SqlData.main import SaveData
from SqlData.account import Account
from SqlData.message_main import Message

from GameProperty.message_screen import Message_Screen



class MainGame:
	def __init__(self,parrent):
		self.time_counter = 0
		self.GameActivate = True
		self.GameActive = False
		self.GamePause = False

		self.admin = False
		self.message_screen_active = False
		self.message_command = None

		self.Db = SaveData()
		self.MsgDb = Message()

		pygame.init()

		self.stats = GameStats()

		self.settings = Settings()

		self.my_screen = Screen(self)
		
		self.New_game_button = Button(self,'New Game')

		self.Load_game_button = Button(self,'Load Game')

		self.username_label = Label(self,'Player')
		self.username_entry = Entry(self,"")

		self.settings.LABEL_FONT_SIZE = 80

		self.verification_button = Button(self,"Verifify")

		self.login_button = Button(self,'Login')

		self.pass_entry = Entry(self,"")

		self.make_new_button = Button(self,'Make New')

		self.start_button = Button(self,'Press To Play')

		self.choose_skin_button = Button(self,'choose skin')

		self.quit_to_menu_button = Button(self,'QUIT TO MENU')

		self.quit_to_pregame_button = Button(self,'CHANGE ACCOUNT')

		self.delete_account_button = Button(self,'Delete Account')

		self.message_button = Button(self,'Message')

		self.search_msg_button = Button(self,'Message')
		self.search_history_msg_button = Button(self,'History')
		self.text_to_button = Button(self,'Send')


		self.settings.LABEL_FONT_SIZE=100
		self.admindmin_Label = Label(self,'Admin Mode')

		self.settings.LABEL_FONT_SIZE=40
		self.to_label = Label(self,'TO')
		self.message_label = Label(self,'MSG')
		self.message_entry = Entry(self,'')
		self.to_entry = Entry(self,"")
		self.send_button = Button(self,'SEND')



		self.my_platforms = pygame.sprite.Group()
		self.platform = Platform(self)

		self.play_button = PlayButton(self)

		self.backward_button = BackButton(self)


		self.slime = Slime(self)
		self.skin_choose = SkinSettings(self)
		self.admindmin = Admintrator(self)
		self.boost = False

		self.create_challange_platfrom()

		pygame.mixer.music.load('GameProperty/Sound/backsound.wav')
		pygame.mixer.music.set_volume(0.05)

		self.message_screen = Message_Screen(self)

		

	#Screen Settings

	def _update_screen(self):
		self.my_screen.blit()

		
		if self.admin:
			self.make_ignoscas()
			
			pygame.display.flip()
		
			
		if not self.admin:
			if self.stats.choose_skin_win:
				self.skin_choose.blit()
			
			elif self.stats.pregame:
				if self.stats.mainpregame:
					self._update_new_game()
					self._update_load_game()

				else:
					self._pregame_screen()

			else:
				if self.message_screen_active:
					self.backward_button.blit()
					if not self.message_command:
						self._update_search_msg_button()
						self._update_search_history_msg_button()
						self._update_text_to_button()
					elif self.message_command == 'GET':
						self.make_message_window_get()
					elif self.message_command == 'History':
						self.make_history_msg_window()
					elif self.message_command == 'text':
						self.message_screens()


					"""data = self.MsgDb.get_all_message(self.player.USERNAME)
																				self.message_screen.make_message_screen(data)
																				self.backward_button.blit()"""
				else:
					self.Db.update_last_play(self.player.USERNAME,dt.now())
					self._update_slime()
					self.platform.show()

					if self.GameActive:
						self._game_screen()
						
					else:
						
							self.start_button.draw()
							self.choose_skin_button.rect.y = self.start_button.rect.y + 100
							self.choose_skin_button.draw()
							if self.player.STATUS == 'PLAYER':
								self.delete_account_button.rect.y = self.choose_skin_button.rect.y + 100
								self.delete_account_button.draw()
								self.message_button.rect.y = self.delete_account_button.rect.y + 100
								self.message_button.draw()
							else:
								self.go_admin_setting_button = Button(self,'ADMIN MODE')
								self.go_admin_setting_button.rect.y = self.choose_skin_button.rect.y + 100
								self.go_admin_setting_button.draw()

							self.settings.LABEL_FONT_SIZE = 80
							self._update_highscore_label()
							self._update_long_survive_label()
			


		pygame.display.flip()
		pygame.time.Clock().tick(30)


	def make_ignoscas(self):
		self.admindmin_Label.rect.center = self.my_screen.rect.center
		self.admindmin_Label.blit()

		self.settings.LABEL_FONT_SIZE = 18
		self.sorry = Label(self,'YANG JALAN HANYA DI CMND-NYA')
		self.sorry.rect.center = self.my_screen.rect.center
		self.sorry.rect.y = self.admindmin_Label.rect.y +60

		self.sorry.blit()

		self.settings.LABEL_FONT_SIZE = 16

		self.duibuchi = Label(self,'MAAF MASIH BUG UNTUK PYGAMENYA SAAT KE MENU ADMIN')
		self.duibuchi.rect.center = self.my_screen.rect.center
		self.duibuchi.rect.y = self.admindmin_Label.rect.y +120

		self.duibuchi.blit()

		self.settings.LABEL_FONT_SIZE = 12

		self.Sumimasen = Label(self,'MOHON PYGAME SCREEN-NYA JANGAN DIHIRAUKAN DAN DIPINDAH-PINDAHKAN')
		self.Sumimasen.rect.center = self.my_screen.rect.center
		self.Sumimasen.rect.y = self.admindmin_Label.rect.y +160

		self.Sumimasen.blit()

		self.settings.LABEL_FONT_SIZE = 25

		self.maaf = Label(self,'KALAU PERLU DI-MINIMIZE SAJA')
		self.maaf.rect.center = self.my_screen.rect.center
		self.maaf.rect.y = self.admindmin_Label.rect.y + 200

		self.maaf.blit()



	def _update_username_label(self):
		self.username_label.rect.center = self.my_screen.rect.center		
		self.username_label.rect.y -= self.my_screen.rect.height //3
		self.username_label.blit()

	def _update_username_entry(self):
		self.username_entry.rect.center = self.my_screen.rect.center
		self.username_entry.rect.y = self.username_label.rect.y + 50
		self.username_entry.draw()

	def _update_pass_entry(self):
		self.pass_entry.rect.center = self.my_screen.rect.center
		self.pass_entry.rect.y = self.username_label.rect.y + 150
		self.pass_entry.draw()

	def _update_makenew_button(self):
		self.make_new_button.rect.center = self.my_screen.rect.center
		self.make_new_button.rect.y = self.username_label.rect.y + 250
		self.make_new_button.draw()

	def _update_login_button(self):
		self.login_button.rect.center = self.my_screen.rect.center
		self.login_button.rect.y = self.username_entry.rect.y + 200
		self.login_button.draw()

	def _update_new_game(self):

		self.New_game_button.rect.center = self.my_screen.rect.center
		self.New_game_button.rect.y = self.username_entry.rect.y
		self.New_game_button.draw()

	def _update_verification(self):
		self.verification_button.rect.center = self.my_screen.rect.center
		self.verification_button.rect.y =  self.username_entry.rect.y + 200
		self.verification_button.draw()

	def _update_load_game(self):

		self.Load_game_button.rect.center = self.my_screen.rect.center
		self.Load_game_button.rect.y = self.username_entry.rect.y + 100
		self.Load_game_button.draw()

	def _update_highscore_label(self):
		self.high_score_label = Label(self,str(self.stats.high_score))
		self.high_score_label.rect.topleft = self.my_screen.rect.topleft
		self.high_score_label.blit()

	def _update_long_survive_label(self):
		self.best_long_survive_label = Label(self,str(self.stats.best_long_survive))
		self.best_long_survive_label.rect.topright = self.my_screen.rect.topright
		self.best_long_survive_label.blit()

	def _update_search_msg_button(self):
		self.search_msg_button.rect.center = self.my_screen.rect.center
		self.search_msg_button.rect.y -=  100
		self.search_msg_button.draw()

	def _update_search_history_msg_button(self):
		self.search_history_msg_button.rect.center = self.my_screen.rect.center
		self.search_history_msg_button.rect.y =  self.search_msg_button.rect.y + 100
		self.search_history_msg_button.draw()

	def _update_text_to_button(self):
		self.text_to_button.rect.center = self.my_screen.rect.center
		self.text_to_button.rect.y =  self.search_msg_button.rect.y + 200
		self.text_to_button.draw()

	def _update_to_label(self):
		self.to_label.rect.center = self.my_screen.rect.center		
		self.to_label.rect.y -= self.my_screen.rect.height //3
		self.to_label.blit()
	
	def _update_to_entry(self):
		self.to_entry.rect.center = self.my_screen.rect.center
		self.to_entry.rect.y = self.to_label.rect.y + 50
		self.to_entry.draw()

	def _update_message_label(self):
		self.message_label.rect.center = self.my_screen.rect.center		
		self.message_label.rect.y = self.to_label.rect.y + 150
		self.message_label.blit()


	def _update_message_entry(self):
		self.message_entry.rect.center = self.my_screen.rect.center
		self.message_entry.rect.y = self.to_label.rect.y + 200
		self.message_entry.draw()

	def _update_send_button(self):
		self.send_button.rect.center = self.my_screen.rect.center
		self.send_button.rect.y = self.to_label.rect.y + 280
		self.send_button.draw()



	



	def _update_slime(self):
		#self.slime.jump_limit = self.platform.rect.top - (self.slime.rect.height*20)
		

		if self.slime.jump == False  and self.slime.down == False or self.slime.rect.bottom > self.platform.rect.top:
			self.slime.standing_animation()
			self.slime.rect.bottom = self.platform.rect.top
			self.slime.jump_limit = self.slime.rect.y - self.slime.rect.height*2


		if self.slime.move_right:
			self.slime.move_right_left('right')

		elif self.slime.move_left:
			self.slime.move_right_left('LEFt')
		
		self.slime.move_up_down()

		if self.slime.stamina <= 0 or self.boost == False:
			self.boost = False
			self.slime.down_speed()

		self.slime.blit()
		
		#self.GameActivate = False

	def create_challange_platfrom(self):
		
		platform = Level1(self)
		number_of_platform,rect_y_list = platform.Random_platform()

		for each_platform in range(number_of_platform):
			gap = randint(self.settings.SCREEN_WIDTH//6,self.settings.SCREEN_WIDTH//2)
			for platforms in range(2):

				platform = Level1(self)

				if platforms == 0 :
					platform.changing_platform_size(gap)
					platform.rect.right = self.my_screen.rect.right


				else:
					platform.changing_platform_size(self.settings.SCREEN_WIDTH-gap*2)

				platform.rect.y = rect_y_list[each_platform]
				self.my_platforms.add(platform)

	def _update_platforms(self):
		collisons = pygame.sprite.spritecollideany(self.slime,self.my_platforms)
		if collisons:
			self.play_hit_sound()
			self.stats.time = 0
			self.platform.rect.bottom = self.my_screen.rect.bottom
			self.slime.rect.bottom = self.platform.rect.top
			self.slime.jump = False
			self.platform.up = True
			self.platform.down = False
			self.my_platforms.empty()
			self.create_challange_platfrom()

	def check_time(self):
		if self.time_counter == 30:
			self.stats.time += 1
			self.time_counter = 0
			self.Db.update_last_play(self.player.USERNAME,dt.now())
		else:
			self.time_counter += 1
			if self.stats._best_long_survive_check():
				self.Db.update_long_survive(self.player.USERNAME,self.stats.best_long_survive)

	def make_message_window_get(self):
		data = self.MsgDb.get_all_message(self.player.USERNAME)
		self.message_screen.make_message_screen(data,'GET')
		self.backward_button.blit()

	def make_history_msg_window(self):
		data = self.MsgDb.get_send_history(self.player.USERNAME)
		self.message_screen.make_message_screen(data,'History')
		self.backward_button.blit()

	def message_screens(self):
		self._update_to_label()
		self._update_to_entry()
		self._update_message_label()
		self._update_message_entry()
		self._update_send_button()

	



	# Check Events

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_position = pygame.mouse.get_pos()
				self.check_mouse_down_events(mouse_position)

			if not self.GamePause:
				if event.type == pygame.KEYDOWN :
					self.check_keydown_events(event)

			if event.type == pygame.KEYUP:
				self.check_keyup_events(event)

	def check_keydown_events(self,event):
		if not self.admin:
			if not self.stats.choose_skin_win:
				if self.message_screen_active:
					self._message_input_entry(event)

				elif not self.stats.pregame:
					if event.key == pygame.K_d:
						self.slime.move_right = True

					elif event.key == pygame.K_a:
						self.slime.move_left = True

					if self.slime.down == False:
						if event.key == pygame.K_w:
							self.slime.jump = True

					if event.key == pygame.K_LSHIFT and self.slime.stamina >= 0:
						if self.slime.move_right or self.slime.move_left:
							self.slime.SLIME_JUMP_SPEED *= 2
							
						self.slime.SLIME_SPEED  *= 2
						self.boost = True
				elif self.stats.pregame:
					self._input_user_pass_entry(event)
			
	def check_keyup_events(self,event):
		if event.key == pygame.K_d:
			self.slime.move_right = False
			self.slime.standing_animation()

		elif event.key == pygame.K_a:
			self.slime.move_left = False
			self.slime.standing_animation()

		if event.key == pygame.K_LSHIFT :
			self.boost = False

	def check_mouse_down_events(self,mouse_position):
		if not self.admin:
			if not self.stats.choose_skin_win:
				if self.stats.pregame:
					if self.stats.mainpregame:
						self._main_pregame_collide(mouse_position)
					else:
						self.pregame_collision(mouse_position)
						self.backward_button_collision(mouse_position)
						if self.stats.verification:
							self.verification_button_collide(mouse_position)
						else:
							if self.stats.game_choose == 'LOADGAME':					
								self._login_button_collide(mouse_position)
							elif self.stats.game_choose == 'NEWGAME':			
								self.make_new_user_collision(mouse_position)
				else:
					if not self.GameActive:
						if not self.message_screen_active:
							self._check_button_collide(mouse_position)
							self.choose_skin_button_collide(mouse_position)

							if self.player.STATUS == "PLAYER":
								self.delete_account_button_collide(mouse_position)
								self.go_Message_Collide(mouse_position)
							else:
								self.ADMIN_MODE_BUTTON_COLLIDE(mouse_position)
						else:
							self.backward_button_collision(mouse_position)
							if not self.message_command:
								self.search_msg_button_collide(mouse_position)
								self.search_history_msg_button_collide(mouse_position)
								self.text_to_button_collide(mouse_position)
							elif self.message_command == 'text':
								self._message_label_collide(mouse_position)
								self._to_entry_collide(mouse_position)
								self.send_button_collide(mouse_position)

					if self.GameActive == True:
						self.play_pause_button_colliding(mouse_position)
						if self.GamePause:
							self.quit_menu_collision(mouse_position)
			else:
				self.skin_collision(mouse_position)

	def _main_pregame_collide(self,mouse_position):
		if self.Load_game_button.rect.collidepoint(mouse_position):
			self.play_click_sound()
			self.stats.game_choose = 'LOADGAME'
			self.stats.mainpregame = False

		elif self.New_game_button.rect.collidepoint(mouse_position):
			self.play_click_sound()
			self.stats.game_choose = 'NEWGAME'
			self.username_entry.text = ''
			self.pass_entry.text = ''
			self.username_entry.update(self.username_entry.text)
			self.pass_entry.update(self.pass_entry.text)
			self.stats.mainpregame = False

	def _input_user_pass_entry(self,event):
		if self.username_entry.active:
			if event.key == pygame.K_BACKSPACE:
				self.username_entry.text = self.username_entry.text[0:-1]
			else:
				if len(self.username_entry.text) < 6:
					self.username_entry.text += event.unicode.upper()
			self.username_entry.update(text= self.username_entry.text)

		if self.pass_entry.active:
			if event.key == pygame.K_BACKSPACE:
				self.pass_entry.text = self.pass_entry.text[0:-1]
			else:
				if len(self.pass_entry.text) < 10:
					self.pass_entry.text += event.unicode
			text = ''
			for step in range(len(self.pass_entry.text)):
				text += '*'
			self.pass_entry.update(text)

	def _message_input_entry(self,event):
		if self.message_entry.active:
			if event.key == pygame.K_BACKSPACE:
				self.message_entry.text = self.message_entry.text[0:-1]
			else:
				if len(self.message_entry.text) < 20:
					self.message_entry.text += event.unicode.upper()
			self.message_entry.update(str(self.message_entry.text))

		if self.to_entry.active:
			if event.key == pygame.K_BACKSPACE:
				self.to_entry.text = self.to_entry.text[0:-1]
			else:
				if len(self.to_entry.text) < 6:
					self.to_entry.text += event.unicode.upper()
			self.to_entry.update(str(self.to_entry.text))

	def pregame_collision(self,mouse_position):
		if not self.stats.verification:
			self._entry_label_collide(mouse_position)
		self._pass_entry_collide(mouse_position)

	def _entry_label_collide(self,mouse_position):
		if self.username_entry.rect.collidepoint(mouse_position):
			self.play_click_sound()
			self.username_entry.active = True
			self.username_entry.color = self.settings.ENTRY_TEXT_COLOR_ACTIVE
		else:
			self.username_entry.active = False
			self.username_entry.color = self.settings.ENTRY_TEXT_COLOR_INACTIVE

	def _pass_entry_collide(self,mouse_position):
		if self.pass_entry.rect.collidepoint(mouse_position):
			self.play_click_sound()
			self.pass_entry.active = True
			self.pass_entry.color = self.settings.ENTRY_TEXT_COLOR_ACTIVE
		else:
			self.pass_entry.active = False
			self.pass_entry.color = self.settings.ENTRY_TEXT_COLOR_INACTIVE

	def _message_label_collide(self,mouse_position):
		if self.message_entry.rect.collidepoint(mouse_position):
			self.play_click_sound()
			self.message_entry.active = True
			self.message_entry.color = self.settings.ENTRY_TEXT_COLOR_ACTIVE
		else:
			self.message_entry.active = False
			self.message_entry.color = self.settings.ENTRY_TEXT_COLOR_INACTIVE

	def _to_entry_collide(self,mouse_position):
		if self.to_entry.rect.collidepoint(mouse_position):
			self.play_click_sound()
			self.to_entry.active = True
			self.to_entry.color = self.settings.ENTRY_TEXT_COLOR_ACTIVE
		else:
			self.to_entry.active = False
			self.to_entry.color = self.settings.ENTRY_TEXT_COLOR_INACTIVE

	def _login_button_collide(self,mouse_position):
		if self.login_button.rect.collidepoint(mouse_position):
			self.play_click_sound()

			name,Pass = self.username_entry.text,self.pass_entry.text
			Pass = Pass.encode('utf-8')
			player_data = self.Db.check_login_data(name,Pass)
			if player_data:
				self.player = Account(player_data[1],player_data[2],player_data[0],player_data[3],player_data[4],dt.now(),player_data[6],player_data[7],player_data[8])
				self.Db.update_last_play(self.player.USERNAME,dt.now())
				self.reset_pregame()

	def reset_pregame(self):
		self.stats.pregame = False
		self.stats.mainpregame = True
		self.stats.game_choose = None
		self.settings.IMAGES_INDEX = self.player.images_index
		self.stats.high_score = self.player.BEST_SCORE
		self.stats.best_long_survive = self.player.Best_Survive_Time
		
	def _check_button_collide(self,mouse_position):
		if self.start_button.rect.collidepoint(mouse_position):
			self.play_click_sound()
			pygame.mixer.music.play(loops=-1)
			self.platform.rect.bottom = self.my_screen.rect.bottom
			self.my_platforms.empty()
			self.create_challange_platfrom()
			self.GameActive = True

	def create_play_pause_button(self):
		self.play_button.blit()

	def play_pause_button_colliding(self,mouse_position):
		if self.play_button.rect.collidepoint(mouse_position):
			Index = int(self.GamePause)
			if Index == 0:
				self.GamePause = True
				self.slime.move_right = False
				self.slime.move_left = False
				pygame.mixer.music.pause()

			else:
				self.GamePause = False

				pygame.mixer.music.unpause()

			self.play_button._make_pause_play_button()

		if self.play_button.sound_image_rect.collidepoint(mouse_position):
			if self.play_button.Sound_index < len(self.settings.SOUND_VOLUME)-1:
				self.play_button.Sound_index += 1
			else:
				self.play_button.Sound_index = 0

			self.play_button._make_sound_image()
			pygame.mixer.music.set_volume(self.settings.SOUND_VOLUME[self.play_button.Sound_index])

	def make_new_user_collision(self,mouse_position):
		if self.make_new_button.rect.collidepoint(mouse_position):
			self.play_click_sound()
			check = self.Db.check_new_data(self.username_entry.text)
			if check and len(self.username_entry.text) >= 4 and len(self.pass_entry.text) > 0:
				password = bcrypt.hashpw(self.pass_entry.text.encode("utf-8"),bcrypt.gensalt())
				self.Db.savedata(self.username_entry.text,password)
				player_data = self.Db.getdata(self.username_entry.text)
				self.player = Account(player_data[1],player_data[2],player_data[0],player_data[3],player_data[4],dt.now(),player_data[6],player_data[7],player_data[8])
				self.reset_pregame()

	def backward_button_collision(self,mouse_position):
		if self.backward_button.rect.collidepoint(mouse_position):
			self.play_click_sound()
			self.stats.mainpregame = True
			self.stats.game_choose = False
			self.stats.verification = False
			self.message_screen_active = False
			self.message_command = None

	def skin_collision(self,mouse_position):
		for slime in self.skin_choose.slimes.sprites():
			if slime.rect.collidepoint(mouse_position):
				self.settings.IMAGES_INDEX = self.skin_choose.slimes.sprites().index(slime)
				self.stats.choose_skin_win = False
				self.Db.update_images_index(self.player.USERNAME,self.settings.IMAGES_INDEX)
				break

	def choose_skin_button_collide(self,mouse_position):
		if self.choose_skin_button.rect.collidepoint(mouse_position):
			self.play_click_sound()
			self.stats.choose_skin_win = True

	def quit_menu_collision(self,mouse_position):
		if self.quit_to_menu_button.rect.collidepoint(mouse_position):
			self.play_click_sound()
			self.GameActive = False
			self.GamePause = False
			self.reset_rect()
		if self.quit_to_pregame_button.rect.collidepoint(mouse_position):
			self.play_click_sound()
			self.GameActive = False
			self.stats.pregame = True
			self.GamePause = False
			self.reset_rect()
		

	def reset_rect(self):
		self.my_platforms.empty()
		self.stats.time = 0
		self.stats.score = 0
		self.platform.rect.bottom = self.my_screen.rect.bottom
		self.slime.rect.top = self.platform.rect.top

	def delete_account_button_collide(self,mouse_position):
		
		if self.delete_account_button.rect.collidepoint(mouse_position):
			self.play_click_sound()	
			self.stats.verification = True
			self.stats.pregame = True
			self.stats.mainpregame = False
			self.pass_entry.text = ''
			self.pass_entry.update('')

	def verification_button_collide(self,mouse_position):
		
		if self.verification_button.rect.collidepoint(mouse_position):
			self.play_click_sound()
			passw = self.pass_entry.text.encode('utf-8')
			if self.Db.check_login_data(self.username_entry.text,passw):
				self.Db.delete_user(self.username_entry.text)
			self.reset_pregame()
			self.stats.verification = False
			self.stats.pregame = True
			self.stats.mainpregame = True
			self.stats.game_choose = None

	def ADMIN_MODE_BUTTON_COLLIDE(self,mouse_position):
		self.play_click_sound()
		if self.go_admin_setting_button.rect.collidepoint(mouse_position):
			self.admin = True

	def go_Message_Collide(self,mouse_position):
		self.play_click_sound()
		if self.message_button.rect.collidepoint(mouse_position):
			self.message_screen_active = True

	def search_msg_button_collide(self,mouse_position):
		self.play_click_sound()
		if self.search_msg_button.rect.collidepoint(mouse_position):
			self.message_command = 'GET'

	def search_history_msg_button_collide(self,mouse_position):
		self.play_click_sound()
		if self.search_history_msg_button.rect.collidepoint(mouse_position):
			self.message_command = 'History'

	def text_to_button_collide(self,mouse_position):
		self.play_click_sound()
		if self.text_to_button.rect.collidepoint(mouse_position):
			self.message_command = 'text'

	def send_button_collide(self,mouse_position):
		if self.send_button.rect.collidepoint(mouse_position):
			if self.to_entry.text != 'ALL':
				if not self.Db.check_new_data(self.to_entry.text):
					if len(self.message_entry.text)>=1 :
						self.message_command = None
						self.MsgDb.savedata(self.player.ID,self.player.USERNAME,self.message_entry.text,self.to_entry.text,self.player.STATUS)
			else:
				if len(self.message_entry.text)>=1 :
					self.message_command = None
					self.MsgDb.savedata(self.player.ID,self.player.USERNAME,self.message_entry.text,self.to_entry.text,self.player.STATUS)
				




	#Sound Playing

	def play_click_sound(self):
		click_sound = pygame.mixer.Sound("GameProperty/Sound/clicked.wav")
		click_sound.set_volume(.05)
		click_sound.play()

	def play_hit_sound(self):
		hit_sound = pygame.mixer.Sound("GameProperty/Sound/hit_sound.wav")
		hit_sound.set_volume(.05)
		hit_sound.play()

	#Defactoring make stats
	def _pregame_screen(self):
		self._update_username_label()
		self._update_username_entry()
		self._update_pass_entry()
		self.backward_button.blit()

		if self.stats.verification:
			self._update_verification()

		else:

			if self.stats.game_choose == 'LOADGAME':
				self._update_login_button()

			elif self.stats.game_choose == 'NEWGAME':
				self._update_makenew_button()

	def _game_screen(self):
		if not self.GamePause:
			self.check_time()
			self.platform.moving_up()

			if self.boost == True:
				self.slime.stamina -= 5
			else:
				self.slime.stamina += 5

		self.my_platforms.draw(self.my_screen.screen)
		self._update_platforms()

		ScoreBoard(self)
		self.create_play_pause_button()


		if self.GamePause:
			self.quit_to_menu_button.draw() 
			self.quit_to_pregame_button.rect.y = self.quit_to_menu_button.rect.y + 100
			self.quit_to_pregame_button.draw()

	def run(self):
		print('USERNAME ADMIN = PROYEK ; PASS  ADMIN = pygame')
		while self.GameActivate:
			if not self.admin:
				self._check_events()	
				self._update_screen()
			else:
				self._update_screen()
				self.admindmin.mainloop()



	