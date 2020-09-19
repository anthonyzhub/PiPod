from tkinter import *

class MusicLibrary:

	def __init__(self, WIN_WIDTH, WIN_HEIGHT):

		# Create a new window
		self.music_win = Toplevel()
		self.music_win.geometry("{}x{}".format(WIN_WIDTH, WIN_HEIGHT))
		self.music_win.title("Music Library")


