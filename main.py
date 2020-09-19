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

if __name__ == "__main__":

	# Initialize tkinter() 
	root = Tk()

	# Create a 240x240 window (dimensions comes from adafruit screen)
	root.geometry("{}x{}".format(WIN_WIDTH, WIN_HEIGHT))

	# Create a "Music" button to show user's music
	music_btn = Button(root, text="Music", command=music_window)
	music_btn.place(x=0, y=0, height=25, width=WIN_WIDTH)

	# Display window with all widgets
	root.mainloop()
