#!/usr/bin/python

#############################################################################
#   App para desactivar click en los touchpad                               #
#   Copyright (C) 2013 linuxknow@gmail.com                                  #
#                                                                           #
#   This program is free software: you can redistribute it and/or modify    #
#   it under the terms of the GNU General Public License as published by    #
#   the Free Software Foundation, either version 3 of the License, or       #
#   (at your option) any later version.                                     #
#                                                                           #
#   This program is distributed in the hope that it will be useful,         #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#   GNU General Public License for more details.                            #
#                                                                           #
#   You should have received a copy of the GNU General Public License       #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>    #
#                                                                           #
#############################################################################


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

