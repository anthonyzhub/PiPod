
from tkinter import *
from playsound import playsound
import os
import copy
import random

from link import LinkList, Node
from database import MusicDatabase

class MusicLibrary:

	"""
	def __init__(self, WIN_WIDTH, WIN_HEIGHT):

		# NOTE: This init() is for GUI use

		# Create a new window
		self.musicWindow = Toplevel()
		self.musicWindow.geometry("{}x{}".format(WIN_WIDTH, WIN_HEIGHT))
		self.musicWindow.title("Music Library")

		# Create a dictionary dedicated to artist
		self.musicLibraryDict = dict()

		# Gather all songs inside the device and add them to self.musicLibraryDict{}
		self.totalSongs = 0
		self.scanMusicDirectory()

		# Create a link list of all the music in sorted order
		self.finalMusicLinkList = LinkList()
		self.organizeMusicLibrary()
		self.finalMusicLinkList.size = self.totalSongs # Manually enter link list size

		# Create a scrollable list
		self.listBox = Listbox(self.musicWindow, selectmode=BROWSE) # <= BROWSE allows the user to scroll the list and only select 1 item
		self.listBox.pack()
		self.populateListBox()
	"""
	"""
	NOTE: music_library structure:

	Key 		  |		Value
	--------------------------
	Artist's name | [
						{Album 1: Head node to 1st song},
						{Album 2: Head node to 1st song},
						{Album 3: Head node to 1st song},
					]


	"""
	
	def __init__(self):

		# NOTE: This init() is for command line use

		# # Create a dictionary dedicated to artist
		# self.musicLibraryDict = dict()

		# # Gather all songs inside the device and add them to self.musicLibraryDict{}
		# self.totalSongs = 0
		# self.scanMusicDirectory()

		# # Create a link list of all the music in sorted order
		# self.finalMusicLinkList = LinkList()
		# self.organizeMusicLibrary()
		# self.finalMusicLinkList.size = self.totalSongs # Manually enter link list size

		self.db = MusicDatabase()
		# Save music in database
		self.addMusicToDatabase()

	def entryMsg(self, location):

		# OBJECTIVE: Display a message whenever the user enters a new window

		location = "Window: {}".format(location)
		print("\n{}\n{}\n{}\n".format("=" * len(location), location, "=" * len(location)))

	def errorMsg(self, msg):

		# OBJECTIVE: Print a custom message if an exception or error rises
		print("ERROR: {}".format(msg))

	def addRemainingNodes(self, newLinkList, headA):

		# OBJECTIVE: Add remaining nodes to from old link list to newLinkList

		# print("Adding remaining nodes")

		while headA != None:
			newLinkList.addNode(headA.data)
			# print(headA.data)
			headA = headA.next

		return newLinkList
		
	def mergeTwoSortedLinkList(self, headA, headB):
		
		# OBJECTIVE: Merge 2 sorted link list to one by calling functions from LinkList class
		# link: https://www.geeksforgeeks.org/merge-sort-for-linked-list/

		# Create a new link list
		newLinkList = LinkList()

		while True:

			# If either link list is empty, add all elements from the other link list
			if headA == None:
				newLinkList = self.addRemainingNodes(newLinkList, headB)
				break

			if headB == None:
				newLinkList = self.addRemainingNodes(newLinkList, headA)
				break

			# Compare nodes from both link list to see which goes first in sorted order
			if headA.data <= headB.data:

				# print("Adding A ")

				# Update pointers
				newLinkList.addNode(headA.data)

				# Update headA
				headA = headA.next

			else:

				# print("Adding B ")

				# Update pointers
				newLinkList.addNode(headB.data)

				# Update headB
				headB = headB.next

		return newLinkList

	def playSongFromLinkList(self, selectedLinkList):

		# OBJECTIVE: Open a new window when a song has been selected from a link list

		# Print song being played
		self.entryMsg("Music Player")

		# Get head node
		currNode = selectedLinkList.getHead()

		# While currNode isn't none, continue to show playSongFromLinkList
		# Exit function once currNode is none
		while currNode != None:

			# Print what song is playing and what options are available
			print("\nNow Playing: {}".format(currNode.data))
			option = input("< |>| > -1: ")

			# Narrow down options
			if option == "<":
				currNode = currNode.prev
			elif option == "|>|":
				option = "Pause/Play"
			elif option == ">":
				currNode = currNode.next
			elif option == "-1":
				return
			else:
				self.errorMsg("Invalid entry!")
				continue

	def playSongFromSortedLinkList(self, selectedNode):

		# OBJECTIVE: Open a new window when a song has been selected

		# Print song being played
		self.entryMsg("Music Player")

		# While currNode isn't none, continue to show playSongFromLinkList
		# Exit function once currNode is none
		while selectedNode != None:

			# Print what song is playing and what options are available
			print("\nNow Playing: {}".format(selectedNode.data))
			option = input("< |>| > -1: ")

			# Narrow down options
			if option == "<":
				selectedNode = selectedNode.prev
			elif option == "|>|":
				option = "Pause/Play"
			elif option == ">":
				selectedNode = selectedNode.next
			elif option == "-1":
				return
			else:
				self.errorMsg("Invalid entry!")
				continue

	def shuffleMusic(self):

		# OBJECTIVE: Pick a random number and play song at selected position

		print("Shuffling music")

		# Create a list filled with random numbers
		randomNumbers = list()

		while len(randomNumbers) != self.finalMusicLinkList.size:

			# Generate a unique random number and add it to list
			r = random.randint(1, self.finalMusicLinkList.size)

			if r not in randomNumbers:
				randomNumbers.append(r)

		# Add data in Nth position to shuffle link list
		newLinkList = LinkList()
		for pos in randomNumbers:
			result = self.finalMusicLinkList.binarySearchForPosition(self.finalMusicLinkList.getHead(), self.finalMusicLinkList.getTail(), pos)
			newLinkList.addNode(result)

		# Delete list and sent link list to playSongFromLinkList()
		del randomNumbers
		self.playSongFromLinkList(newLinkList)

	def showMusicLibraryWindow(self):

		# OBJECTIVE: List all songs inside the device onto the window in alphabetical order

		self.entryMsg("Music Library")

		# Select music to play
		print("Enter -1 to go back")
		while True:

			# Print music library
			self.finalMusicLinkList.printForward()

			# Raise exception if musicSelected cannot cast to int
			try:
				musicSelected = int(input("\nPlay song #: "))
			except:
				self.errorMsg("Numbers only!")
			else:

				# Skip to next iteration, if invalid entry was entered
				if musicSelected == -1:
					return
				
				if (musicSelected > self.finalMusicLinkList.size) or (musicSelected <= 0):
					self.errorMsg("Invalid entry!")
					continue

				# Get song from nth position
				nodeWithSong = self.finalMusicLinkList.binarySearchForNode(self.finalMusicLinkList.getHead(), self.finalMusicLinkList.getTail(), musicSelected)
				self.playSongFromSortedLinkList(nodeWithSong)
				# self.finalMusicLinkList.printForward()

	def organizeMusicLibrary(self):

		# OBJECTIVE: Iterate dictionary and add music to a sorted link list. Return head of link list

		print("Creating 1 link list with all the music together in sorted order")

		# Create a list to hold all head nodes inside self.music.library{}
		headNodesList = list()

		# Iterate dictionary and inner dictionary to add head nodes to headNodesList
		for singerAlbums in self.musicLibraryDict.values():
			for album in singerAlbums:

				# Get head node (value) from dictionary
				currHead = album[next(iter(album))]

				# Add head node to list
				headNodesList.append(currHead)

		# Iterate headNodesList
		newLinkList = LinkList()
		for pos in range(0, len(headNodesList)):

			# Merge 2 link lists and return a new one
			newLinkList = self.mergeTwoSortedLinkList(newLinkList.getHead(), headNodesList[pos].getHead())
			
		# Update final link list's head
		self.finalMusicLinkList = newLinkList

	def printMusicDictionary(self):

		# OBJECTIVE: Print music library

		# Iterate dictionary
		print("Printing 'self.musicLibraryDict'")
		for artistStr, albumsList in self.musicLibraryDict.items():
			
			print("Artist: {}".format(artistStr))

			# Iterate list
			for albumDict in albumsList:

				# Get key and value from dictionary
				# NOTE: iter() => create an iterator
				# 		next() => Go to next element within iterable
				albumName = next(iter(albumDict))
				albumNode = albumDict[albumName]

				# Print link list
				print("\tAlbum: {}".format(albumName))
				print("\tSongs:")

				while albumNode != None:
					print("\t\t{}".format(albumNode.data))
					albumNode = albumNode.next

				print()

	def addSongsToDictionary(self, albumNameStr, albumDirList, songsList, oldArtistAlbumsList):

		# OBJECTIVE: Add an album and its songs as a dictionary to a list

		# If sub_directory is empty and songs_list isn't, then we are inside an album directory
		# We're currently in the location of the album's songs
		if albumDirList == [] and songsList != []:
			print("Preparing to add '{}' to 'oldArtistAlbumsList'".format(albumNameStr))

			# Create a new link list of the album's songs
			ll = LinkList()

			# Add all songs inside directory to link list
			for song in songsList:
				ll.addNode(song)

			# Sort link list
			ll.head = ll.mergeSort(ll.getHead())
			# ll.printForward()
			# ll.printBackwards()

			# Keep track of number of songs for self.finalMusicLibrary link list
			self.totalSongs += ll.size

			# Save album and songs as a dictionary to the list
			# Ex. {album name: link list}
			# oldArtistAlbumsList.append({albumNameStr: ll.getHead()})
			oldArtistAlbumsList.append({albumNameStr: ll}) # NOTE: Save instance of LinkList
			# print("Added '{}' with '{}' as head node to 'old_artist_albums'!".format(albumName, ll.getHead().data))

		# Return album (list)
		return oldArtistAlbumsList

	def scanMusicDirectory(self):

		# OBJECTIVE: Fetch all music inside the device from dedicated directory

		# Get full path of Music folder
		startingDir = "{}/Music".format(os.environ["HOME"])
		print("Scanning device's Music directory")

		# Hold name of directories last visited
		oldArtistStr = ""
		oldArtistAlbumsList = list()

		while True:

			# Get directories and files inside Music directory
			# NOTE: 
			# 	1. For-loop breakdown: string, list, list in os.walk(starting_dir)
			# 	2. "topdown=True" allows os.walk() to go to the bottom of the directory before going to any other
			for directory, subDirectory, song in os.walk(startingDir, topdown=True):

				# print("Directory: {}".format(directory))
				# print("Subdirectory: {}".format(subDirectory))
				# print("song: {}".format(song))

				try:
					# Split directory with "/" as denominator and slice it
					directoryList = directory.split("/")[4:]

					# Get album and song name from list
					artist = directoryList[0]
					album = directoryList[1]
					# print("Artist: {}".format(artist))
					# print("Album: {}".format(album))

				except:
					# print("Exception occurred!")
					pass

				else:
					# If exception wasn't raised, execute code below

					# If this is the 1st iteration, add artist to old_artist
					if oldArtistStr == "":
						# print("1st iteration, so I'll manually set 'old_artist' to 'artist'")
						oldArtistStr = artist

					# If old_artist == artist, then we haven't changed singers, so there must be more albums
					if oldArtistStr == artist:
						# print("'old_artist' and 'artist' match!")
						oldArtistAlbumsList = self.addSongsToDictionary(album, subDirectory, song, oldArtistAlbumsList)

					# If old_artist != artist, then we already have all the songs from "old_artist" and need to add a new "artist"
					if oldArtistStr != artist:
						# print("'old_artist' and 'artist' DON'T match!")

						# Add old_artist with old_artist_albums to final dictionary
						self.musicLibraryDict[oldArtistStr] = copy.deepcopy(oldArtistAlbumsList)

						# Update variables
						oldArtistStr = artist
						oldArtistAlbumsList = []

						oldArtistAlbumsList = self.addSongsToDictionary(album, subDirectory, song, oldArtistAlbumsList)

				# print()

			# Once for-loop ends, save last record of artist's songs and albums
			# Add old_artist with old_artist_albums to final dictionary
			self.musicLibraryDict[oldArtistStr] = copy.deepcopy(oldArtistAlbumsList)

			# Exit while-loop
			break

		# self.printMusicDictionary()

	def addMusicToDatabase(self):

		# OBJECTIVE: Save all songs in directory to SQLite database

		# Base case. 
		# If database doesn't exist, create one and add songs to it.
		# If not, then don't add any songs and exit function.
		if not self.db.doesDatabaseExist():
			self.db.createDatabase()
		else:
			return

		# Get full path of Music folder
		startingDir = "{}/Music".format(os.environ["HOME"])
		print("Scanning device's Music directory")

		while True:

			# Get directories and files inside Music directory
			# NOTE: 
			# 	1. For-loop breakdown: string, list, list in os.walk(starting_dir)
			# 	2. "topdown=True" allows os.walk() to go to the bottom of the directory before going to any other
			for directory, subDirectory, songs in os.walk(startingDir, topdown=True):

				try:
					# Split directory with "/" as denominator and slice it
					directoryList = directory.split("/")[4:]

					# Get album and song name from list
					artist = directoryList[0]
					album = directoryList[1]

					# print("Directory: {}".format(directory))
					# print("Subdirectory: {}".format(subDirectory))
					# print("Artist: {}".format(artist))
					# print("Album: {}".format(album))
					# print("Songs: {}".format(songs))
					# print()

				except:
					# Skip to next iteration
					continue

				else:
					
					# If exception wasn't raised, enter data to database
					
					for song in songs:

						# Define path name
						# location = directory + "/" + song

						# Insert new data to table
						# NOTE: For 3rd argument, remove media file extension but keep it for file's pathname (location)
						self.db.insert(artist, album, song[:-4], directory + "/" + song)

			# Exit while-loop
			break

		# Outside of while-loop print table and close connection to datebase
		self.db.printTable()
		self.db.closeConnection()

	def playSongFromDatabase(self):

		# OBJECTIVE: When user clicks "songs", display all songs available in iPod

		# Base case.
		# Check if database exists. If yes, then show all songs. If not, create one and add all songs.
		if not self.db.doesDatabaseExist():
			self.addMusicToDatabase()

		# Connect to database
		self.db.connectToDatabase()

		# Display everything in "song" column of database
		self.entryMsg("Music Library")
		self.db.printSongsAvailable()

		# Ask user to select song
		while True:

			songSelected = input("Play song #")
			
			# If variable cannot cast to int, raise exception and ask for input again
			try:
				songSelected = int(songSelected)

			except:
				print("Invalid entry!")
				continue
				
			else:
