import tkinter as tk
from tkinter import Tk
import sys

from Widget.Board.board_setting import Settings
from Widget.Board.board import  MainPage
from Widget.Board.start_board import StartBoard
from Widget.Board.setting_boards import SettingBoard

class MainWidget(Tk):
	
	def __init__(self,Parrent):
		self.settings = Settings()
		self.Parrent = Parrent

		super().__init__()
		
		self.geometry(self.settings.SCREEN_CONFIGURATION)
		self.title(self.settings.GAME_TITLE)
		
		self.resizable(0,0)

		self.pages = {}
		self.create_container()
		self.play_pages()

	def create_container(self):
		self.container = tk.Frame(self,bg = 'black')
		self.container.pack(fill="both", expand=True)

	def play_pages(self):
		self.pages['MainPage'] = MainPage(self,self.container)


	def start_pages(self):
		self.pages['StartBoard'] = StartBoard(self,self.container)

	def setting_pages(self):
		self.pages['SettingsBoard'] = SettingBoard(self,self.container)

	def run(self):
		self.mainloop()





