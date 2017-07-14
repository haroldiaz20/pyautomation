from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import sys
from views.confirmalert import Ui_dlgConfirmation


class ConfirmAlertUiController(Ui_dlgConfirmation):
	
    INFO_DIALOG = 1
    WARNING_DIALOG = 2
    SUCCESS_DIALOG = 3
	
    def __init__(self, dialog):
        Ui_dlgConfirmation.__init__(self)
		
        # Hide help icon from title bar
        dialog.setWindowFlags(QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        dialog.setWindowModality(QtCore.Qt.WindowModal)
		
        self.setupUi(dialog)
        self.btnConfirmDialog.setVisible(True)
        self.btnCancelDialog.setVisible(True)
        #self.btnConfirmDialog.clicked.connect(self.buttonOkClicked)
		
        self.mainWindow = QtWidgets.QMainWindow()
	
    def buttonOkClicked(self):
        return strCallbackMethod
		
    def setTypeDialog(self, typeDialog):
        self.typeDialog = typeDialog
        # Change dialog icon
        self.imageIcon = self.findDialogIcon()
        self.lblConfirmIcon.setPixmap(self.imageIcon)
		
	
    def findDialogIcon(self):		
        if self.typeDialog == self.INFO_DIALOG:
            return QtGui.QPixmap("images/info-icon.png")
			
        elif self.typeDialog == self.WARNING_DIALOG:
            return QtGui.QPixmap("images/warning-icon.png")
			
        else:
            return QtGui.QPixmap("images/info-icon.png")
	
    def setMessage(self, message):
        self.lblConfirmMessage.setText(message)
	
    def setOkButtonAction(self, strActionName):
        self.strCallbackMethod = strActionName
		
    def setTitle(self, title):
        self.lblConfirmTitle.setText(str(title))
	
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = ConfirmAlertUiController(dialog)
    dialog.show()
    sys.exit(app.exec_())
	
	
	
	