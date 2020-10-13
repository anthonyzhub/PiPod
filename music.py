
from tkinter import *
from playsound import playsound
import os
import copy

from link import LinkList, Node

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

		# Create a dictionary dedicated to artist
		self.musicLibraryDict = dict()

		# Gather all songs inside the device and add them to self.musicLibraryDict{}
		self.totalSongs = 0
		self.scanMusicDirectory()

		# Create a link list of all the music in sorted order
		self.finalMusicLinkList = LinkList()
		self.organizeMusicLibrary()
		self.finalMusicLinkList.size = self.totalSongs # Manually enter link list size

	def entryMsg(self, location):

		# OBJECTIVE: Display a message whenever the user enters a new window

		location = "Window: {}".format(location)
		print("\n{}\n{}\n{}\n".format("=" * len(location), location, "=" * len(location)))

	def errorMsg(self, msg):

		# OBJECTIVE: Print a custom message if an exception or error rises
		print("ERROR: {}".format(msg))
		
	def mergeTwoSortedLinkList(self, headA, headB=None):
		
		# OBJECTIVE: Merge 2 sorted link list to one by calling functions from LinkList class
		# link: https://www.geeksforgeeks.org/merge-sort-for-linked-list/

		# Create a dummy node
		dummyNode = Node()

		# Create a tail node referencing to dummy node
		tailNode = dummyNode
		while True:

			# If either link list is empty, add all elements from the other link list
			if headA == None:
				# print("head_a is empty!")
				tailNode.next = headB
				headB.prev = tailNode
				break

			if headB == None:
				# print("head_b is empty!")
				tailNode.next = headA
				headA.prev = tailNode
				break

			# Compare nodes from both link list to see which goes first in sorted order
			if headA.data <= headB.data:
				# print("Adding head_a as next node")
				# print("Adding headA: {}".format(headA.data))

				# Update pointers
				tailNode.next = headA
				headA.prev = tailNode

				# Update headA
				headA = headA.next
			else:
				# print("Adding head_b as next node")
				# print("Adding headB: {}".format(headB.data))

				# Update pointers
				tailNode.next = headB
				headB.prev = tailNode

				# Update headB
				headB = headB.next

			# Update tail node
			tailNode = tailNode.next

		# Delete prev pointer in head link list
		# NOTE: Prev pointer still points to dummyNode after function ends
		dummyNode.next.prev = None

		# Return head of merged link list
		return dummyNode.next

	def musicPlayerWindow(self, songPlaying):

		# OBJECTIVE: Open a new window when a song has been selected

		# Print song being played
		self.entryMsg("Music Player")

		# Show options to go skip, rewind, pause, play, and go back to previous window
		while True:

			# Print what song is playing and what options are available
			print("\nNow Playing: {}".format(songPlaying))
			option = input("< |>| > -1: ")

			# Narrow down options
			if option == "<":
				option = "Rewind song or going to previous song"
			elif option == "|>|":
				option = "Pause/Play"
			elif option == ">":
				option = "Next song"
			elif option == "-1":
				return
			else:
				self.errorMsg("Invalid entry!")
				continue

			# Print selected option
			print(option)

	def showMusicLibraryWindow(self):

		# OBJECTIVE: List all songs inside the device onto the window in alphabetical order

		# Select music to play
		print("Enter -1 to go back")
		while True:

			# Print music library
			self.entryMsg("Music Library")
			# self.finalMusicLinkList.printForward()
			self.finalMusicLinkList.printBackwards()

			# Raise exception if musicSelected cannot cast to int
			try:
				musicSelected = int(input("Play song #: "))
			except:
				self.errorMsg("Numbers only!")
			else:

				# Skip to next iteration, if invalid entry was entered
				if (musicSelected > self.finalMusicLinkList.size) or (musicSelected == 0):
					self.errorMsg("Invalid entry!")
					continue

				if musicSelected == -1:
					return

				# Get song from nth position
				musicSelected = self.finalMusicLinkList.dataAtPosition(musicSelected)
				self.musicPlayerWindow(musicSelected)

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
		oldHead = headNodesList[0] # <= Get 1st element from list
		for pos in range(1, len(headNodesList)):

			# print("head_nodes_list[pos]: {}".format(headNodesList[pos]))

			# Merge head of 2 link lists together in sorted order. Return value will be head of new link list
			oldHead = self.mergeTwoSortedLinkList(oldHead, headNodesList[pos])

		# Update final link list's head
		self.finalMusicLinkList.head.next = oldHead
		# self.finalMusicLinkList.printForward()
		# self.finalMusicLinkList.printBackwards() BUG: 'NoneType' object has no attribute 'prev'

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

				# while albumNode.next != None:
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
			ll.head.next = ll.mergeSort(ll.getHead())
			# ll.printForward()
			# ll.printBackwards()

			# Keep track of number of songs for self.finalMusicLibrary link list
			self.totalSongs += ll.size

			# Save album and songs as a dictionary to the list
			# Ex. {album name: link list}
			oldArtistAlbumsList.append({albumNameStr: ll.getHead()})
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
			for directory, subDirectory, filename in os.walk(startingDir, topdown=True):

				# print("Directory: {}".format(directory))
				# print("Subdirectory: {}".format(subDirectory))
				# print("filename: {}".format(filename))

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
						oldArtistAlbumsList = self.addSongsToDictionary(album, subDirectory, filename, oldArtistAlbumsList)

					# If old_artist != artist, then we already have all the songs from "old_artist" and need to add a new "artist"
					if oldArtistStr != artist:
						# print("'old_artist' and 'artist' DON'T match!")

						# Add old_artist with old_artist_albums to final dictionary
						self.musicLibraryDict[oldArtistStr] = copy.deepcopy(oldArtistAlbumsList)

						# Update variables
						oldArtistStr = artist
						oldArtistAlbumsList = []

						oldArtistAlbumsList = self.addSongsToDictionary(album, subDirectory, filename, oldArtistAlbumsList)

				# print()

			# Once for-loop ends, save last record of artist's songs and albums
			# Add old_artist with old_artist_albums to final dictionary
			self.musicLibraryDict[oldArtistStr] = copy.deepcopy(oldArtistAlbumsList)

			# Exit while-loop
			break

		self.printMusicDictionary()