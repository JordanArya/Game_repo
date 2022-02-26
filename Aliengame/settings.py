class Settings:
	def __init__(self):
		self.Title = 'ALIEN GAME'
		self.Screen_width = 600
		self.Screen_height = 400
		self.BG_COLOR = (230,230,230)

		#Ship Setting 
		self.SHIP_LIMIT = 5
		
		#Bullet Settings
		self.BULLETS_ALLOWED = 5
		self.BULLET_WIDTH = 100
		self.BULLET_HEIGHT = 15
		self.BULLET_COLOUR = (60,60,60)

		#Alien Settings
		self.ALIEN_DROP = 15
		"""
		#Rain Settings
		self.RAIN_COLOUR = (0,0,255)
		self.RAIN_WIDTH = 10
		self.RAIN_HEIGHT = 20
		self.RAIN_SPEED = 3
		self.BLACK_LIST_RAIN = None
		
		#Genagan settings
		self.GENANG_WIDTH = 15
		self.GENANG_HEIGHT = 10
		"""
		#Setting Rain
		#self.RAINDROP_SPEED = 2

		#Setting button
		self.BUTTON_WIDTH = 200
		self.BUTTON_HEIGHT = 50
		self.BUTTON_COLOR = (0,255,0)
		self.BUTTON_TEXT_COLOR = (255,255,255)
		self.BUTTON_FONT = None
		self.BUTTON_FONT_SIZE = 48

		#SCORE DISP SETTINGS
		self.SCORE_TEXT_COLOR = (30,30,30)
		self.SCORE_FONT = 'ariel'
		self.SCORE_FONT_SIZE = 20

		self.speed_scale = 1
		self.init_dynamic_settings()

	def init_dynamic_settings(self):
		self.ALIEN_POINTS = 50
		self.SHIP_SPEED = 5
		self.BULLET_SPEED = 3
		self.ALIEN_SPEED = 2

	def increase_speed(self):
		self.SHIP_SPEED *= self.speed_scale
		self.BULLET_SPEED *= self.speed_scale
		self.ALIEN_SPEED *= self.speed_scale
		self.ALIEN_POINTS *= self.speed_scale
