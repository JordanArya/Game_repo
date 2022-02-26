import tkinter as tk
import sys
from PIL import Image,ImageTk


class StartBoard(tk.Frame):

	def __init__(self,App,Parrent):
		self.settings = App.settings
		self.APP = App

		super().__init__(Parrent)

		self.configure(bg = 'white')
		self.grid(column=0,row=0,sticky = 'nsew')
		self.grid_rowconfigure(0,weight=1)
		self.grid_columnconfigure(0,weight=1)

		Parrent.grid_rowconfigure(0,weight=1)
		Parrent.grid_columnconfigure(0,weight=1)

		self.make_window()


	def make_window(self):
		self._make_upper_board()
		self._make_middle_window()
		self._make_bottom_window()

	def make_picture(self):
		image = Image.open(self.settings.SLIME_IMAGES[self.settings.IMAGES_INDEX ])
		image_w,image_h = image.size
		ratio = image_w/self.settings.SCREEN_WIDTH*4
		image = image.resize((int(image_w/ratio),int(image_h/ratio)))

		self.SlimeImage = ImageTk.PhotoImage(image)


	def _make_upper_board(self):

		VirtualFrame = tk.Frame(self,height = self.settings.SCREEN_HEIGHT//4//2,bg='white')
		VirtualFrame.pack(fill='x')

		self.BackButton = tk.Button(VirtualFrame,command=self.Back_button_Command,width = 8,height=self.settings.SCREEN_HEIGHT//160,text = 'BACK',font=('arial',10))
		self.BackButton.pack(side='left')


		self.UpperFrame = tk.Frame(self,height = self.settings.SCREEN_HEIGHT//4,bg='white')
		self.UpperFrame.pack(fill='x')

		VirtualFrame = tk.Frame(self.UpperFrame,width=self.settings.SCREEN_WIDTH//4.5,bg='white')
		VirtualFrame.grid(column=0,row=0)

		self.StringVar = tk.StringVar()
		self.EnteryUser = tk.Entry(self.UpperFrame,font=('arial',int(self.settings.SCREEN_WIDTH//15)),bg='white',textvariable= self.StringVar,width = 11)
		self.EnteryUser.grid(column=1,row=1, sticky='nsew')

	def _make_middle_window(self):
		VirtualFrame = tk.Frame(self,height = self.settings.SCREEN_HEIGHT//30,bg='white')
		VirtualFrame.pack(fill='x')

		self.LabelError = tk.Label(VirtualFrame ,fg = 'blue',bg='white',font=('Ink Free',12),text='Insert less then 11')
		self.LabelError.pack(fill='x')

		self.middle_Frame = tk.Frame(self,height=self.settings.SCREEN_HEIGHT//2,bg='white')
		self.middle_Frame.pack(fill='x')

		VirtualFrame = tk.Frame(self.middle_Frame,width=self.settings.SCREEN_WIDTH//4.5,bg='white')
		VirtualFrame.grid(column=0,row=0)

		self.Backward_button = tk.Button(self.middle_Frame,bg = 'grey',width=self.settings.SCREEN_WIDTH//51,command=self.MoveBackWard)
		self.Backward_button.grid(row=0,column=1,sticky='ns')

		self.make_picture()

		self.SlimeImages = tk.Label(self.middle_Frame,bg='white',image = self.SlimeImage)
		self.SlimeImages.grid(row=0,column=2,sticky='ns')

		self.Frontward_button = tk.Button(self.middle_Frame,bg = 'grey',width=self.settings.SCREEN_WIDTH//51,command= self.MoveForward)
		self.Frontward_button.grid(row=0,column=3,sticky='ns')

	def _make_bottom_window(self):
		VirtualFrame = tk.Frame(self,height = self.settings.SCREEN_HEIGHT//10,bg='white')
		VirtualFrame.pack(fill='x')

		self.bottom_Frame = tk.Frame(self,bg='black')
		self.bottom_Frame.pack(expand=True)

		self.Start_Button = tk.Button(self.bottom_Frame,font=('arial',40),text='START',width=int(self.settings.SCREEN_WIDTH//22.5),bd=0,bg='white',command=self.StartCommand)
		self.Start_Button.pack(expand=True)

	#Button Command
	def MoveForward(self):

		Maximum = len(self.settings.SLIME_IMAGES) - 1
		
		if self.settings.IMAGES_INDEX  >= Maximum:
			self.Frontward_button.configure(command = lambda:None)
		
		else:
			self.settings.IMAGES_INDEX  += 1
			self.make_picture()
			self.SlimeImages.configure(image = self.SlimeImage)
			self.Backward_button.configure(command = self.MoveBackWard)

	def MoveBackWard(self):

		if self.settings.IMAGES_INDEX  <= 0:
			self.Backward_button.configure(command = lambda:None)
		
		else:
			self.settings.IMAGES_INDEX  -= 1
			self.make_picture()
			self.SlimeImages.configure(image = self.SlimeImage)
			self.Frontward_button.configure(command=self.MoveForward)

	def StartCommand(self):

		PLAYER_NAME = self.StringVar.get()
		if len(PLAYER_NAME) > 11:
			self.EnteryUser.configure(text=None)
			self.LabelError.configure(text = "please Insert less then 11 word")
			self.LabelError.pack(fill='x')
		else:
			self.settings.PLAYER_NAME = PLAYER_NAME
			self.APP.Parrent.method = 'pygame'
			self.APP.Parrent.widget_available = False
			self.APP.Parrent.run()
			

	def Back_button_Command(self):
		self.destroy()
		self.APP.play_pages()









