import sqlite3
from SqlData.account import Account
from SqlData.message_setting import Settings
from datetime import datetime as dt

class Message:
	def __init__(self):

		self.settings = Settings()

	def savedata(self,ids,Username,message,to,status):

	#emp1 = Account(USERNAME = name,PASS = Pass)
		if len(message) <= 20:
			with self.settings.conn:
				self.settings.cur.execute("""INSERT INTO Message(id,Username,Message,TO_User,STATUS) VALUES (:id,:Username,:Message,:TO_User,:STATUS)""", {'id':ids,'Username':Username,'Message':message,'TO_User':to,'STATUS':status})


	def get_all_message(self,Username):
		data = self.get_message(Username)
		with self.settings.conn:
			self.settings.cur.execute("SELECT * FROM Message WHERE TO_User=:Username",{'Username':'ALL'})

		data2 = self.settings.cur.fetchall()
		if data2 != []:
			for all_data in data:
				data2.append(all_data)
			return data2
		else:
			return data

	def get_send_history(self,Username):
		with self.settings.conn:
			self.settings.cur.execute("SELECT * FROM Message WHERE Username=:Username",{'Username':Username})

		return self.settings.cur.fetchall()

	def get_message(self,Username):
		with self.settings.conn:
			self.settings.cur.execute("SELECT * FROM Message WHERE TO_User=:Username",{'Username':Username})

		return self.settings.cur.fetchall()

