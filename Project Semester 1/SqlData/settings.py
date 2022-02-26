import sqlite3

class Settings:

	conn = sqlite3.connect('SqlData/account.db')
	cur = conn.cursor()

	cur.execute("""
		CREATE TABLE IF NOT EXISTS Account(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		Username TEXT NOT NULL UNIQUE,
		Pass TEXT NOT NULL UNIQUE,
		BestScore INTEGER NOT NULL DEFAULT 0,
		Created TEXT NOT NULL DEFAULT '',
		LastPlaying TEXT NOT NULL DEFAULT '',
		ImagesIndex INTEGER NOT NULL DEFAULT 0,
		SurviveTime INTEGER NOT NULL DEFAULT 0,
		STATUS TEXT NOT NULL DEFAULT 'PLAYER')
		""")