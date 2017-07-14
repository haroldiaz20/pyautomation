#from cx_Freeze import setup, Executable
#import sys
#
#base = None
#
#base = None
#if sys.platform == "win32":
#    base = "Win32GUI"
#
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
#executables = [Executable("main.py", base=base)]
#
#
#setup(
#    name = "rt",
#    options = {"build_exe": build_exe_options},
#    version = "1.0",
#    description = 'eeee',
#    executables = executables
#)
#


from cx_Freeze import Executable
from cx_Freeze import setup
import sys

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit',
        'include_files': ['images', 'winium', 'webdrivers', 'logs'],
    }
}

executables = [
    Executable('main.py', base=base, icon='images/icon.ico', shortcutName="Testing App", shortcutDir="DesktopFolder",copyright="Unified Group Online")
]

# https://stackoverflow.com/questions/24195311/how-to-set-shortcut-working-directory-in-cx-freeze-msi-bundle

setup(name='TestingApp',
      version='0.1.7',
      description='Testing Application Desktop Client. Changed webdriver configuration.',
      options=options,
      executables=executables
      )