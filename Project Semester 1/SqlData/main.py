import sqlite3
from SqlData.account import Account
from SqlData.settings import Settings
from datetime import datetime as dt
import bcrypt

class SaveData:
	def __init__(self):

		self.settings = Settings()

	def savedata(self,name,Pass,BestScore=0):

		emp1 = Account(USERNAME = name,PASS = Pass)

		with self.settings.conn:
					self.settings.cur.execute("""INSERT INTO Account(Username,Pass,BestScore,Created,LastPlaying) VALUES (:Username,:Pass,:BestScore,:Created,:LastPlaying)""", {'Username':emp1.USERNAME,'Pass':emp1.PASS,'BestScore':emp1.BEST_SCORE,'Created':emp1.created, 'LastPlaying':emp1.last_played })

	#ADMIN FUNCTION
	def get_all_data(self):
		with self.settings.conn:
			self.settings.cur.execute("SELECT * FROM Account")

		return self.settings.cur.fetchall()

	def getdata(self,Username):
		with self.settings.conn:
			self.settings.cur.execute("SELECT * FROM Account WHERE Username=:Username",{'Username':Username})

		return self.settings.cur.fetchone()

	def check_login_data(self,Username,Pass):		
	
		data = self.getdata(Username)
		if data:
			if Username == data[1] and bcrypt.checkpw(Pass,data[2]):
				return data

			return 

	def check_new_data(self,Username):
		data = self.getdata(Username)

		if data:
			return False

		return True

	def update_last_play(self,Username,lastplay):
		with self.settings.conn:
			self.settings.cur.execute("""UPDATE Account SET LastPlaying=:LastPlaying WHERE Username=:Username""",{'LastPlaying':lastplay,'Username':Username})

	def update_high_score(self,Username,high_score):
		with self.settings.conn:
			self.settings.cur.execute("""UPDATE Account SET BestScore=:high_score WHERE Username=:Username""",{'high_score':high_score,'Username':Username})

	def update_images_index(self,Username,images_index):
		with self.settings.conn:
			self.settings.cur.execute("""UPDATE Account SET ImagesIndex=:ImagesIndex WHERE Username=:Username""",{'ImagesIndex':images_index,'Username':Username})

	def delete_user(self,Username):
		with self.settings.conn:
			self.settings.cur.execute("DELETE FROM Account WHERE Username=:Username",{'Username':Username})
			

	def update_long_survive(self,Username,Long_survive):
		with self.settings.conn:
			self.settings.cur.execute("UPDATE Account SET SurviveTime=:SurviveTime WHERE Username=:Username",{'SurviveTime':Long_survive,'Username':Username})


		






