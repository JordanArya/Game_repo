
class GameStats:
	def __init__(self):
		self.time = 0
		self.score = 0
		self.high_score = 0
		self.best_long_survive = 0
		self.life = 3
		self.pregame = True
		self.mainpregame = True
		self.game_choose = None
		self.choose_skin_win = False
		self.verification = False

	def reset(self):
		self.score = 0
		self.life = 3

	def _check_high_score(self):
		if self.score > self.high_score:
			self.high_score = self.score
			return True

	def _best_long_survive_check(self):
		if self.time > self.best_long_survive:
			self.best_long_survive = self.time
			return True



