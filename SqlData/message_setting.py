import sqlite3

class Settings:

	conn = sqlite3.connect('SqlData/message.db')
	cur = conn.cursor()

	cur.execute("""
		CREATE TABLE IF NOT EXISTS Message(
		id INTEGER ,
		Username TEXT,
		Message TEXT ,
		TO_User TEXT ,
		STATUS TEXT  )
		""")