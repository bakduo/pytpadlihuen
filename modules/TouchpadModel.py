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


import os
import ConfigParser
import subprocess

class Command(object):
  def execute(self):
    raise NotImplementedError

class ClickCommand(Command):
  def __init__(self,value):
    self.option = value

  def execute(self):
     str="/usr/bin/synclient %s 2>&1 >/dev/null" % self.option
     p = subprocess.Popen(str, stdout=subprocess.PIPE, shell=True)
     (output, err) = p.communicate()
     #print "debug", err

class OffCommand(Command):
  def __init__(self,value):
     self.option = value

  def execute(self):
     str="/usr/bin/synclient %s 2>&1 >/dev/null" % self.option
     p = subprocess.Popen(str, stdout=subprocess.PIPE, shell=True)
     (output, err) = p.communicate()
     #print "debug", err

class TouchpadModel(object):
  def __init__(self):
    enabled=True
    enabledClick=True
    config=""

  def createConfigParser(self):
    if config is None:
      config=ConfigParser.ConfigParser()
      return config
    else:
      return config

  def createNewCfg(self,path):
   config = Create_ConfigParser()
   cfgfile = open(path,'w')
   config.add_section('config')
   config.set('config','enabledclick',True)
   config.set('config','enabledall', True)
   config.write(cfgfile)
   cfgfile.close()

  def configSectionMap(self,section):
    dict1 = {}
    config = Create_ConfigParser()
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

  def loadConfig(self):
    home_file = os.path.join(os.environ["HOME"], ".touchpad")
    config = createConfigParser()
    if os.path.exists(home_file):
      #print config.read(home_file)
      #print Config_Section_Map("config",config)['enabledclick']
      print "existe la configuracion"
      config.read(home_file)
      self.setEnabled(self.Config_Section_Map("config",config)['enabledall'])
      self.setClickEnabled(self.Config_Section_Map("config",config)['enabledclick'])
    else:
      print "creando archivo"
      self.createNewCfg(home_file)

 
  def getEnabled(self):
    return self.enabled

  def setEnabled(self,value):
    self.enabled=value

  def setClickEnabled(self,value):
    self.enabledClick=value
    if self.enabledClick == True:
      c=ClickCommand("TapButton1=1")
    else:
      c=ClickCommand("TapButton1=0")
    c.execute()

  def getClickEnabled(self):
    return self.enabledClick
