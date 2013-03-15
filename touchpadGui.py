#!/usr/bin/python

#Importamos la libreria pygtk
import pygtk
#Especificamos la version de pygtk a usar, normalmente la 2.0
pygtk.require("2.0")
#Importamos la libreria gtk
import gtk
import time
import os
import sys
from modules.TouchpadModel import TouchpadModel

class TouchPadGui(object):
  def __init__(self):
    # Cargamos el constructor de gtk y lo llamamos builder
    #variables
    self.model=TouchpadModel()
    self.builder = gtk.Builder()
    self.builder.add_from_file("pygtktouchpad.glade")
    # Conectamos signal de cerrar ventana
    self.builder.connect_signals({
    "exitApp" : gtk.main_quit,
    "disabledClickTp" : self.disabledClickTp,
    "enabledClickTp" : self.enabledClickTp,
    "disabledAllTp" : self.disableAllTp,
    "enabledAllTp" : self.enabledAllTp
    })
    
    self.window = self.builder.get_object("window1")
    self.window.set_size_request(350, 200)
    self.window.set_title("Touchpad")
    self.window.connect("delete_event", self.on_delete)
    self.window.show()

  def on_delete(self, widget, *args):
    gtk.main_quit()

  def disabledClickTp(self,evento):
    self.model.setClickEnabled(False)
    print "disabled"

  def enabledClickTp(self,evento):
    self.model.setClickEnabled(True)
    print "enabled"

  def disableAllTp(self,evento):
    print "disabled all"

  def enabledAllTp(self,evento):
    print "enabled"


if __name__ == "__main__":
        app = TouchPadGui()
        gtk.main()

