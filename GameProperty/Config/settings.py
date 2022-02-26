#from Widget.Board.board_setting import Settings

class Settings():

		
	SCREEN_OPTION = [(400,'x',650),(800,'x',600),(1280,'x',800),(1366,'x',728),(1558,'x',868)]
	
	SCREEN_WIDTH = SCREEN_OPTION[0][0]
	SCREEN_HEIGHT = SCREEN_OPTION[0][2]
	BG_SCREEN = 'GameProperty/Assets/bg.png'

	#self.SCREEN_CONFIGURATION = f"{self.SCREEN_WIDTH}x{self.SCREEN_HEIGHT}+{self.width_ratio}+{self.height_ratio}"
	#self.GAME_TITLE = "Jumping Slime"
	
	#ICon
	#self.Help_Icon = 'Widget/assets/Help_Icon.JPG'
	#self.Gear_Icon = 'Widget/assets/Gear.JPG'

	#StartBoard Images:
	STAND_SLIME_IMAGES = ('GameProperty/Assets/SLIME_STAND_ASSET/standblue.png','GameProperty/Assets/SLIME_STAND_ASSET/standgreen.png','GameProperty/Assets/SLIME_STAND_ASSET/standorange.png','GameProperty/Assets/SLIME_STAND_ASSET/standpurple.png','GameProperty/Assets/SLIME_STAND_ASSET/standsilver.png')

	SLIME_WALK_LEFT = ('GameProperty/Assets/SLIME_WALK_ASSET_LEFT/walkleftblue.png','GameProperty/Assets/SLIME_WALK_ASSET_LEFT/walkleftgreen.png','GameProperty/Assets/SLIME_WALK_ASSET_LEFT/walkleftorange.png','GameProperty/Assets/SLIME_WALK_ASSET_LEFT/walkleftpurple.png','GameProperty/Assets/SLIME_WALK_ASSET_LEFT/walkleftsilver.png')

	SLIME_WALK_RIGHT = ('GameProperty/Assets/SLIME_WALK_ASSET_RIGHT/walkrightblue.png','GameProperty/Assets/SLIME_WALK_ASSET_RIGHT/walkrightgreen.png','GameProperty/Assets/SLIME_WALK_ASSET_RIGHT/walkrightorange.png','GameProperty/Assets/SLIME_WALK_ASSET_RIGHT/walkrightpurple.png','GameProperty/Assets/SLIME_WALK_ASSET_RIGHT/walkrightsilver.png')

	SLIME_DASH_LEFT = ('GameProperty/Assets/SLIME_DASH_ASSET_LEFT/dashleftblue.PNG','GameProperty/Assets/SLIME_DASH_ASSET_LEFT/dashleftgreen.png','GameProperty/Assets/SLIME_DASH_ASSET_LEFT/dashleftorange.png','GameProperty/Assets/SLIME_DASH_ASSET_LEFT/dashleftpurple.png','GameProperty/Assets/SLIME_DASH_ASSET_LEFT/dashleftsilver.png')

	SLIME_DASH_RIGHT = ('GameProperty/Assets/SLIME_DASH_ASSET_RIGHT/dashrightblue.PNG','GameProperty/Assets/SLIME_DASH_ASSET_RIGHT/dashrightgreen.png','GameProperty/Assets/SLIME_DASH_ASSET_RIGHT/dashrightorange.png','GameProperty/Assets/SLIME_DASH_ASSET_RIGHT/dashrightpurple.png','GameProperty/Assets/SLIME_DASH_ASSET_RIGHT/dashrightsilver.png')

	SLIME_JUMP = ('GameProperty/Assets/SLIME_JUMP_ASSET/jumpblue.PNG','GameProperty/Assets/SLIME_JUMP_ASSET/jumpgreen.png','GameProperty/Assets/SLIME_JUMP_ASSET/jumporange.png','GameProperty/Assets/SLIME_JUMP_ASSET/jumppurple.png','GameProperty/Assets/SLIME_JUMP_ASSET/jumpsilver.png')

	IMAGES_INDEX = 0
	PLAYER_NAME = None
	
	PLATFORM = ('GameProperty/Assets/platform.PNG')
	BRICK_PLATFORM = ('GameProperty/Assets/platform2.png')
	SPICKY_PLATFORM = ('GameProperty/Assets/platform3.png')
	BRICK_PLATFORM_SMALL =  ('GameProperty/Assets/small_size.png')

	BOOST = False

	SCORE_FONT = "ariel"
	SCORE_TEXT_COLOR = (255,255,255)
	SCORE_FONT_SIZE = 40

	#BUTTON(UIX) CONFIGURATION
	BUTTON_WIDTH = SCREEN_WIDTH//2.1
	BUTTON_HEIGHT = SCREEN_HEIGHT//12
	BUTTON_PICTURE = ['GameProperty/Assets/playbutton.png','GameProperty/Assets/pausebutton.png']

	#SOUND CONFIGURATION
	SOUND_VOLUME = [0.05,0.07,0.1,0]
	SOUND_PICTURE = ['GameProperty/Assets/unpausesoundbutton.png','GameProperty/Assets/sound2.png','GameProperty/Assets/sound 3.png','GameProperty/Assets/pausesound.PNG']

	#ENTRY CONFIGURATION
	ENTRY_FONT = 'ariel'
	ENTRY_TEXT_COLOR_ACTIVE = (255,0,0)
	ENTRY_TEXT_COLOR_INACTIVE =  (122, 255, 0)
	ENTRY_FONT_SIZE = 40

	#Label Configuration
	LABEL_FONT = 'ariel'
	LABEL_FONT_COLOR = (255,255,255)
	LABEL_FONT_SIZE = 40

	#Back Button Configuration
	BACK_BUTTON_PICTURE = 'GameProperty/Assets/back.png'
	BACK_BUTTON_WIDTH = int(SCREEN_WIDTH//6)
	BACK_BUTTON_HEIGHT = int(SCREEN_HEIGHT//12)