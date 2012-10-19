#!/usr/bin/env python
# -*- coding: utf-8 -*

# Toolbar
# PyGtk Stady Notes By DawnDIY
# http://www.dawndiy.com

import pygtk
pygtk.require('2.0')
import gtk


class Toolbar:
	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.set_title("Toolbar")
		self.win.set_size_request(300,250)
		self.win.set_position(gtk.WIN_POS_CENTER)

		toolbar = gtk.Toolbar()
		toolbar.set_style(gtk.TOOLBAR_ICONS)
	
	#	toolbar.set_icon_size(gtk.ICON_SIZE_MENU)
#		toolbar.set_icon_size(gtk.ICON_SIZE_SMALL_TOOLBAR)
#		toolbar.set_icon_size(gtk.ICON_SIZE_INVALID)
		toolbar.set_icon_size(gtk.ICON_SIZE_LARGE_TOOLBAR)

		newtb = gtk.ToolButton(gtk.STOCK_NEW)
		opentb = gtk.ToolButton(gtk.STOCK_OPEN)
		sep = gtk.SeparatorToolItem()
		closetb = gtk.ToolButton(gtk.STOCK_CLOSE)
		exittb = gtk.ToolButton(gtk.STOCK_QUIT)

		exittb.connect("clicked", gtk.main_quit)

		closetb.set_sensitive(False)

		toolbar.insert(newtb, 0)
		toolbar.insert(opentb, 1)
		toolbar.insert(sep, 2)
		toolbar.insert(closetb, 3)
		toolbar.insert(exittb, 4)


		vbox = gtk.VBox()
#		vbox.add(toolbar)
#		vbox.pack_start(toolbar)
#		vbox.pack_end(toolbar)
		vbox.pack_start(toolbar, False, False, 0)
		self.win.add(vbox)

		self.win.connect("destroy", gtk.main_quit)
		self.win.show_all()
		
if __name__ == "__main__":
	toolbar = Toolbar()
	gtk.main()
