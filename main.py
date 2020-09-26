#! /usr/bin/python3

# Import libraries
from tkinter import *

# Import classes
from music import MusicLibrary

# Global variables
WIN_WIDTH = 240
WIN_HEIGHT = 240

def music_window():

	# OBJECTIVE: Open a new window with a list of songs
	print("Music window is open")

	music_library = MusicLibrary(WIN_WIDTH, WIN_HEIGHT)

def entry_msg(loc):
	print("Window: {}".format(loc))

def music(music_class):
	entry_msg("Music Library")
	music_class.music_library_window()

def photos():
	entry_msg("Photo Library")

def videos():
	entry_msg("Video Library")

def extras():
	entry_msg("Extras")

def settings():
	entry_msg("Settings")

def shuffle():
	entry_msg("Music Player")

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
	music_class = MusicLibrary()

	# Print menu
	print("1. Music\n2. Photos\n3. Videos\n4. Extras\n5. Settings\n6. Shuffle Songs")

	# Ask for input
	option = 0
	while True:

		try:
			option = int(input("Select: "))

		except ValueError as e:
			print("Error: {}".format(e))
			print("Enter a number!")

		else:

			# If "option" is valid, call desired function

			if option == 1:
				music(music_class)
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
			else:
				print("Invalid option!")
