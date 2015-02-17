# UI
# Imort modules
import os
from gi.repository import Gtk, Vte,Pango, PangoCairo
from gi.repository import GLib, Gdk
from gi.repository import GObject
from gi.repository import GtkSource
import numpy as np
import sys
# Graphical User Interface
# Global
StatusBar = Gtk.Statusbar()
source = GtkSource.View()
buffer = source.get_buffer()
terminal = Vte.Terminal()
textview = Gtk.TextView()
textbuffer = textview.get_buffer()
entry = Gtk.Entry()
menu = Gtk.MenuBar()
filemenu = Gtk.Menu()
scrolledwindow1 = Gtk.ScrolledWindow()
vpaned = Gtk.VPaned()

# Starting Window
class MainWindow(Gtk.Window):
    file_tag = 'NoFileLoaded!'
    # Open File function
    def open_file(menuitem, user_param):
        chooser = Gtk.FileChooserDialog(title="Open a file",action=Gtk.FileChooserAction.OPEN, buttons=(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_OPEN,Gtk.ResponseType.OK))
        chooser.set_default_response(Gtk.ResponseType.OK)
        filter = Gtk.FileFilter()
        filter2 = Gtk.FileFilter()
        filter2.set_name("All Files")
        filter2.add_pattern("*.*")
        chooser.add_filter(filter2)
        response = chooser.run()
        if response == Gtk.ResponseType.OK:
            filename = chooser.get_filename()
            global file_tag
            file_tag = filename
            textbuffer = source.get_buffer()
            print "Opened File: " + filename
            StatusBar.push(0,"Opened File: " + filename)
            index = filename.replace("\\","/").rfind("/") + 1
            file = open(filename, "r")
            text = file.read()
            textbuffer.set_text(text)
            file.close()
            chooser.destroy()
        elif response == Gtk.ResponseType.CANCEL:
            chooser.destroy()
            chooser.destroy()
    def save_file(menuitem,user_param):
            textbuffer = source.get_buffer()
            StatusBar.push(0,"Saved File: " + file_tag)
            index = file_tag.replace("\\","/").rfind("/") + 1
            text = textbuffer.get_text(textbuffer.get_start_iter() , textbuffer.get_end_iter(),False)
            file = open(file_tag, "w+")
            file.write(text)
            file.close()

    def save_file_as(menuitem,user_param):
        chooser = Gtk.FileChooserDialog(title="Save file",action=Gtk.FileChooserAction.SAVE, buttons=(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_SAVE,Gtk.ResponseType.OK))
        chooser.set_default_response(Gtk.ResponseType.OK)
        filter = Gtk.FileFilter()
        filter.set_name("Text Files")
        filter.add_mime_type("text/data")
        chooser.add_filter(filter)
        filter2 = Gtk.FileFilter()
        filter2.set_name("All Files")
        filter2.add_pattern("*.*")
        chooser.add_filter(filter2)
        response = chooser.run()
        if response == Gtk.ResponseType.OK:
            filename = chooser.get_filename()
            textbuffer = source.get_buffer()
            print "Saved File: " + filename
            StatusBar.push(0,"Saved File: " + filename)
            index = filename.replace("\\","/").rfind("/") + 1
            text = textbuffer.get_text(textbuffer.get_start_iter() , textbuffer.get_end_iter(),False)
            file = open(filename, "w")
            file.write(text)
            file.close()
            chooser.destroy()
        elif response == Gtk.ResponseType.CANCEL:
            chooser.destroy()
            chooser.destroy()


    def entry_go(self,widget):
	input = entry.get_text()
	print(input)
	#Octave or Python Session Instructions
	octave_session = 'octave'
	python_session = 'python'
	if input == octave_session or input == python_session:
	  # send terminal commands
      		command= input+"\n"
        	length = len(command)
        	terminal.feed_child(command, length)
		self.box = Gtk.VBox(homogeneous=False, spacing=0)
       		self.add(self.box)
        	terminal.menu = Gtk.Menu()
        	menu_item = Gtk.ImageMenuItem.new_from_stock("gtk-copy", None)
        	menu_item.connect_after("activate", lambda w: self.copy_clipboard())
        	terminal.menu.add(menu_item)
		scrolledwindow1.remove(source)
		scrolledwindow1.add(textview)
		# Vertical Pane
 		vpaned.add1(scrolledwindow1)
        	vpaned.add2(terminal)
 		# Pack everything in vertical box
 		#self.box.pack_start(menu, False, False, 0)
        	self.box.pack_start(entry, False, False, 0)
		self.box.pack_start(vpaned, True, True, 0)
        	self.connect("delete-event", Gtk.main_quit)
        	self.show_all()

	entry.set_text(' ')
   

    def get_text(object, *args):  	
	term_input = repr(terminal.get_text(lambda *a: True))  
	file = open('term_input.txt','w+')
	file.write(term_input)
	file.close()

    def	Trap1(self,widget):
	self.box = Gtk.VBox(homogeneous=False, spacing=0)
       	self.add(self.box)
       	terminal.menu = Gtk.Menu()
       	menu_item = Gtk.ImageMenuItem.new_from_stock("gtk-copy", None)
       	menu_item.connect_after("activate", lambda w: self.copy_clipboard())
       	terminal.menu.add(menu_item)
	scrolledwindow1.remove(source)
	scrolledwindow1.add(textview)
	# Vertical Pane 
	vpaned.add1(scrolledwindow1)
        vpaned.add2(terminal)
 	# Pack everything in vertical box
 	#self.box.pack_start(menu, False, False, 0)
       	self.box.pack_start(entry, False, False, 0)
	self.box.pack_start(vpaned, True, True, 0)
       	self.connect("delete-event", Gtk.main_quit)
       	self.show_all()

    def	Trap2(self,widget):
	self.box = Gtk.VBox(homogeneous=False, spacing=0)
       	self.add(self.box)
       	terminal.menu = Gtk.Menu()
       	menu_item = Gtk.ImageMenuItem.new_from_stock("gtk-copy", None)
       	menu_item.connect_after("activate", lambda w: self.copy_clipboard())
       	terminal.menu.add(menu_item)
	scrolledwindow1.remove(source)
	scrolledwindow1.add(source)
	# Vertical Pane 
	vpaned.add1(scrolledwindow1)
        vpaned.add2(terminal)
 	# Pack everything in vertical box
 	#self.box.pack_start(menu, False, False, 0)
       	self.box.pack_start(entry, False, False, 0)
	self.box.pack_start(vpaned, True, True, 0)
       	self.connect("delete-event", Gtk.main_quit)
       	self.show_all()

    def __init__(self):
        Gtk.Window.__init__(self)
        # Window title and Icon
        self.set_title("MaeTrics")
        # Vertical Box
        self.box = Gtk.VBox(homogeneous=False, spacing=0)
        self.add(self.box)
        # Menu
        filem = Gtk.MenuItem("File")
        #Popup Menu
        terminal.menu = Gtk.Menu()
        menu_item = Gtk.ImageMenuItem.new_from_stock("gtk-copy", None)
        menu_item.connect_after("activate", lambda w: self.copy_clipboard())
        terminal.menu.add(menu_item)
        # Import
        imenu = Gtk.Menu()
        importm = Gtk.MenuItem("T.R.A.P")
        importm.set_submenu(imenu)
        itrap1 = Gtk.MenuItem("New Source")
        itrap2 = Gtk.MenuItem("TextEditor")
        imenu.append(itrap1)
        imenu.append(itrap2)
	#TRAP Signals
	itrap1.connect("activate",self.Trap1)
	itrap2.connect("activate",self.Trap2)
	#Signals for other menu items
        openm = Gtk.MenuItem("Open")
        savem = Gtk.MenuItem("Save")
        saveasm = Gtk.MenuItem("Save As")
        exit = Gtk.MenuItem("Exit")
        openm.connect("activate",self.open_file)
        saveasm.connect("activate",self.save_file_as)
        savem.connect("activate",self.save_file)
        exit.connect("activate", Gtk.main_quit)
        filemenu.append(importm)
        filemenu.append(openm)
        filemenu.append(savem)
        filemenu.append(saveasm)
        filemenu.append(exit)
        filem.set_submenu(filemenu)
        menu.append(filem)
        # Source View
        source.set_show_line_numbers(True)
        source.set_show_line_marks(True)
        source.set_highlight_current_line(True)
        source.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse("silver"))
        source.modify_fg(Gtk.StateType.NORMAL, Gdk.color_parse("black"))
	source.modify_font(Pango.FontDescription('monospace 10'))
        # Terminal settings
        terminal.set_scroll_on_output(True)
        terminal.set_scroll_on_keystroke(True)
        #terminal.set_visible(True)
        terminal.set_scrollback_lines(-1)
        terminal.set_font_from_string("monospace 10")
        terminal.set_color_background(Gdk.color_parse("black"))
        terminal.set_color_foreground(Gdk.color_parse("silver"))
        terminal.set_cursor_blink_mode(True)
	terminal.connect("child-exited", lambda w: gtk.main_quit())
	terminal.set_encoding("UTF-8")
        terminal.fork_command_full(Vte.PtyFlags.DEFAULT,os.environ['HOME'],["/bin/sh"],[],GLib.SpawnFlags.DO_NOT_REAP_CHILD,None,None,)
        # send terminal commands
        #command= "ls\n"
        #length = len(command)
        #terminal.feed_child(command, length)
	terminal.connect("commit", self.get_text)
        #Text entry
	entry.connect("activate",self.entry_go)
	input = entry.get_text()
	#Octave or Python Session Instructions
	octave_session = 'octave'
	python_session = 'python'
        # Scrolled Text Window
        scrolledwindow1.set_hexpand(True)
        scrolledwindow1.set_vexpand(True)
        scrolledwindow1.set_border_width(10)
	scrolledwindow1.add(source)
        # Vertical Pane
 	vpaned.add1(scrolledwindow1)
        vpaned.add2(terminal)
        # Pack everything in vertical box
 	self.box.pack_start(menu, False, False, 0)
        self.box.pack_start(entry, False, False, 0)
	self.box.pack_start(vpaned, True, True, 0)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


window = MainWindow()
Gtk.main()

