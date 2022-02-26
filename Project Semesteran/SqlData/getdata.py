import sqlite3

connection = sqlite3.connect('account.db') # conn
cursor = connection.cursor() # c/cur

#cursor.execute("CREATE TABLE IF NOT EXISTS Account (Username  TEXT,Pass TEXT,BestScore INTEGER)")
connection.commit()

query = """
			SELECT * FROM Account
		"""

cursor.execute(query)
emp = cursor.fetchall()

print(emp)

#connection.commit()
connection.close()

"""
INSERT INTO employees VALUES('me','you',1000)
"""