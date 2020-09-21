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

	def is_empty(self):

		# OBJECTIVE: Check if link list is empty

		return self.size == 0

	def add_head(self, data):

		# OBJECTIVE: If list is empty, immediately add a head

		# Create a new node
		new_node = Node(data)
		new_node.next = None

		# Update head node
		self.head = new_node
		self.tail = new_node

		# Update counter
		self.size += 1

	def add_node(self, data):

		# OBJECTIVE: Add a new node to the end of the list

		# Check if link list is empty
		if self.is_empty():
			self.add_head(data)
			return None

		# Get last node
		last_node = self.tail

		# Create a new node
		new_node = Node(data)
		new_node.next = None

		last_node.next = new_node

		# Update last node
		self.tail= new_node

		# Update counter
		self.size += 1

	def delete_node(self, pos):

		# OBJECTIVE: Delete a node from link list

		# Abort if list is empty
		if self.is_empty():
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

	def get_head(self):

		# OBJECTIVE: Return memory address of head node

		return self.head

	def print_list(self):

		# OBJECTIVE: Print all nodes inside link list

		curr_node = self.head
		while curr_node != None:
			print(curr_node.data)
			curr_node = curr_node.next

class MusicLibrary:

	def __init__(self, WIN_WIDTH, WIN_HEIGHT):

		# Create a new window
		self.music_win = Toplevel()
		self.music_win.geometry("{}x{}".format(WIN_WIDTH, WIN_HEIGHT))
		self.music_win.title("Music Library")

		# Create a dictionary dedicated to artist
		self.music_library = dict()

		# Immediately call function to collect device's songs
		self.get_music()

	def print_music(self, album, head_node):

		# OBJECTIVE: Print link list from self.music_library's values value (no typo)

		# Print data
		print("\tAlbum: {}".format(album))
		print("\tSongs:")

		# Iterate link list
		old_node = head_node
		while old_node != None:
			print("\t\t{}".format(old_node.data))
			old_node = old_node.next

	def print_dictionary(self):

		# OBJECTIVE: Print music library

		print("Printing 'self.music_library'")
		for artist, albums in self.music_library.items():
			
			print("Artist: {}".format(artist))

			for listing in albums:

				# Get key and value
				temp_key = next(iter(listing))
				temp_val = listing[temp_key]

				# Print link list of dictionary's value
				self.print_music(temp_key, temp_val)
				print()

	def add_songs_from_library(self, album_name, album_dir, songs_list, old_artist_albums):

		# OBJECTIVE: Add an album and its songs as a dictionary to a list

		# If sub_directory is empty and filename isn't, then we are inside an album directory
		# We're currently in the location of the album's songs
		if album_dir == [] and songs_list != []:
			print("Preparing to add '{}' to 'old_artist_albums'".format(album_name))

			ll = LinkList()

			# Add all songs inside directory to link list
			for song in songs_list:
				ll.add_node(song)

			# Save album and songs to list
			old_artist_albums.append({album_name: ll.get_head()})
			print("Added '{}' with {} to 'old_artist_albums!".format(album_name, ll.get_head()))

		# Return album
		return old_artist_albums

	def get_music(self):

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
						old_artist_albums = self.add_songs_from_library(album, sub_directory, filename, old_artist_albums)

					# If old_artist != artist, then we already have all the songs from "old_artist" and need to add a new "artist"
					if old_artist != artist:
						print("'old_artist' and 'artist' DON'T match!")

						# Add old_artist with old_artist_albums to final dictionary
						self.music_library[old_artist] = copy.deepcopy(old_artist_albums)
						# print("Music Library: {}".format(self.music_library))

						# Update variables
						old_artist = artist
						old_artist_albums = []

						old_artist_albums = self.add_songs_from_library(album, sub_directory, filename, old_artist_albums)

				print()

			# Once for-loop ends, save last record of artist's songs and albums
			# Add old_artist with old_artist_albums to final dictionary
			self.music_library[old_artist] = copy.deepcopy(old_artist_albums)
			# print("Music Library: {}".format(self.music_library))

			# Exit while-loop
			break

		# print("Final Music Library: {}".format(self.music_library))
		self.print_dictionary()
