from GameProperty.Uix.label import Label
import pygame
class Message_Screen():
	def __init__(self,parrent):
		self.app = parrent
		self.app.settings.LABEL_FONT_SIZE = 40
		self.From_label = Label(parrent,'From')
		self.Message_label = Label(parrent,"Message")
		self.To_label = Label(parrent,'TO')

		self.Labels = pygame.sprite.Group()

	def make_message_screen(self,data,form):
		self.Labels.empty()
		if form == "GET":
			self.make_From_label('GET')
		else:
			self.make_From_label(form)
		for steps in range(len(data)):
			for step in range(2):
				if step == 0:
					if form == 'GET':
						from_user = data[steps][1]
					else:
						from_user = data[steps][3]
					self.app.settings.LABEL_FONT_SIZE = 30
					Labels = Label(self.app,str(from_user))
					Labels.rect.center = self.From_label.rect.center
					Labels.rect.x = self.From_label.rect.x
					Labels.rect.y = self.From_label.rect.y

				else:
					message = data[steps][2]
					self.app.settings.LABEL_FONT_SIZE = 30
					Labels = Label(self.app,str(message))
					Labels.rect.center = self.Message_label.rect.center
					Labels.rect.x = self.Message_label.rect.x
					Labels.rect.y = self.Message_label.rect.y
					

				Labels.rect.y += (steps+1)*30
				self.Labels.add(Labels)

		self.Labels.draw(self.app.my_screen.screen)


	def make_From_label(self,form):
		#self.app.settings.LABEL_FONT_SIZE = 30
		self.From_label.rect.topleft = self.app.my_screen.rect.topleft
		self.From_label.rect.x += 20
		self.From_label.rect.y += 60
		self.To_label.rect.topleft = self.app.my_screen.rect.topleft
		self.To_label.rect.x += 20
		self.To_label.rect.y += 60
		if form == "GET":
			self.From_label.blit()
		else:
			self.To_label.blit()


		self.Message_label.rect.topright = self.app.my_screen.rect.topright
		self.Message_label.rect.x -= 150
		self.Message_label.rect.y += 60
		self.Message_label.blit()
		
