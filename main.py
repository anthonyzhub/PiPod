#! /usr/bin/python3

# from tkinter import *

# Import classes
from music import MusicLibrary

# Global variables
WIN_WIDTH = 240
WIN_HEIGHT = 240

def entryMsg(location):
	print("\n{}\nWindow: {}\n{}\n".format("=" * 20, location, "=" * 20))

def music():

	# Show music library
	musicClass.showMusicLibraryWindow()

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

	# Create and layout buttons
	musicBtn = Button(root, text="Music", command=music)
	photosBtn = Button(root, text="Photos", command=photos)
	videosBtn = Button(root, text="Videos", command=videos)
	extrasBtn = Button(root, text="Extras", command=extras)
	shuffleBtn = Button(root, text="Shuffle", command=shuffle)
	settingsBtn = Button(root, text="Settings", command=settings)

	musicBtn.place(x=0, y=0, height=BTN_HEIGHT, width=WIN_WIDTH)
	photosBtn.place(x=0, y=BTN_HEIGHT, height=BTN_HEIGHT, width=WIN_WIDTH)
	videosBtn.place(x=0, y=BTN_HEIGHT * 2, height=BTN_HEIGHT, width=WIN_WIDTH)
	extrasBtn.place(x=0, y=BTN_HEIGHT * 3, height=BTN_HEIGHT, width=WIN_WIDTH)
	shuffleBtn.place(x=0, y=BTN_HEIGHT * 4, height=BTN_HEIGHT, width=WIN_WIDTH)
	settingsBtn.place(x=0, y=BTN_HEIGHT * 5, height=BTN_HEIGHT, width=WIN_WIDTH)

	# Display window with all widgets
	root.mainloop()
	
	# Initialize MusicLibrary
	musicClass = MusicLibrary(WIN_WIDTH, WIN_HEIGHT)
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
	"""