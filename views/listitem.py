# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Harold\projects\python\Testing\testing\listitem.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(325, 126)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblProjectName = QtWidgets.QLabel(Form)
        self.lblProjectName.setObjectName("lblProjectName")
        self.verticalLayout.addWidget(self.lblProjectName)
        self.lblProjectDesc = QtWidgets.QLabel(Form)
        self.lblProjectDesc.setObjectName("lblProjectDesc")
        self.verticalLayout.addWidget(self.lblProjectDesc)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblProjectName.setText(_translate("Form", "PROJECT NAME"))
        self.lblProjectDesc.setText(_translate("Form", "PROJECT DESCRIPTION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

