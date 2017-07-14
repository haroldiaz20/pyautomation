# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Harold\projects\python\TestingDesktop\src\confirmalert.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgConfirmation(object):
    def setupUi(self, dlgConfirmation):
        dlgConfirmation.setObjectName("dlgConfirmation")
        dlgConfirmation.setWindowModality(QtCore.Qt.WindowModal)
        dlgConfirmation.resize(446, 279)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlgConfirmation.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(dlgConfirmation)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(dlgConfirmation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: rgb(233, 239, 255);")
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 40, 451, 181))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lblConfirmMessage = QtWidgets.QLabel(self.frame)
        self.lblConfirmMessage.setGeometry(QtCore.QRect(110, 20, 301, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblConfirmMessage.setFont(font)
        self.lblConfirmMessage.setWordWrap(True)
        self.lblConfirmMessage.setObjectName("lblConfirmMessage")
        self.lblConfirmIcon = QtWidgets.QLabel(self.frame)
        self.lblConfirmIcon.setGeometry(QtCore.QRect(30, 20, 61, 61))
        self.lblConfirmIcon.setText("")
        self.lblConfirmIcon.setPixmap(QtGui.QPixmap("images/info-icon.png"))
        self.lblConfirmIcon.setScaledContents(True)
        self.lblConfirmIcon.setObjectName("lblConfirmIcon")
        self.lblConfirmTitle = QtWidgets.QLabel(self.widget)
        self.lblConfirmTitle.setGeometry(QtCore.QRect(60, 10, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblConfirmTitle.setFont(font)
        self.lblConfirmTitle.setObjectName("lblConfirmTitle")
        self.btnConfirmDialog = QtWidgets.QPushButton(self.widget)
        self.btnConfirmDialog.setGeometry(QtCore.QRect(310, 240, 101, 23))
        self.btnConfirmDialog.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(0, 0, 255);")
        self.btnConfirmDialog.setAutoDefault(False)
        self.btnConfirmDialog.setDefault(False)
        self.btnConfirmDialog.setFlat(False)
        self.btnConfirmDialog.setObjectName("btnConfirmDialog")
        self.btnCancelDialog = QtWidgets.QPushButton(self.widget)
        self.btnCancelDialog.setGeometry(QtCore.QRect(200, 240, 91, 23))
        self.btnCancelDialog.setStyleSheet("background-color: rgb(233, 239, 255);\n"
"background-color: rgb(225, 225, 225);")
        self.btnCancelDialog.setAutoDefault(False)
        self.btnCancelDialog.setFlat(False)
        self.btnCancelDialog.setObjectName("btnCancelDialog")
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(dlgConfirmation)
        QtCore.QMetaObject.connectSlotsByName(dlgConfirmation)

    def retranslateUi(self, dlgConfirmation):
        _translate = QtCore.QCoreApplication.translate
        dlgConfirmation.setWindowTitle(_translate("dlgConfirmation", "Quit UGOBoot?"))
        self.lblConfirmMessage.setText(_translate("dlgConfirmation", "You won\'t be able to send or recieve instant call and messages if you do."))
        self.lblConfirmTitle.setText(_translate("dlgConfirmation", "Sure you want to exit UGOBoot?"))
        self.btnConfirmDialog.setText(_translate("dlgConfirmation", "OK"))
        self.btnCancelDialog.setText(_translate("dlgConfirmation", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgConfirmation = QtWidgets.QDialog()
    ui = Ui_dlgConfirmation()
    ui.setupUi(dlgConfirmation)
    dlgConfirmation.show()
    sys.exit(app.exec_())

