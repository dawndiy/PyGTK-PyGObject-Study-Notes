#!/usr/bin/env python
# -*- coding: utf-8 -*

# Menu_accelerator
# PyGtk Study Notes By DawnDIY
# http://www.dawndiy.com

import pygtk
pygtk.require('2.0')
import gtk

class MenuTest(gtk.Window):
	def __init__(self):
		super(MenuTest, self).__init__()
		
		self.set_title("Menu")
		self.set_size_request(300,250)
		self.set_position(gtk.WIN_POS_CENTER)
		
		mb = gtk.MenuBar()
		
		filemenu = gtk.Menu()
		filem = gtk.MenuItem("_File")
		filem.set_submenu(filemenu)
		
		agr = gtk.AccelGroup()
		self.add_accel_group(agr)
		
		exit = gtk.MenuItem("_Exit", agr)
		
		key = gtk.accelerator_parse("<Control>Q")
		key, mod = gtk.accelerator_parse("<Control>Q")
		print key
		print mod
		print key, mod
		exit.add_accelerator("activate", agr, key, mod, gtk.ACCEL_VISIBLE)
		exit.connect("activate", gtk.main_quit)
		filemenu.append(exit)
		
		mb.append(filem)
		
		vbox = gtk.VBox(False, 2)
		vbox.pack_start(mb, False, False, 0)
		
		self.add(vbox)
		self.connect("destroy", gtk.main_quit)
		self.show_all()

if __name__ == "__main__":
	mt = MenuTest()
	gtk.main()
		
