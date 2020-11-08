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
							Location TEXT NOT NULL UNIQUE,
							Pos INTEGER)"""
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

		# Connect to database
		self.connectToDatabase()

		try:
			# Insert new information and commit it (save changes)
			self.db.execute("""INSERT INTO music VALUES (?, ?, ?, ?, ?)""", (artist, album, song, location, 0))
			self.db.commit()
		except sqlite3.IntegrityError as err:
			print("Duplicate entry! Error: {}".format(err))

		# Disconnect from database
		self.db.close()

	def reorganizeDatabase(self):

		# OBJECTIVE: Sort database by Song and create a new column labeled index

		# Connect to database
		self.connectToDatabase()

		# Create a cursor and execute sqlite command
		rows = self.db.execute("""SELECT * FROM music ORDER BY Song""")

		# Update index columns
		for indx, row in enumerate(rows):
			self.db.execute("""UPDATE music
								SET Pos=(?)
								WHERE Location=(?)""", (indx, row[3]))

		# Save changes
		self.db.commit()

		# Disconnect from database
		self.db.close()

	def getSongByName(self, name):

		# OBJECTIVE: Based on song's name, return song's pathname.

		# Connect to database
		self.connectToDatabase()
		
		# Create a cursor and execute sqlite command
		row = self.db.execute("""SELECT Song, Location, Pos
								FROM music
								WHERE Song=(?)""", (name,)) # <= Need to make it into a tuple and add a comma

		# If data wasn't found, return
		if row == None:
			print("Song doesn't exist!") 

		else:
			# Save data from row before disconnection from server
			# NOTE: fetchone => execute() returns all rows meeting the criteria. fetchone() gets the 1st row
			# 		Also, fetchone() returns a tuple (name, pathname)
			row = row.fetchone()

		# Disconnect from database and return output
		self.db.close()
		return row

	def getSongByPos(self, pos):

		# OBJECTIVE: Return a nearby song if a user selects Forward or Rewind

		# Connect to database
		self.connectToDatabase()
		
		# Create a cursor and execute sqlite command
		# If Pos is out of bounds, then it's non-existent so return the 1st song as default value
		row = self.db.execute("""SELECT Song, Location, Pos
								FROM music
								WHERE Pos=(?)""", (pos,)) # <= Need to make it into a tuple and add a comma

		# Save data from row before disconnection from server
		# NOTE: fetchone => execute() returns all rows meeting the criteria. fetchone() gets the 1st row
		# 		Also, fetchone() returns a tuple (name, pathname)
		row = row.fetchone()

		# If data wasn't found, return
		if row == None:
			print("Song doesn't exist!")

			# Create a cursor and get 1st row as default value
			row = self.db.execute("""SELECT Song, Location, Pos
									FROM music
									WHERE Pos=0""")
			row = row.fetchone()
			

		# Disconnect from database and return output
		self.db.close()
		return row

	def printTable(self):

		# OBJECTIVE: Print table with cursor

		# Connect to database
		self.connectToDatabase()

		# Create a cursor
		cursor = self.db.execute("""SELECT * FROM music
									ORDER BY Song""")

		# Print table
		for pos, row in enumerate(cursor):
			print(row)

		# Disconnect from database
		self.db.close()

	def printSongsAvailable(self):

		# OBJECTIVE: Print all songs inserted to database

		# Connect to database
		self.connectToDatabase()

		# Create a crusor
		cursor = self.db.execute("""SELECT Song FROM music
									ORDER BY Song""")

		# Only print "song" column
		for pos, row in enumerate(cursor):
			print("{}. {}".format(pos + 1, row[0]))

		# Disconnect from database
		self.db.close()
