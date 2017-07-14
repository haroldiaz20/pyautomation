# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WelcomeWindow(object):
    def setupUi(self, WelcomeWindow):
        WelcomeWindow.setObjectName("WelcomeWindow")
        WelcomeWindow.resize(601, 444)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WelcomeWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(WelcomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-20, 0, 631, 411))
        self.widget.setStyleSheet("background-color: rgb(233, 239, 255);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(10, 60, 621, 281))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.lstWidgetProjects = QtWidgets.QListWidget(self.widget_2)
        self.lstWidgetProjects.setGeometry(QtCore.QRect(50, 20, 521, 231))
        self.lstWidgetProjects.setObjectName("lstWidgetProjects")
        self.lblWelcome = QtWidgets.QLabel(self.widget)
        self.lblWelcome.setGeometry(QtCore.QRect(60, 20, 426, 23))
        self.lblWelcome.setTextFormat(QtCore.Qt.RichText)
        self.lblWelcome.setObjectName("lblWelcome")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(460, 370, 131, 20))
        self.label_2.setObjectName("label_2")
        self.btnRefreshProjectsList = QtWidgets.QPushButton(self.widget)
        self.btnRefreshProjectsList.setGeometry(QtCore.QRect(520, 20, 41, 31))
        self.btnRefreshProjectsList.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRefreshProjectsList.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefreshProjectsList.setIcon(icon1)
        self.btnRefreshProjectsList.setIconSize(QtCore.QSize(25, 25))
        self.btnRefreshProjectsList.setAutoDefault(False)
        self.btnRefreshProjectsList.setDefault(False)
        self.btnRefreshProjectsList.setFlat(True)
        self.btnRefreshProjectsList.setObjectName("btnRefreshProjectsList")
        self.btnLogout = QtWidgets.QPushButton(self.widget)
        self.btnLogout.setGeometry(QtCore.QRect(570, 20, 41, 31))
        self.btnLogout.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/logout-button-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogout.setIcon(icon2)
        self.btnLogout.setIconSize(QtCore.QSize(25, 25))
        self.btnLogout.setAutoDefault(False)
        self.btnLogout.setFlat(True)
        self.btnLogout.setObjectName("btnLogout")
        WelcomeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WelcomeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName("menubar")
        WelcomeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WelcomeWindow)
        self.statusbar.setObjectName("statusbar")
        WelcomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WelcomeWindow)
        QtCore.QMetaObject.connectSlotsByName(WelcomeWindow)

    def retranslateUi(self, WelcomeWindow):
        _translate = QtCore.QCoreApplication.translate
        WelcomeWindow.setWindowTitle(_translate("WelcomeWindow", "MainWindow"))
        self.lblWelcome.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">__TEXT__</span></p></body></html>"))
        self.label_2.setText(_translate("WelcomeWindow", "© Developed by UGO, Inc."))
        self.btnRefreshProjectsList.setToolTip(_translate("WelcomeWindow", "Refresh projects"))
        self.btnLogout.setToolTip(_translate("WelcomeWindow", "Log out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomeWindow = QtWidgets.QMainWindow()
    ui = Ui_WelcomeWindow()
    ui.setupUi(WelcomeWindow)
    WelcomeWindow.show()
    sys.exit(app.exec_())

