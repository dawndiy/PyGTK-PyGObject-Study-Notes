#!/usr/bin/env python
# -*- coding: utf-8 -*
# Toolbar
# PyGtk Stady Notes By DawnDIY
# http://www.dawndiy.com 

from gi.repository import Gtk

class MessageDialogWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="MessageDialog Example")

		box = Gtk.Box(spacing=6)
		self.add(box)
	
		button1 = Gtk.Button("信息")
		button1.connect("clicked", self.on_info_clicked)
		box.add(button1)

		button2 = Gtk.Button("错误")
		button2.connect("clicked", self.on_error_clicked)
		box.add(button2)

		button3 = Gtk.Button("警告")
		button3.connect("clicked", self.on_warn_clicked)
		box.add(button3)

		button4 = Gtk.Button("询问")
		button4.connect("clicked", self.on_question_clicked)
		box.add(button4)

	def on_info_clicked(self, widget):
		dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
		Gtk.ButtonsType.OK, "这是一个信息消息对话框")
		dialog.format_secondary_text(
		"这里是副文本用于说明信息。")
		dialog.run()
		print "INFO dialog closed"

		dialog.destroy()

	def on_error_clicked(self, widget):
		dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
		Gtk.ButtonsType.CANCEL, "这是一个错误消息对话框")
		dialog.format_secondary_text("这里是副文本用于说明信息。")
		dialog.run()
		print "ERROR dialog closed"

		dialog.destroy()

	def on_warn_clicked(self, widget):
		dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
		Gtk.ButtonsType.OK_CANCEL, "这是一个警告消息对话框")
		dialog.format_secondary_text(
		"这里是副文本用于说明信息。")
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			print "OK button is clicked"
		elif response == Gtk.ResponseType.CANCEL:
			print "CANCEL button is clicked"

		dialog.destroy()

	def on_question_clicked(self, widget):
		dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION,
		Gtk.ButtonsType.YES_NO, "这是一个询问消息对话框")
		dialog.format_secondary_text(
		"这里是副文本用于说明信息。")
		response = dialog.run()
		if response == Gtk.ResponseType.YES:
			print "YES button is clicked"
		elif response == Gtk.ResponseType.NO:
			print "NO button is clicked"

		dialog.destroy()

win = MessageDialogWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
