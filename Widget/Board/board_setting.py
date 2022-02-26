

class Settings:
	def __init__(self):
	#Screen Settings
	#base = 100
	#ratio = (9, 6)
	#SCREEN_WIDTH = base*ratio[0]
	#SCREEN_HEIGHT = base*ratio[1]
		self.SCREEN_OPTION = [(800,'x',600),(1280,'x',800),(1366,'x',728),(1558,'x',868)]
		
		self.SCREEN_WIDTH = self.SCREEN_OPTION[0][0]
		self.SCREEN_HEIGHT = self.SCREEN_OPTION[0][2]

		self.Check_ratio()
		

		self.SCREEN_CONFIGURATION = f"{self.SCREEN_WIDTH}x{self.SCREEN_HEIGHT}+{self.width_ratio}+{self.height_ratio}"
		self.GAME_TITLE = "Jumping Slime"
		
		#ICon
		self.Help_Icon = 'Widget/assets/Help_Icon.JPG'
		self.Gear_Icon = 'Widget/assets/Gear.JPG'

		#StartBoard Images:
		self.SLIME_IMAGES = ('Widget/assets/Slime.PNG','Widget/assets/Slime1.PNG','Widget/assets/Slime2.PNG','Widget/assets/Slime3.PNG')
		self.IMAGES_INDEX = 0
		self.PLAYER_NAME = None
	

	#Method

	def Check_ratio(self):
		if self.SCREEN_HEIGHT >= 800:
			self.height_ratio = 0
		else:
			self.height_ratio = 30

		if self.SCREEN_WIDTH >= 1558:
			self.width_ratio = 0
		elif self.SCREEN_WIDTH >= 1280:
			self.width_ratio = 140
		else:
			self.width_ratio = 350

	def CHANGE_SCREEN_RESOLUTION(self,SCREEN_INDEX):
		self.SCREEN_WIDTH = self.SCREEN_OPTION[SCREEN_INDEX][0]
		self.SCREEN_HEIGHT = self.SCREEN_OPTION[SCREEN_INDEX][2]

		self.Check_ratio()
	
		self.SCREEN_CONFIGURATION = f"{self.SCREEN_WIDTH}x{self.SCREEN_HEIGHT}+{self.width_ratio}+{self.height_ratio}"
	

