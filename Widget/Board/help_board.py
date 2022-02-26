import tkinter as tk 

class Help_Board(tk.Tk):
	def __init__(self,parrent.App):
		self.App = App
		self.settings = App.settings

		super().__init__(parrent)

		self.configure(bg='pink')
		self.grid(column=0,row=0,sticky = 'nsew')
		self.grid_columnconfigure(0,weight = 1)
		self.grid_rowconfigure(0,weight = 1)


		Parrent.grid_rowconfigure(0,weight = 1)
		Parrent.grid_columnconfigure(0,weight = 1)

	def Create_Frame(self):
		pass

	def Create_How_To_Move_Frame(self):
		pass
