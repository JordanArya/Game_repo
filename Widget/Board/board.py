import tkinter as tk
from tkinter import Tk 
from PIL import Image,ImageTk

class MainPage(tk.Frame):

	def __init__(self,App,Parrent):
		
		self.APP = App
		self.settings = App.settings
		self.Parrent_frame = Parrent

		super().__init__(Parrent)
		self.configure(bg='white')
		self.grid(column = 0,row = 0, sticky = 'nsew')
		self.grid_rowconfigure(0,weight=1)
		self.grid_columnconfigure(0,weight=1)

		Parrent.grid_rowconfigure(0,weight = 1)
		Parrent.grid_columnconfigure(0,weight = 1)

		self.Create_Frame()

	def Create_Frame(self):
		self.create_Frame()
		self.create_middle_Frame()
		self.create_Bottom_Frame()
		
	def create_Frame(self):
		
		self.Help_Logo = self.make_picture(self.settings.Help_Icon,ratio=25,index=None)

		self.GearLogo =  self.make_picture(self.settings.Gear_Icon,ratio=15,index=None)

		self.UpHeading = tk.Frame(self,bg='black',height=self.settings.SCREEN_HEIGHT//6,width=self.settings.SCREEN_WIDTH)
		self.UpHeading.pack(fill='x')

		self.Icon_Frame = tk.Frame(self.UpHeading,bg = 'white')
		self.Icon_Frame.grid(column=0,row=0,sticky='wns')


		self.HelpIcon = tk.Button(self.Icon_Frame,image = self.Help_Logo,bd = 0,bg = 'white')
		self.HelpIcon.grid(row=0,column=0,sticky='sne')

		self.virtual_image = tk.PhotoImage(width=1,height=1)

		Virtual_Board = tk.Frame(self.UpHeading,bg='white',width=self.settings.SCREEN_WIDTH//5.1)
		Virtual_Board.grid(column=1,row=0,sticky='nsew')

		self.TitleFrame = tk.Frame(self.UpHeading,bg='green')
		self.TitleFrame.grid(column=2,row=0)

		self.Title_label = tk.Label(self.TitleFrame,text = "Jumping Slime",font=('Ink Free',int(self.settings.SCREEN_WIDTH//30)),width = self.settings.SCREEN_WIDTH//2,height = self.settings.SCREEN_HEIGHT//6,image = self.virtual_image,compound='c',bg='white')

		self.Title_label.grid(row=0,column=0,sticky='wn')

		Virtual_Board = tk.Frame(self.UpHeading,bg='white',width=self.settings.SCREEN_WIDTH//5.1)
		Virtual_Board.grid(column=3,row=0,sticky='nsew')

		self.SettingLogoFrame = tk.Frame(self.UpHeading,bg='white')
		self.SettingLogoFrame.grid(column=4,row=0,sticky='ens')

		self.GearIcon = tk.Button(self.SettingLogoFrame,image= self.GearLogo,bd = 0 ,bg = 'white',command = self.SettingButton_Command)
		self.GearIcon.grid(row=0,column=0,sticky='snw')

	def create_middle_Frame(self):
		self.settings.IMAGES_INDEX = 1

		Virtual_Board = tk.Frame(self,bg=('skyblue'),width=self.settings.SCREEN_WIDTH,height=self.settings.SCREEN_HEIGHT//3//2)
		Virtual_Board.pack()


		self.middleHeading = tk.Frame(self,bg='blue')
		self.middleHeading.pack(fill='x')

		self.Start_Button = tk.Button(self.middleHeading,font=("Comic Sans MS",int(self.settings.SCREEN_WIDTH//30)),text = "Start Game",width = int(self.settings.SCREEN_WIDTH//22.5),bg='skyblue',fg='Black',bd = 0,command = self.StartButton_command)
		self.Start_Button.pack(side='top',fill='x')


		self.middleHeading.grid_rowconfigure(0,weight=1)
		self.middleHeading.grid_columnconfigure(1,weight=1)	

	def create_Bottom_Frame(self):
		self.settings.IMAGES_INDEX = 0
		self.SlimeImage = self.make_picture(self.settings.SLIME_IMAGES,1,10)
		Virtual_Board = tk.Frame(self,bg='skyblue',width=self.settings.SCREEN_WIDTH,height=self.settings.SCREEN_HEIGHT//3//2)
		Virtual_Board.pack(fill='x')

		self.Virtual_Label = tk.Label(Virtual_Board,image = self.SlimeImage,bg = 'skyblue',height=self.settings.SCREEN_HEIGHT//3//2)
		self.Virtual_Label.grid(sticky = 's')

		self.BottomHeading = tk.Frame(self,bg ='Black')
		self.BottomHeading.pack(fill='x')

		self.Stats_Button = tk.Button(self.BottomHeading,text='Game Stats',font=("Comic Sans MS",int(self.settings.SCREEN_WIDTH//45)),bg ='white',bd= 0,width=int(self.settings.SCREEN_WIDTH//22.5))
		self.Stats_Button.pack(fill='x')

	def make_picture(self,images,index ,ratio):
		indexs = index
		if indexs:
			image = Image.open(images[index])
		elif not indexs:
			image = Image.open(images)

		image_w,image_h = image.size
		ratio = image_w/self.settings.SCREEN_WIDTH*ratio
		image = image.resize((int(image_w/ratio),int(image_h/ratio)))

		return ImageTk.PhotoImage(image)

	#Button Command
	def StartButton_command(self):
		self.destroy()
		self.APP.start_pages()

	def SettingButton_Command(self):
		self.destroy()
		self.APP.setting_pages()




