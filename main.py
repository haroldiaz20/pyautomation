# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import inspect
import os
import sys

from controllers.loginctrl import MyFirstGuiProgram

if __name__ == "__main__":
    print(sys.path)
    print("Hello World")
    ruta = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
    print(ruta)
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = MyFirstGuiProgram(dialog)
    dialog.show()
    sys.exit(app.exec_())
    