from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import sys
from controllers.confirmalertctrl import ConfirmAlertUiController
from controllers.projectsctrl import ProjectsUiController
from controllers.welcomectrl import WelcomeController
from utils.connection import ConnectionWS
from views.login import Ui_dlgLogin
import time

class MyFirstGuiProgram(Ui_dlgLogin):
    def __init__(self, dialog):
        Ui_dlgLogin.__init__(self)
        ## Remove close button
        dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        dialog.setWindowFlags(QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        dialog.resize(325, 439)
        dialog.setFixedSize(dialog.width(), dialog.height())
        self.setupUi(dialog)
		
        self.mainWindow = QtWidgets.QMainWindow()		
        # Set button background color
        #self.btnLogin.setStyleSheet('QPushButton {background-color: #57c7d4; border-color:#57c7d4; color: white; box-shadow: 0 0 2px rgba(0, 0, 0, 0.18), 0 2px 4px rgba(0, 0, 0, 0.21)}')
		
		
        # Add signal (event) to this control
        #self.btnLogin.clicked.connect(self.loginUser)
        self.btnLogin.clicked.connect(lambda:self.loginUser(dialog))
        # Add signal to this control
        self.btnCancelLogin.clicked.connect(self.cancelLogin)
        # Let's set the focus to this control
        self.txtEditUsername.setFocus()	
        
        
		
		
    def cancelLogin(self):
        self.confirmDialog = QtWidgets.QDialog()		
		
        self.ui = ConfirmAlertUiController(self.confirmDialog)
        self.ui.setTitle("Sure you wanna exit this app?")
        self.ui.setTypeDialog(ConfirmAlertUiController.WARNING_DIALOG)
        self.ui.setMessage("You are about to exit this app, please confirm or cancel in order to continue...")
		
        # Attach events to buttons
        self.ui.btnConfirmDialog.clicked.connect(self.btnOkConfirmDialog_Click)
        #self.ui.setOkButtonAction(MyFirstGuiProgram.btnCancelConfirmDialog_Click)
        self.ui.btnCancelDialog.clicked.connect(self.btnCancelConfirmDialog_Click)
		
        # Change confirm dialog title
        self.confirmDialog.setWindowTitle("You really wanna quit UGOBoot?")
        # Show dialog
        self.confirmDialog.show()
		
        #QtCore.QCoreApplication.instance().quit()
        #self.txtEditUsername.setText('')
        #self.txtEditPassword.setText('')
        #self.txtEditUsername.setFocus()
		
    def btnOkConfirmDialog_Click(self):
        QtCore.QCoreApplication.instance().quit()
	
    def btnCancelConfirmDialog_Click(self):
        self.confirmDialog.close()
	
    # Define the slot (method)
    def loginUser(self, Dialog):
        
        
        
        #self.dlgProjects = QtWidgets.QDialog()
        #self.ui = Ui_dlgProjects()
        #self.ui.setupUi(self.dlgProjects)
        #self.dlgProjects.show()
		
        conn = ConnectionWS()
        conn.addParam(('func', str(ConnectionWS.USER_LOGIN)))
        conn.addParam(('email', str(self.txtEditUsername.text())))
        conn.addParam(('password', str(self.txtEditPassword.text())))
        conn.generateUrl()
        conn.makeRequest()
        if(conn.response['status'] == 1):
                      
            print(conn.response)
            
            self.welcomeWindow = QtWidgets.QMainWindow()
            
            self.ui = WelcomeController(self.mainWindow, conn.response['data'][0]['Email'], conn.response['data'][0]['TokenLogin'])
            self.ui.setWelcomeMessage(conn.response['data'][0]['Firstname'])
            
            # Pass the ID TESTER param
            self.ui.setIdTester(conn.response['data'][0]['IdTester'])
            
            # Let's load all projects for this user (tester)
            self.ui.loadProjects()
            
            Dialog.hide()
            
            self.mainWindow.show()
            return
            
            self.dlgProjects = QtWidgets.QDialog()
                        
            self.ui = ProjectsUiController(self.dlgProjects, conn.response['data'][0]['Email'], conn.response['data'][0]['TokenLogin'])
            self.ui.setWelcomeMessage(conn.response['data'][0]['Firstname'])
            
            # Pass the ID TESTER param
            self.ui.setIdTester(conn.response['data'][0]['IdTester'])
            
            # Let's load all projects for this user (tester)
            self.ui.loadProjects()
            self.dlgProjects.show()
            
            Dialog.close()
        else:
            print(conn.response)
            self.confirmDialog = QtWidgets.QDialog()		
            self.ui = ConfirmAlertUiController(self.confirmDialog)
            self.ui.setTitle("There was an error:")
            self.ui.setTypeDialog(ConfirmAlertUiController.WARNING_DIALOG)
            self.ui.setMessage("[" + conn.response['message'] + "]")
			
            # Attach events to buttons
            self.ui.btnConfirmDialog.clicked.connect(self.btnOKAlertDialog)
            #self.ui.setOkButtonAction(MyFirstGuiProgram.btnCancelConfirmDialog_Click)
            self.ui.btnCancelDialog.setVisible(False)
			
            # Change confirm dialog title
            self.confirmDialog.setWindowTitle("Warning")
            # Show dialog
            self.confirmDialog.show()
	
    def btnOKAlertDialog(self):
        self.confirmDialog.close()
			
    def addInputTextToListbox(self):
        txt = self.myTextInput.text()
        self.listWidget.addItem(txt)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
#	pixmap = QtGui.QPixmap("images/icon-testing_full.png")
#	pixmapResized = pixmap.scaledToWidth(200)
#	splash_pix = pixmapResized
#	
#	splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
#	splash.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
#	splash.setEnabled(False)
#	
#	#splash = QtWidgets.QSplashScreen(splash_pix)
#	# adding progress bar
#	progressBar = QtWidgets.QProgressBar(splash)
#	color = "#4397e6"
#	template_css = """QtWidgets.QProgressBar::chunk { background: %s; }"""
#	css = template_css % color
#	progressBar.setStyleSheet(css)
#	progressBar.setTextVisible(False)
#	progressBar.setMaximum(10)
#	progressBar.setGeometry(0, splash_pix.height()-10, splash_pix.width(), 5)
#	
#	#splash.setMask(splash_pix.mask())
#	
#	splash.show()
#	splash.showMessage("<h2><font color='#FFFFFF'>Welcome to UGOBot!</font></h2>", QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter, QtCore.Qt.black)
#	
#	for i in range(1, 11):
#		progressBar.setValue(i)
#		t = time.time()
#		while time.time() < t + 0.4:
#			app.processEvents()
    # Simulate something that takes time
    #time.sleep(1)
    #splash.close()
	
    dialog = QtWidgets.QDialog()
    prog = MyFirstGuiProgram(dialog)
    dialog.show()
    sys.exit(app.exec_())
