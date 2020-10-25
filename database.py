import sqlite3
import os

class MusicDatabase:

	def __init__(self):
		self.db = None

	def doesDatabaseExist(self):

		# OBJECTIVE: Check if database exists. This function will stop music.addMusicToDatabase() from adding same songs on bootup.

		# Check if file exists
		return os.path.exists("Music.db")

	def createDatabase(self):

		# OBJECTIVE: Create a database if one doesn't exist

		# Create a new database and table
		self.db = sqlite3.connect("Music.db")
		self.db.execute("""CREATE TABLE music
							(Artist TEXT NOT NULL,
							Album TEXT NOT NULL,
							Song TEXT NOT NULL,
							Location TEXT NOT NULL PRIMARY KEY UNIQUE)"""
		)

	def connectToDatabase(self):

		# OBJECTIVE: Check whether or not database exists. If not, call another function to create one.

		# Connect to database
		if self.doesDatabaseExist():
			self.db = sqlite3.connect("Music.db")
		
		# Create a database
		else:
			self.createDatabase()

	def closeConnection(self):

		# NOTE: All connections to database must be closed
		self.db.close()

	def insert(self, artist, album, song, location):

		# OBJECTIVE: Insert new data to Music.db
		
		"""
		NOTE: 
		1. INSERT INTO music => Enter data into music table
		2. VALUES (?, ?, ?, ?) => Insert following values. Question marks were added to prevent SQL injection attack
		"""
		# Insert new information and commit it (save changes)
		self.db.execute("""INSERT INTO music
							VALUES (?, ?, ?, ?)""", (artist, album, song, location))
		self.db.commit()

	def printTable(self):

		# OBJECTIVE: Print table with cursor

		# Create a crusor
		cursor = self.db.execute("""SELECT * FROM music
									ORDER BY song""")

		# Print table
		for pos, row in enumerate(cursor):
			print("Pos #{}".format(pos))
			print("\t\tArtist: {}".format(row[0]))
			print("\t\tAlbum: {}".format(row[1]))
			print("\t\tSong: {}".format(row[2]))
			print("\t\tLocation: {}".format(row[3]))

	def printSongsAvailable(self):

		# OBJECTIVE: Print all songs inserted to database

		# Create a crusor
		cursor = self.db.execute("""SELECT song FROM music
									ORDER BY song""")

		# Only print "song" column
		for pos, row in enumerate(cursor):
			print("{}. {}".format(pos + 1, row[0]))

