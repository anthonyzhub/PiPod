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
		new_node = Node(data)
		new_node.next = None

		# Update head node
		self.head = new_node
		self.tail = new_node

		# Update counter
		self.size += 1

	def addNode(self, data):

		# OBJECTIVE: Add a new node to the end of the list

		# Check if link list is empty
		if self.isEmpty():
			self.addHead(data)
			return None

		# Get last node
		last_node = self.tail

		# Create a new node
		new_node = Node(data)
		new_node.next = None

		last_node.next = new_node

		# Update last node
		self.tail = new_node

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
			old_head = self.head
			new_head = old_head.next

			# Update head and old node
			self.head = new_head
			del old_head

		elif pos > 1 and pos <= self.size:
			
			# Iterate link list until position is met
			curr_node = self.head
			old_node = curr_node

			for _ in range(pos - 1):
				old_node = curr_node
				curr_node = curr_node.next

			# Update references and remove node
			old_node.next = curr_node.next
			del curr_node

			# Update counter
			self.size -= 1

		else:

			return False

	def getHead(self):

		# OBJECTIVE: Return memory address of head node

		return self.head

	def getMiddleNode(self, head_node):

		# OBJECTIVE: Get middle position of node from link list
		# NOTE: Cannot use self.size because a link list will be divided by half until there is only 1 left,
		# 		so the size will be changing

		# Return node if it is empty
		if head_node == None:
			return head_node

		# Set 2 positions
		slow_node = head_node
		fast_node = head_node

		# Iterate link list
		# Make sure next node and node after that exist
		while (fast_node.next != None) and (fast_node.next.next != None):

			# Update nodes
			slow_node = slow_node.next
			fast_node = fast_node.next.next

		# Return slow_node as middle node
		return slow_node

	def sortedMerge(self, linkListA, linkListB):

		# OBJECTIVE: Sort 2 halves of the same link list

		result = None

		# Check if either halves of the list are none
		if linkListA == None:
			return linkListB

		if linkListB == None:
			return linkListA

		# Make a recursive call, divide called link list, and come back here
		if linkListA.data <= linkListB.data:
			result = linkListA
			result.next = self.sortedMerge(linkListA.next, linkListB)
		else:
			result = linkListB
			result.next = self.sortedMerge(linkListA, linkListB.next)

		# Return head sorted link list
		return result

	def mergeSort(self, head_node):

		# OBJECTIVE: Sort link list starting with head node

		# Check if link list is empty or by itself
		if (head_node == None) or (head_node.next == None):
			return head_node

		# Get middle node
		middle_node = self.getMiddleNode(head_node)
		node_after_middle = middle_node.next

		# Set pointer from middle_node to next node as None
		# NOTE: By setting next as none, middle_node would be the end of the link list
		middle_node.next = None

		# Sort left and right side of link list
		left_side = self.mergeSort(head_node)
		right_side = self.mergeSort(node_after_middle)

		# Merge both sides of the link list to one in sorted order.
		# The return value of sortedMerge() is the head node of the new link list
		sorted_link_list = self.sortedMerge(left_side, right_side)
		return sorted_link_list

		# Update head node
		# self.head = self.sortedMerge(left_side, right_side)

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
		self.music_library_dict = dict()

		# Gather all songs inside the device and add them to self.music_library{}
		self.scanMusicDirectory()

		# Create a link list of all the music in sorted order
		self.finalMusicLinkList = LinkList()
		self.finalMusicLinkList.head = self.organizeMusicLibrary()

	def musicPlayerWindow(self, chosen_song):

		# OBJECTIVE: Open a new window when a song has been selected

		print("Now Playing: {}".format(chose_song))
		
	def mergeTwoSortedLinkList(self, head_a, head_b=None):
		# link: https://www.geeksforgeeks.org/merge-sort-for-linked-list/
		# OBJECTIVE: Merge 2 sorted link list to one by calling functions from LinkList class

		# Create a dummy node
		dummy_node = Node(0)

		# Create a tail node referencing to dummy node
		tail_node = dummy_node
		while True:

			# If either link list is empty, add all elements from the other link list
			if head_a == None:
				print("head_a is empty!")
				tail_node.next = head_b
				break

			if head_b == None:
				print("head_b is empty!")
				tail_node.next = head_a
				break

			# Compare nodes from both link list to see which goes first in sorted order
			if head_a.data <= head_b.data:
				print("Adding head_a as next node")
				tail_node.next = head_a
				head_a = head_a.next # BUG: head_a and head_b are not advancing
			else:
				print("Adding head_b as next node")
				tail_node.next = head_b
				head_b = head_b.next

			# Update tail node
			tail_node = tail_node.next

		# Return head of merged link list
		return dummy_node.next

	def organizeMusicLibrary(self):

		# OBJECTIVE: Iterate dictionary and add music to a sorted link list. Return head of link list

		print("Collecting head nodes from each album")

		# Create a list to hold all head nodes inside self.music.library{}
		head_nodes_list = list()

		# Iterate dictionary and inner dictionary
		for albums in self.music_library_dict.values():
			for album in albums:

				# Get head node (value) from dictionary
				curr_head = album[next(iter(album))]
				# curr_head = album.keys()[0]

				# Add head node to list
				head_nodes_list.append(curr_head)

		print("Creating 1 link list")
		print("head_nodes_list: {}".format(head_nodes_list))
		old_head = None
		for pos in range(len(head_nodes_list)):

			print("head_nodes_list[pos]: {}".format(head_nodes_list[pos]))

			# Set 2nd parameter as None for 1st and last node
			if pos == 0:
				old_head = self.mergeTwoSortedLinkList(head_nodes_list[pos], None)
			else:
				old_head = self.mergeTwoSortedLinkList(old_head, head_nodes_list[pos])

		# Return head of link list
		return old_head

	def printMusicLibrary(self):

		# OBJECTIVE: List all songs inside the device onto the window in alphabetical order
		self.finalMusicLinkList.printLinkList()

	def printDictionaryValues(self, album, head_node):

		# OBJECTIVE: Print link list from self.music_library's values value (no typo)

		# Print data
		print("\tAlbum: {}".format(album))
		print("\tSongs:")

		# Iterate link list
		old_node = head_node
		while old_node != None:
			print("\t\t{}".format(old_node.data))
			old_node = old_node.next

	def printDictionary(self):

		# OBJECTIVE: Print music library

		# Iterate dictionary
		print("Printing 'self.music_library_dict\{\}'")
		for artist, albums in self.music_library_dict.items():
			
			print("Artist: {}".format(artist))

			# Iterate list
			for listing in albums:

				# Get key and value
				temp_key = next(iter(listing))
				temp_val = listing[temp_key]

				# Print link list of dictionary's value
				self.printDictionaryValues(temp_key, temp_val)
				print()

	def addSongsToDictionary(self, album_name, album_dir, songs_list, old_artist_albums):

		# OBJECTIVE: Add an album and its songs as a dictionary to a list

		# If sub_directory is empty and songs_list isn't, then we are inside an album directory
		# We're currently in the location of the album's songs
		if album_dir == [] and songs_list != []:
			print("Preparing to add '{}' to 'old_artist_albums'".format(album_name))

			ll = LinkList()

			# Add all songs inside directory to link list
			for song in songs_list:
				ll.addNode(song)

			# Sort link list
			# ll.printLinkList()
			# ll.mergeSort(ll.getHead()) # <= BUG: mergeSort() is creating a link list that points to the same node infinitely
			ll.head = ll.mergeSort(ll.getHead())
			ll.printLinkList()

			# Save album and songs as a dictionary to the list
			old_artist_albums.append({album_name: ll.getHead()})
			print("Added '{}' with '{}' as head node to 'old_artist_albums'!".format(album_name, ll.getHead().data))

		# Return album (list)
		return old_artist_albums

	def scanMusicDirectory(self):

		# OBJECTIVE: Fetch all music inside the device

		# Get full path of Music folder
		starting_dir = "{}/Music".format(os.environ["HOME"])

		# Hold name of directories last visited
		old_artist = ""
		old_artist_albums = list()

		while True:

			# Get directories and files inside Music directory
			# string, list, list in os.walk(starting_dir)
			# NOTE: topdown=True allows os.walk() to go to the bottom of the directory before going to any other
			for directory, sub_directory, filename in os.walk(starting_dir, topdown=True):

				print("Directory: {}".format(directory))
				print("Subdirectory: {}".format(sub_directory))
				print("filename: {}".format(filename))

				try:
					# Split directory with "/" as denominator and slice it
					directory_list = directory.split("/")[4:]

					# Get album and song name from list
					artist = directory_list[0]
					album = directory_list[1]
					print("Artist: {}".format(artist))
					print("Album: {}".format(album))

				except:
					print("Exception occurred!")

				else:
					# If exception wasn't raised, execute code below

					# If this is the 1st iteration, add artist to old_artist
					if old_artist == "":
						print("1st iteration, so I'll manually set 'old_artist' to 'artist'")
						old_artist = artist

					# If old_artist == artist, then we haven't changed singers, so there must be more albums
					if old_artist == artist:
						print("'old_artist' and 'artist' match!")
						old_artist_albums = self.addSongsToDictionary(album, sub_directory, filename, old_artist_albums)

					# If old_artist != artist, then we already have all the songs from "old_artist" and need to add a new "artist"
					if old_artist != artist:
						print("'old_artist' and 'artist' DON'T match!")

						# Add old_artist with old_artist_albums to final dictionary
						self.music_library_dict[old_artist] = copy.deepcopy(old_artist_albums)
						# print("Music Library: {}".format(self.music_library))

						# Update variables
						old_artist = artist
						old_artist_albums = []

						old_artist_albums = self.addSongsToDictionary(album, sub_directory, filename, old_artist_albums)

				print()

			# Once for-loop ends, save last record of artist's songs and albums
			# Add old_artist with old_artist_albums to final dictionary
			self.music_library_dict[old_artist] = copy.deepcopy(old_artist_albums)
			# print("Music Library: {}".format(self.music_library))

			# Exit while-loop
			break
