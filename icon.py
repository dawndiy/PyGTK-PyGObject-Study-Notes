#!/usr/bin/env python

import gtk

class PyApp(gtk.Window):
	def __init__(self):
		super(PyApp, self).__init__()

		self.set_title("Icon")
		self.set_size_request(250, 150)
		self.set_position(gtk.WIN_POS_CENTER)

		try:
			self.set_icon_from_file("images/icon.xpm")
		except Exception, e:
			print e.message
			sys.exit(1)
			
		self.connect("destroy", gtk.main_quit)
		
		self.show()
		
if __name__ == "__main__":
	pyapp = PyApp()
	gtk.main()
