import tkinter as tk
from tkinter import *
from tkinter import ttk


class SettingBoard(tk.Frame):
	def __init__(self,App,Parrent):
		self.App = App
		self.settings = self.App.settings

		super().__init__(Parrent)

		self.configure(bg='pink')
		self.grid(column=0,row=0,sticky = 'nsew')
		self.grid_columnconfigure(0,weight = 1)
		self.grid_rowconfigure(0,weight = 1)


		Parrent.grid_rowconfigure(0,weight = 1)
		Parrent.grid_columnconfigure(0,weight = 1)

		self.create_frame()

	def create_frame(self):
		self.make_upper_frame()
		self.make_middle_frame()
		self.make_Screen_Resolution_setting_frame()
		self.make_buttom_Frame()


	def make_upper_frame(self):
		VirtualFrame = tk.Frame(self,height = self.settings.SCREEN_HEIGHT//4//2,bg='white')
		VirtualFrame.pack(fill='x')

		self.BackButton = tk.Button(VirtualFrame,command=self.Back_button_Command,width = int(self.settings.SCREEN_WIDTH//112.5),height=self.settings.SCREEN_HEIGHT//160,text = 'BACK',font=('arial',10))
		self.BackButton.pack(side='left')

		self.UpperFrame = tk.Frame(self,height = self.settings.SCREEN_HEIGHT//8,bg='white')
		self.UpperFrame.pack(fill='x')

		self.CodeLabel = tk.Label(self.UpperFrame,font=('arial',30),text = 'Code : ',width=self.settings.SCREEN_WIDTH//80,bg='white')
		self.CodeLabel.grid(sticky='e')

		self.Code_StringVar = tk.StringVar()

		self.Codeentry = tk.Entry(self.UpperFrame,font=('arial',30),width =int(self.settings.SCREEN_WIDTH//45),bg='white',textvariable = self.Code_StringVar)
		self.Codeentry.grid(row = 0,column= 1,sticky='ns')

		self.entryButton = tk.Button(self.UpperFrame,font=('arial',30),bg='white',bd = 0,text='Enter',width=int(self.settings.SCREEN_WIDTH//112.5))
		self.entryButton.grid(row=0,column=2,sticky='ns')

	def make_middle_frame(self):
		VirtualFrame = tk.Frame(self,height = self.settings.SCREEN_HEIGHT//20,bg='white')
		VirtualFrame.pack(fill='x')

		self.ControlOptionFrame = tk.Frame(self,bg='white')
		self.ControlOptionFrame.pack(fill='x')

		self.ControlLabel = tk.Label(self.ControlOptionFrame,font=('arial',30),text = 'Control : ',width=self.settings.SCREEN_WIDTH//80,bg='white')
		self.ControlLabel.grid(sticky='e')

		ControlOptions = ['WASD','Arrow Button']

		self.ControlOption = ttk.Combobox(self.ControlOptionFrame,width=self.settings.SCREEN_WIDTH//10,text = ('Arial',60),height=self.settings.SCREEN_HEIGHT//10)
		self.ControlOption['values'] = ControlOptions
		self.ControlOption.current(0)
		self.ControlOption.grid(row=0 , column=1,sticky='w')


	def make_Screen_Resolution_setting_frame(self):
		VirtualFrame = tk.Frame(self,height = self.settings.SCREEN_HEIGHT//20,bg='white')
		VirtualFrame.pack(fill='x')

		self.Screen_Resolution_Setting_Frame = tk.Frame(self,bg='white')
		self.Screen_Resolution_Setting_Frame.pack(fill='x')

		self.Screen_Resolution_Setting_Label = tk.Label(self.Screen_Resolution_Setting_Frame,font=('arial',30),text = 'Resolution :  ',width=self.settings.SCREEN_WIDTH//80,bg='white')
		self.Screen_Resolution_Setting_Label.grid(column=0,row=0)

		self.Screen_Resolution_Combobox = ttk.Combobox(self.Screen_Resolution_Setting_Frame,font=('arial',30),width=self.settings.SCREEN_WIDTH//80)
		self.Screen_Resolution_Combobox.grid(column=1,row=0,sticky='w')
		self.Screen_Resolution_Combobox['values'] = self.settings.SCREEN_OPTION 

		self.Screen_Resolution_Combobox.bind('<<ComboboxSelected>>',self.Change_Resolution)

	def make_buttom_Frame(self):
		VirtualFrame = tk.Frame(self,height = self.settings.SCREEN_HEIGHT//5,bg='white')
		VirtualFrame.pack(fill='x')

		self.Buttom_Frame = tk.Frame(self,bg='white')
		self.Buttom_Frame.pack(fill='x')

		self.Reset_Button = tk.Button(self.Buttom_Frame,font=('arial',30),text = 'Reset',width=self.settings.SCREEN_WIDTH//80,bg='white',bd=0,command = self.reset_setting)
		self.Reset_Button.grid(column=0,row=0)

		self.Apply_Button = tk.Button(self.Buttom_Frame,font=('arial',30),text = 'Apply',width=self.settings.SCREEN_WIDTH//80,bg='white',bd=0)
		self.Apply_Button.grid(column=1,row=0)
		
	#Command 

	def Back_button_Command(self):
		self.destroy()
		self.App.play_pages()

	def print_data(self):
		Data = self.ControlOption.get()
		print(Data)

	def Change_Resolution(self,event):
		Screen_index = self.Screen_Resolution_Combobox.current()
		self.Change_Screen(Screen_index)

	def reset_setting(self):
		Screen_index = 0
		self.Change_Screen(Screen_index)	
		
	def Change_Screen(self,Screen_index):

		if Screen_index == 3:
			self.App.resizable(1,1)
		else:
			self.App.resizable(0,0)

		self.settings.CHANGE_SCREEN_RESOLUTION(Screen_index)
		self.App.geometry(self.settings.SCREEN_CONFIGURATION)
		self.App.setting_pages()
		self.quit()



		
		
