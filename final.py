"""
Program: final.py
Author: Zachary Binder
Date: 9-17-18

A program that contains 3 buttons and on click will make a different image appear
one for html one for js and one for css
"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage

class Final(EasyFrame):
	#Displays the buttons and provides space for the images to later be filled upon click of the buttons
	def __init__(self):
		EasyFrame.__init__(self, title = "Image Viewer 1.0")

		#creating a heading on the top saying the name of the program
		self.label1 = self.addLabel(text = "Image Viewer 1.0", row = 0, column = 0, columnspan = 4, sticky = "NSEW")

		#Making the buttons for each image
		self.html = self.addButton(text = "HTML", row = 2, column = 0, command = self.htmlAppear)
		self.js = self.addButton(text = "    JS    ", row = 2, column = 1, command = self.jsAppear)
		self.css = self.addButton(text = "  CSS  ", row = 2, column = 2, command = self.cssAppear)

		#changing the colors for the buttons
		self.html["background"] = "darkorange"
		self.js["background"] = "gold"
		self.css["background"] = "dodgerblue"

	#Makes the html image appear
	def htmlAppear(self):
		imageLabel1 = self.addLabel(text = "", row = 1, column = 0, sticky = "NSEW")
		self.image1 = PhotoImage(file = "html.gif")
		imageLabel1["image"] = self.image1
		self.html["command"] = self.htmlDisappear

	#Makes the html image disappear
	def htmlDisappear(self):
		imageLabel1 = self.addLabel(text = "", row = 1, column = 0, sticky = "NSEW")
		imageLabel1["image"] = PhotoImage(file = "")
		self.html["command"] = self.htmlAppear
	
	#Makes the js image appear
	def jsAppear(self):
		imageLabel2 = self.addLabel(text = "", row = 1, column = 1, sticky = "NSEW")
		self.image2 = PhotoImage(file = "js.gif")
		imageLabel2["image"] = self.image2
		self.js["command"] = self.jsDisappear
	
	#Makes the js image disappear
	def jsDisappear(self):
		imageLabel2 = self.addLabel(text = "", row = 1, column = 1, sticky = "NSEW")
		imageLabel2["image"] = PhotoImage(file = "")
		self.js["command"] = self.jsAppear
	
	#Makes the css image appear
	def cssAppear(self):
		imageLabel3 = self.addLabel(text = "", row = 1, column = 2, sticky = "NSEW")
		self.image3 = PhotoImage(file = "css.gif")
		imageLabel3["image"] = self.image3
		self.css["command"] = self.cssDisappear
	
	#Makes the css image disappear
	def cssDisappear(self):
		imageLabel3 = self.addLabel(text = "", row = 1, column = 2, sticky = "NSEW")
		imageLabel3["image"] = PhotoImage(file = "")
		self.css["command"] = self.cssAppear
#setting the program to run a main loop so it is able to run properly
def main():
	Final().mainloop()

#calls the main method which runs the program
main()