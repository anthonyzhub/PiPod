# Sort link list with merge sort: https://www.geeksforgeeks.org/merge-sort-for-linked-list/

from tkinter import *
import os
import copy

class Node:

	def __init__(self, data):
		self.next = None
		self.data = data

class LinkList:

	def __init__(self):

		# Create a head and tail node
		self.head = None
		self.tail = None

		# Create counter of list size
		self.size = 0

	def isEmpty(self):

		# OBJECTIVE: Check if link list is empty

		return self.size == 0

	def addHead(self, data):

		# OBJECTIVE: If list is empty, immediately add a head

		# Create a new node
		newNode = Node(data)
		newNode.next = None

		# Update head node
		self.head = newNode
		self.tail = newNode

		# Update counter
		self.size += 1

	def addNode(self, data):

		# OBJECTIVE: Add a new node to the end of the list

		# Check if link list is empty
		if self.isEmpty():
			self.addHead(data)
			return None

		# Create a new node
		newNode = Node(data)
		newNode.next = None

		# Get last node
		lastNode = self.tail
		lastNode.next = newNode

		# Update last node
		self.tail = newNode

		# Update counter
		self.size += 1

	def deleteNode(self, pos):

		# OBJECTIVE: Delete a node from link list

		# Abort if list is empty
		if self.isEmpty():
			return None

		# Delete head
		if pos == 1:

			# Get the first 2 nodes
			oldHead = self.head
			newHead = oldHead.next

			# Update head and old node
			self.head = newHead
			del oldHead

		elif pos > 1 and pos <= self.size:
			
			# Iterate link list until position is met
			currNode = self.head
			oldNode = currNode

			for _ in range(pos - 1):
				oldNode = currNode
				currNode = currNode.next

			# Update references and remove node
			oldNode.next = currNode.next
			del currNode

			# Update counter
			self.size -= 1

		else:

			return False

	def getHead(self):

		# OBJECTIVE: Return memory address of head node

		return self.head

	def getMiddleNode(self, headNode):

		# OBJECTIVE: Get middle position of node from link list
		# NOTE: Cannot use self.size because a link list will be divided by half until there is only 1 left,
		# 		so the size will be changing

		# Return node if it is empty
		if headNode == None:
			return headNode

		# Set 2 positions
		slowNode = headNode
		fastNode = headNode

		# Iterate link list
		# Make sure next node and node after that exist
		while (fastNode.next != None) and (fastNode.next.next != None):

			# Update nodes
			slowNode = slowNode.next
			fastNode = fastNode.next.next

		# Return slow_node as middle node
		return slowNode

	def sortedMerge(self, linkListA, linkListB):

		# OBJECTIVE: Sort 2 halves of the same link list

		newHead = None

		# Check if either halves of the list are none
		if linkListA == None:
			return linkListB

		if linkListB == None:
			return linkListA

		# Make a recursive call, divide called link list, and come back here
		if linkListA.data <= linkListB.data:
			newHead = linkListA
			newHead.next = self.sortedMerge(linkListA.next, linkListB)
		else:
			newHead = linkListB
			newHead.next = self.sortedMerge(linkListA, linkListB.next)

		# Return head sorted link list
		return newHead

	def mergeSort(self, headNode):

		# OBJECTIVE: Sort link list starting with head node

		# Check if link list is empty or by itself
		if (headNode == None) or (headNode.next == None):
			return headNode

		# Get middle node
		middleNode = self.getMiddleNode(headNode)
		node_after_middle = middleNode.next

		# Set pointer from middle_node to next node as None
		# NOTE: By setting next as none, middle_node would be the end of the link list
		middleNode.next = None

		# Sort left and right side of link list
		leftSide = self.mergeSort(headNode)
		rightSide = self.mergeSort(node_after_middle)

		# Merge both sides of the link list to one in sorted order.
		# The return value of sortedMerge() is the head node of the new link list
		return self.sortedMerge(leftSide, rightSide)
		# self.head = self.sortedMerge(leftSide, rightSide)

	def printLinkList(self):

		# OBJECTIVE: Print all nodes inside link list

		# Get head node
		curr_node = self.head

		# Iterate link list with counter
		counter = 1
		
		print()
		while curr_node != None:
			print("{}. {}".format(counter, curr_node.data))

			curr_node = curr_node.next
			counter += 1
		print()

