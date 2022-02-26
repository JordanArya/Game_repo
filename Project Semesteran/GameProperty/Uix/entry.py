import pygame

from GameProperty.Uix.button import Button 

class Entry(Button):

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.text = ''
		self.active = False
		self.font_file = self.settings.ENTRY_FONT
		self.color = self.settings.ENTRY_TEXT_COLOR_INACTIVE 

	def update(self,text):
		self.text_to_image(text)