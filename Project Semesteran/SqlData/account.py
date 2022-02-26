from datetime import datetime as dt

class Account:
	def __init__(self,USERNAME,PASS,ID=None,BEST_SCORE=0,created = dt.now(),last_played = dt.now(),images_index=0,Best_Survive_Time=0,STATUS='PLAYER'):
		self.ID = ID
		self.USERNAME = USERNAME
		self.PASS = PASS
		self.BEST_SCORE = BEST_SCORE
		self.created = created
		self.last_played = last_played
		self.images_index = images_index
		self.Best_Survive_Time = Best_Survive_Time
		self.STATUS = STATUS