
class MainFrame():
	def __init__(self):
		self.method = "tkinter"
		self.widget_available  = False

	def run(self):
		
		from GameProperty.main_game import MainGame
		#if self.method == 'tkinter':
			#self.widget_available = True
			#self.widget = MainWidget(self)
			#self.widget.run()
			
		#else:
			#self.widget.quit()
			#from GameProperty.main_game import MainGame



		Game = MainGame(self)
		Game.run()
			#Aliengame.run()
		#from Aliengame.run import AlienGame 
			

		#Game = MainGame(self)
		#Game = AlienGame()
		#Game.run()
		
		"""
		widget = MainWidget(self)
		widget.run()
		"""
		
if __name__ == "__main__" :
	Frame = MainFrame()
	Frame.run()
	