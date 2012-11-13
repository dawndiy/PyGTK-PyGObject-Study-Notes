#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Label Example
# PyGObject Stady Notes By DawnDIY
# http://dawndiy.com

from gi.repository import Gtk

class LabelWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Label Example")
		hbox = Gtk.Box(spacing=10)
		hbox.set_homogeneous(False)
		vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		vbox_left.set_homogeneous(False)
		vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		vbox_right.set_homogeneous(False)
		hbox.pack_start(vbox_left, True, True, 0)
		hbox.pack_start(vbox_right, True, True, 0)
		label = Gtk.Label("这是一个普通 label")
		vbox_left.pack_start(label, True, True, 0)
		label = Gtk.Label()
		label.set_text("这是一个左对齐的 label。\n包含多行。")
		label.set_justify(Gtk.Justification.LEFT)
		vbox_left.pack_start(label, True, True, 0)
		label = Gtk.Label("这是一个右对齐的 label。\n包含多行。")
		label.set_justify(Gtk.Justification.RIGHT)
		vbox_left.pack_start(label, True, True, 0)
		label = Gtk.Label("这是一个多行显示的 label 示例。它"
							"不是占据所有能容纳下它的"
							"宽度，而是自动的换行调整适应。\n"
							"并且它支持多段落正确的显示，"
							"正确的补充额外的空间。")
		label.set_line_wrap(True)
		vbox_right.pack_start(label, True, True, 0)
		label = Gtk.Label("这是一个多行显示的 label 示例，填充式 label 。"
							"它会占据所有能容纳下它的宽度。 "
							"好，来几个句子证明我的说法。"
							"这又是一个句子。又来一个句子，巴拉巴拉巴拉。\n"
							"这是一个新段落~\n"
							"好吧，这又是一个扯淡的段落，扯点"
							"什么呢？元芳，你怎么看啊？呵呵~")
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		vbox_right.pack_start(label, True, True, 0)
		label = Gtk.Label()
		label.set_markup("文本内容可以 <small>小</small>, <big>大</big>, "
							"<b>粗体</b>, <i>斜体</i> 甚至可以是超链接 "
							" <a href=\"http://dawndiy.com\" "
							"title=\"点击试一试\">网络</a>.")
		label.set_line_wrap(True)
		vbox_left.pack_start(label, True, True, 0)
		label = Gtk.Label.new_with_mnemonic("按下 Alt + P 来选择右边的按钮 (_P)")
		vbox_left.pack_start(label, True, True, 0)
		label.set_selectable(True)
		button = Gtk.Button(label="点一下试一试")
		label.set_mnemonic_widget(button)
		vbox_right.pack_start(button, True, True, 0)
		self.add(hbox)

window = LabelWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
