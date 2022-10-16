import sqlite3
import api

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE)
cur = db.cursor()

cur.execute("""
	CREATE TABLE IF NOT EXISTS users(
	  id INTEGER PRIMARY KEY,
	  username TEXT,
	  password TEXT)""")

cur.execute("""
	CREATE TABLE IF NOT EXISTS entries(
	  title TEXT,
	  user_id INTEGER,
	  entry TEXT)""") #user with user_id can edit cuz they're the author

db.commit()
db.close()