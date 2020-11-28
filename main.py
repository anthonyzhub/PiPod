#! /usr/bin/python3

# from tkinter import *

# Import classes
from music import MusicLibrary

# Global variables
WIN_WIDTH = 240
WIN_HEIGHT = 240

def entryMsg(location):
	print("\n{}\nWindow: {}\n{}\n".format("=" * 20, location, "=" * 20))

def music(musicClass):

	# Show music library
	# musicClass.songsWindow()
	musicClass.musicMenuWindow()

def photos():
	entryMsg("Photo Library")

def videos():
	entryMsg("Video Library")

def extras():
	entryMsg("Extras")

def settings():
	entryMsg("Settings")

def shuffle(musicClass):
	musicClass.shuffleMusic()

if __name__ == "__main__":

	# Initialize MusicLibrary
	musicClass = MusicLibrary()

	# Ask for input
	while True:

		# Print menu
		print("\n1. Music\n2. Photos\n3. Videos\n4. Extras\n5. Settings\n6. Shuffle Songs\n-1. Quit")

		option = int(input("\nSelect: "))

		# If "option" is valid, call desired function
		if option == 1:
			music(musicClass)
		elif option == 2:
			photos()
		elif option == 3:
			videos()
		elif option == 4:
			extras()
		elif option == 5:
			settings()
		elif option == 6:
			shuffle(musicClass)
		elif option == -1:
			exit(1)
		else:
			print("Invalid option!")