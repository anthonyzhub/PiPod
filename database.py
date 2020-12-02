import sqlite3
import os

class MusicDatabase:

	def __init__(self):

		# Separate databases for artists, albums, and all songs
		self.allSongsDB = None

	def doesDatabaseExist(self):

		# OBJECTIVE: Check if database exists. This function will stop music.addMusicToDatabase() from adding same songs on bootup.

		# Check if file exists
		return os.path.exists("allSongs.db")

	def createDatabase(self):

		# OBJECTIVE: Create a databases if either one or all don't exist

		self.allSongsDB = sqlite3.connect("allSongs.db")
		self.allSongsDB.execute("""CREATE TABLE music
							(Artists TEXT NOT NULL,
							Album TEXT NOT NULL,
							AlbumPos INTEGER NOT NULL,
							Song TEXT NOT NULL,
							LibraryPos INTEGER,
							Location TEXT NOT NULL UNIQUE)"""
		)

	def connectToDatabase(self):

		# OBJECTIVE: Check whether or not database exists. If not, call another function to create one.

		# Connect to database
		if self.doesDatabaseExist():
			self.allSongsDB = sqlite3.connect("allSongs.db")
		
		# Create a database
		else:
			self.createDatabase()

	def closeConnection(self):

		# NOTE: All connections to database must be closed
		self.allSongsDB.close()

	def insert(self, artist, album, song, location):

		# OBJECTIVE: Insert new data to allSongs.db
		
		"""
		NOTE: 
		1. INSERT INTO music => Enter data into music table
		2. VALUES (?, ?, ?, ?) => Insert following values. Question marks were added to prevent SQL injection attack
		"""

		# Connect to database
		self.connectToDatabase()

		def getNumber(string):

			# OBJECTIVE: A small helper function used to fetch first few numbers of song's filename

			# Create blank string
			number = ""

			# Iterate string for numbers
			for pos, i in enumerate(string):

				# Once letter or whitespace is reached, exit for-loop
				if i.isalpha() or i == " ":
					break

				number += i

			# Cast variable to int
			if number != "":
				number = int(number)

			# Cut string
			string = string[pos:]

			return (number, string)

		try:
			
			# Parse album order and file extension from "song"
			albumOrder, song = getNumber(song)
			songExt = song[-4:]
			song = song[:-4]

			# Insert new information and commit it (save changes)
			self.allSongsDB.execute("""INSERT INTO music VALUES (?, ?, ?, ?, ?, ?)""", (artist, album, albumOrder, song, 0, location))
			self.allSongsDB.commit()

		except sqlite3.IntegrityError as err:
			print("Duplicate entry! Error: {}".format(err))

		# Disconnect from database
		self.allSongsDB.close()

	def reorganizeDatabase(self):

		# OBJECTIVE: Sort database by Song and create a new column labeled index

		# Connect to database
		self.connectToDatabase()

		# Create a cursor and execute sqlite command
		rows = self.allSongsDB.execute("""SELECT *
										FROM music
										ORDER BY Song""")

		# Update index columns
		for indx, row in enumerate(rows):
			self.allSongsDB.execute("""UPDATE music
									SET LibraryPos=(?)
									WHERE Location=(?)""", (indx + 1, row[-1]))

		# Save changes
		self.allSongsDB.commit()

		# Disconnect from database
		self.allSongsDB.close()

	def getSongDetails(self, path):

		# OBJECTIVE: Return entire row based from matching path

		# Connect to database
		self.connectToDatabase()

		# Creature a cursor
		cursor = self.allSongsDB.execute("""SELECT *
											FROM music
											WHERE Location=(?)""", (path,))

		# If cursor is none, exit function
		if cursor == None:
			print("Song doesn't exist!")
			return

		# Get first row from cursor
		cursor = cursor.fetchone()

		# Close database and return cursor
		self.allSongsDB.close()
		return cursor

	def getSongByName(self, name):

		# OBJECTIVE: Based on song's name, return song's pathname.

		# Connect to database
		self.connectToDatabase()
		
		# Create a cursor and execute sqlite command
		row = self.allSongsDB.execute("""SELECT Song, Location, LibraryPos
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
		self.allSongsDB.close()
		return row

	def getSongByPos(self, pos):

		# OBJECTIVE: Return a nearby song if a user selects Forward or Rewind

		# Connect to database
		self.connectToDatabase()
		
		# Create a cursor and execute sqlite command
		# If Pos is out of bounds, then it's non-existent so return the 1st song as default value
		row = self.allSongsDB.execute("""SELECT Song, Location, LibraryPos
										FROM music
										WHERE LibraryPos=(?)""", (pos,)) # <= Need to make it into a tuple and add a comma

		# Save data from row before disconnection from server
		# NOTE: fetchone => execute() returns all rows meeting the criteria. fetchone() gets the 1st row
		# 		Also, fetchone() returns a tuple (name, pathname)
		row = row.fetchone()

		# If data wasn't found, return
		if row == None:
			print("Song doesn't exist!")

			# Create a cursor and get 1st row as default value
			row = self.allSongsDB.execute("""SELECT Song, Location, LibraryPos
											FROM music
											WHERE LibraryPos=0""")
			row = row.fetchone()
			

		# Disconnect from database and return output
		self.allSongsDB.close()
		return row

	def printList(self, tmpList):

		for i in tmpList:
			print(i)

	def printTable(self):

		# OBJECTIVE: Print table with cursor

		# Connect to database
		self.connectToDatabase()

		# Create a cursor
		cursor = self.allSongsDB.execute("""SELECT *
											FROM music
											ORDER BY Song""")

		# Print table
		self.printList(cursor)

		# Disconnect from database
		self.allSongsDB.close()

	def printSongsTable(self):

		# OBJECTIVE: Print all songs inserted to database

		# Connect to database
		self.connectToDatabase()

		# Create a cursor
		cursor = self.allSongsDB.execute("""SELECT Song, Location
											FROM music
											ORDER BY Song""")

		# Only print "song" column
		self.printList(cursor)

		# Disconnect from database
		self.allSongsDB.close()

	def printArtistsTable(self):

		# OBJECTIVE: Print a table of all recorded artists

		# Connect to database
		self.connectToDatabase()

		# Create a cursor
		# NOTE: "DISTINCT" doesn't return duplicate entries from a result set
		cursor = self.allSongsDB.execute("""SELECT DISTINCT Artists
											FROM music
											ORDER BY Artists""")

		# Print table
		self.printList(cursor)

		# Disconnect from database
		self.allSongsDB.close()

	def getArtistAlbums(self, artist):

		# OBJECTIVE: Print a table of an artist's albums

		# Connect to database
		self.connectToDatabase()

		# Create a cursor
		cursor = self.allSongsDB.execute("""SELECT Artists, Album
											FROM music
											WHERE Artists=(?)
											ORDER BY Album""", (artist,))

		# Print table
		self.printList(cursor)

		# Disconnect from database
		self.allSongsDB.close()

	def printAlbumsTable(self):

		# OBJECTIVE: Print a table of all recorded albums

		# Connect to database
		self.connectToDatabase()

		# Create a cursor
		cursor = self.allSongsDB.execute("""SELECT DISTINCT Album
											FROM music
											ORDER BY Album""")

		# Print table
		self.printList(cursor)

		# Disconnect from database
		self.allSongsDB.close()

	def getAlbumSongs(self, album):

		# OBJECTIVE: Print a table of all songs listed under album

		# Connect to database
		self.connectToDatabase()

		# Create a cursor
		cursor = self.allSongsDB.execute("""SELECT DISTINCT Album, Song
											FROM music
											WHERE Album=(?)
											ORDER BY Song""", (album,))

		# Print table
		self.printList(cursor)

		# Disconnect from database
		self.allSongsDB.close()