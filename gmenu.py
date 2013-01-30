#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GMenu & SimpleActions
# PyGObject Study Notes By DawnDIY
# http://dawndiy.com

from gi.repository import Gtk
from gi.repository import Gio
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="GMenu Example", application=app)

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup (self):
        # 启动应用
        Gtk.Application.do_startup(self)

        # 建立菜单
        menu = Gio.Menu()
        # 向菜单添加3个选项
        menu.append("New", "app.new")
        menu.append("About", "app.about")
        menu.append("Quit", "app.quit")
        # 将该菜单添加成应用的菜单 
        self.set_app_menu(menu)

        # 为菜单 new 选项添加动作
        new_action = Gio.SimpleAction.new("new", None)
        # 连接到回调函数 new_cb
        new_action.connect("activate", self.new_cb)
        # 将动作添加到应用中 
        self.add_action(new_action)

        # about 选项
        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.about_cb)
        self.add_action(about_action)

        # quit 选项 
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.quit_cb)
        self.add_action(quit_action)

    # new 的回调函数 
    def new_cb(self, action, parameter):
        print("This does nothing. It is only a demonstration.")

    # about 的回调函数 
    def about_cb(self, action, parameter):
        print("No AboutDialog for you. This is only a demonstration.")

    # about 的回调函数 
    def quit_cb(self, action, parameter):
        print("You have quit.")
        self.quit()

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