class MusicLibrary:

	"""
	def __init__(self, WIN_WIDTH, WIN_HEIGHT):

		# Create a new window
		self.music_win = Toplevel()
		self.music_win.geometry("{}x{}".format(WIN_WIDTH, WIN_HEIGHT))
		self.music_win.title("Music Library")

		# Create a dictionary dedicated to artist
		self.music_library = dict()

		# Immediately call function to collect device's songs
		self.get_music()
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

		# Create a dictionary dedicated to artist
		self.musicLibraryDict = dict()

		# Gather all songs inside the device and add them to self.music_library{}
		self.scanMusicDirectory()

		# Create a link list of all the music in sorted order
		self.finalMusicLinkList = LinkList()
		# self.finalMusicLinkList.head = self.organizeMusicLibrary()
		self.organizeMusicLibrary()

	def musicPlayerWindow(self, chosen_song):

		# OBJECTIVE: Open a new window when a song has been selected

		print("Now Playing: {}".format(chose_song))
		
	def mergeTwoSortedLinkList(self, headA, headB=None):
		# link: https://www.geeksforgeeks.org/merge-sort-for-linked-list/
		# OBJECTIVE: Merge 2 sorted link list to one by calling functions from LinkList class

		# Create a dummy node
		dummyNode = Node(0)

		# Create a tail node referencing to dummy node
		tailNode = dummyNode
		while True:

			# If either link list is empty, add all elements from the other link list
			if headA == None:
				print("head_a is empty!")
				tailNode.next = headB
				break

			if headB == None:
				print("head_b is empty!")
				tailNode.next = headA
				break

			# Compare nodes from both link list to see which goes first in sorted order
			if headA.data <= headB.data:
				print("Adding head_a as next node")
				tailNode.next = headA
				headA = headA.next # BUG: head_a and head_b are not advancing
			else:
				print("Adding head_b as next node")
				tailNode.next = headB
				headB = headB.next

			# Update tail node
			tailNode = tailNode.next

		# Return head of merged link list
		return dummyNode.next

	def organizeMusicLibrary(self):

		# OBJECTIVE: Iterate dictionary and add music to a sorted link list. Return head of link list

		print("Collecting head nodes from each album")

		# Create a list to hold all head nodes inside self.music.library{}
		headNodesList = list()

		# Iterate dictionary and inner dictionary
		for albums in self.musicLibraryDict.values():
			for album in albums:

				# Get head node (value) from dictionary
				currHead = album[next(iter(album))]

				# Add head node to list
				headNodesList.append(currHead)

		print("Creating 1 link list")
		print("head_nodes_list: {}".format(headNodesList))
		oldHead = None
		for pos in range(len(headNodesList)):

			print("head_nodes_list[pos]: {}".format(headNodesList[pos]))

			# Set 2nd parameter as None for 1st and last node
			if pos == 0:
				oldHead = self.mergeTwoSortedLinkList(headNodesList[pos], None)
			else:
				oldHead = self.mergeTwoSortedLinkList(oldHead, headNodesList[pos])

		# Update final link list's head
		self.finalMusicLinkList.head = oldHead

	def printMusicLibrary(self):

		# OBJECTIVE: List all songs inside the device onto the window in alphabetical order
		self.finalMusicLinkList.printLinkList()

	def printDictionaryValues(self, album, headNode):

		# OBJECTIVE: Print link list from self.music_library's values value (no typo)

		# Print data
		print("\tAlbum: {}".format(album))
		print("\tSongs:")

		# Iterate link list
		oldNode = headNode
		while oldNode != None:
			print("\t\t{}".format(oldNode.data))
			oldNode = oldNode.next

	def printDictionary(self):

		# OBJECTIVE: Print music library

		# Iterate dictionary
		print("Printing 'self.music_library_dict\{\}'")
		for artist, albums in self.musicLibraryDict.items():
			
			print("Artist: {}".format(artist))

			# Iterate list
			for listing in albums:

				# Get key and value
				tempKey = next(iter(listing))
				tempVal = listing[tempKey]

				# Print link list of dictionary's value
				self.printDictionaryValues(tempKey, tempVal)
				print()

	def addSongsToDictionary(self, albumName, albumDir, songsList, oldArtistAlbums):

		# OBJECTIVE: Add an album and its songs as a dictionary to a list

		# If sub_directory is empty and songs_list isn't, then we are inside an album directory
		# We're currently in the location of the album's songs
		if albumDir == [] and songsList != []:
			print("Preparing to add '{}' to 'old_artist_albums'".format(albumName))

			ll = LinkList()

			# Add all songs inside directory to link list
			for song in songsList:
				ll.addNode(song)

			# Sort link list
			# ll.mergeSort(ll.getHead()) # <= BUG: mergeSort() is creating a link list that points to the same node infinitely
			ll.head = ll.mergeSort(ll.getHead())
			ll.printLinkList()

			# Save album and songs as a dictionary to the list
			oldArtistAlbums.append({albumName: ll.getHead()})
			print("Added '{}' with '{}' as head node to 'old_artist_albums'!".format(albumName, ll.getHead().data))

		# Return album (list)
		return oldArtistAlbums

	def scanMusicDirectory(self):

		# OBJECTIVE: Fetch all music inside the device

		# Get full path of Music folder
		startingDir = "{}/Music".format(os.environ["HOME"])

		# Hold name of directories last visited
		oldArtist = ""
		oldArtistAlbums = list()

		while True:

			# Get directories and files inside Music directory
			# string, list, list in os.walk(starting_dir)
			# NOTE: topdown=True allows os.walk() to go to the bottom of the directory before going to any other
			for directory, subDirectory, filename in os.walk(startingDir, topdown=True):

				print("Directory: {}".format(directory))
				print("Subdirectory: {}".format(subDirectory))
				print("filename: {}".format(filename))

				try:
					# Split directory with "/" as denominator and slice it
					directoryList = directory.split("/")[4:]

					# Get album and song name from list
					artist = directoryList[0]
					album = directoryList[1]
					print("Artist: {}".format(artist))
					print("Album: {}".format(album))

				except:
					print("Exception occurred!")

				else:
					# If exception wasn't raised, execute code below

					# If this is the 1st iteration, add artist to old_artist
					if oldArtist == "":
						print("1st iteration, so I'll manually set 'old_artist' to 'artist'")
						oldArtist = artist

					# If old_artist == artist, then we haven't changed singers, so there must be more albums
					if oldArtist == artist:
						print("'old_artist' and 'artist' match!")
						oldArtistAlbums = self.addSongsToDictionary(album, subDirectory, filename, oldArtistAlbums)

					# If old_artist != artist, then we already have all the songs from "old_artist" and need to add a new "artist"
					if oldArtist != artist:
						print("'old_artist' and 'artist' DON'T match!")

						# Add old_artist with old_artist_albums to final dictionary
						self.musicLibraryDict[oldArtist] = copy.deepcopy(oldArtistAlbums)
						# print("Music Library: {}".format(self.music_library))

						# Update variables
						oldArtist = artist
						oldArtistAlbums = []

						oldArtistAlbums = self.addSongsToDictionary(album, subDirectory, filename, oldArtistAlbums)

				print()

			# Once for-loop ends, save last record of artist's songs and albums
			# Add old_artist with old_artist_albums to final dictionary
			self.musicLibraryDict[oldArtist] = copy.deepcopy(oldArtistAlbums)
			# print("Music Library: {}".format(self.music_library))

			# Exit while-loop
			break
