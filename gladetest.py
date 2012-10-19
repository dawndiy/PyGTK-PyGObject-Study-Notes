#!/usr/bin/env python
#-*- coding: utf-8 -*-
import gtk

class TutorialApp:       
	def __init__(self):
	    builder = gtk.Builder()
	    builder.add_from_file("gladetest.ui")
	    builder.connect_signals({ "on_window1_destroy" : gtk.main_quit })
	    self.window = builder.get_object("window1")
	    self.window.show()

if __name__ == "__main__":
	app = TutorialApp()
	gtk.main()
