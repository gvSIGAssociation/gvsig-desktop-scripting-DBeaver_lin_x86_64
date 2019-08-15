# encoding: utf-8

import gvsig
from gvsig import getResource

import thread
import os.path
import subprocess
import shutil

from java.lang import System
from java.io import File
from java.io import FileInputStream
from java.io import FileOutputStream
from java.util import Properties

from org.apache.commons.io import FileUtils
from org.gvsig.andami import PluginsLocator
from org.gvsig.scripting.app.extension import ScriptingExtension
from org.gvsig.scripting.swing.api import ScriptingSwingLocator, JScriptingComposer
from org.gvsig.tools import ToolsLocator

import javax.swing.ImageIcon
import javax.imageio.ImageIO
from javax.swing import AbstractAction, Action
from org.gvsig.scripting import ScriptingLocator

def getDataFolder():
  return ScriptingLocator.getManager().getDataFolder("dbeaver").getAbsolutePath()

def launchDBeaver():
  #pluginsManager = PluginsLocator.getManager()
  #appfolder = pluginsManager.getApplicationFolder().getAbsolutePath()
  
  #java = os.path.join( System.getProperties().getProperty("java.home"), "bin", "java")

  dbeaverhome = getResource(__file__, "app").replace("\\","/")
  #settings = getDataFolder().replace("\\","/")

  cmd = [
    dbeaverhome+"/dbeaver",
  ]
  #print cmd
  subprocess.call(cmd)


class DBeaverAction(AbstractAction):

  def __init__(self):
    AbstractAction.__init__(self,"DBeaver")
    self.putValue(Action.ACTION_COMMAND_KEY, "DBeaver")
    self.putValue(Action.SMALL_ICON, self.load_icon(getResource(__file__,"images","dbeaver16x16.png")))
    self.putValue(Action.SHORT_DESCRIPTION, "DBeaver")

  def load_icon(self, afile):
    if not isinstance(afile,File):
      afile = File(str(afile))
    return javax.swing.ImageIcon(javax.imageio.ImageIO.read(afile))

  def actionPerformed(self,e):
    #composer = e.getSource().getContext()
    thread.start_new_thread(launchDBeaver,tuple())

def selfRegister():
  i18nManager = ToolsLocator.getI18nManager()
  manager = ScriptingSwingLocator.getUIManager()
  action = DBeaverAction()
  manager.addComposerTool(action)
  manager.addComposerMenu(i18nManager.getTranslation("Tools"),action)

def main(*args):
  thread.start_new_thread(launchDBeaver,tuple())
