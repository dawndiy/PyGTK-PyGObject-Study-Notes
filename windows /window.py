#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Window
# PyGObject Study Notes By DawnDIY
# http://dawndiy.com

from gi.repository import Gtk
import sys

class MyApplication(Gtk.Application):
    def do_activate(self):
        # 建立一个属于 Application 的窗口
        window = Gtk.Window(application=self)
        # 设置标题
        window.set_title("Welcome to GNOME")
        # 显示窗口
        window.show_all()

# 新建并运行程序，退出，返回
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)