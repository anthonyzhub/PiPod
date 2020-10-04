#! /usr/bin/python3

# Import libraries
#from tkinter import *

# Import classes
from music import MusicLibrary

# Global variables
WIN_WIDTH = 240
WIN_HEIGHT = 240

def musicWindow():

	# OBJECTIVE: Open a new window with a list of songs
	print("Music window is open")

	music_library = MusicLibrary(WIN_WIDTH, WIN_HEIGHT)

def entryMsg(location):
	print("\n{}\nWindow: {}\n{}\n".format("=" * 20, location, "=" * 20))

def music(music_class):
	music_class.showMusicLibraryWindow()

def photos():
	entryMsg("Photo Library")

def videos():
	entryMsg("Video Library")

def extras():
	entryMsg("Extras")

def settings():
	entryMsg("Settings")

def shuffle():
	entryMsg("Music Player")

if __name__ == "__main__":

	"""
	# Initialize tkinter() 
	root = Tk()

	# Create a 240x240 window (dimensions comes from adafruit screen)
	root.geometry("{}x{}".format(WIN_WIDTH, WIN_HEIGHT))

	# Create a "Music" button to show user's music
	music_btn = Button(root, text="Music", command=music_window)
	music_btn.place(x=0, y=0, height=25, width=WIN_WIDTH)

	# Display window with all widgets
	root.mainloop()
	"""

	# Initialize MusicLibrary
	musicClass = MusicLibrary()

	# Ask for input
	option = 0
	while True:

		# Print menu
		print("1. Music\n2. Photos\n3. Videos\n4. Extras\n5. Settings\n6. Shuffle Songs\n-1. Quit")

		try:
			option = int(input("\nSelect: "))

		except ValueError as e:
			print("Error: {}".format(e))
			print("Enter a number!")

		else:

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
				shuffle()
			elif option == -1:
				exit(1)
			else:
				print("Invalid option!")
