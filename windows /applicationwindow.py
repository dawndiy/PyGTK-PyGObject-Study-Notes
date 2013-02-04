#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Window
# PyGObject Study Notes By DawnDIY
# http://dawndiy.com

from gi.repository import Gtk
import sys

# Gtk 应用窗口
class MyWindow(Gtk.ApplicationWindow):
    # 构造器：设置标题，和窗口所属
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)

class MyApplication(Gtk.Application):
    # Gtk Application 的构造器
    def __init__(self):
        Gtk.Application.__init__(self)

    # 新建并激活一个属于该应用本身的 MyWindow。
    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    # 启动应用程序
    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)