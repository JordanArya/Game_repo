import sqlite3

connection = sqlite3.connect('account.db') # conn
cursor = connection.cursor() # c/cur

cursor.execute("CREATE TABLE IF NOT EXISTS Account (Username  TEXT,Pass TEXT,BestScore INTEGER)")
connection.commit()

with connection:
	cursor.execute("""UPDATE Account SET STATUS=:STATUS WHERE Username=:Username""",{'STATUS':'ADMIN','Username':'PROYEK'})


connection.close()