from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from controllers.confirmalertctrl import ConfirmAlertUiController
import sys
import os
import threading
from views.projectdetails import Ui_dlgProjectDetails
from utils.auto_web import AutoWeb
from utils.auto_desktop import AutoDesktop

class ProjectDetailsUiController(Ui_dlgProjectDetails):
    def __init__(self, dialog, projectName , dialogP):
        
        #super(ProjectDetailsUiController, self).__init__(parent)
        
        Ui_dlgProjectDetails.__init__(self)
        
        self.dialogGeneralDetail = dialog
        self.dialogGeneralProjects = dialogP
        self.setupUi(dialog)
        
        dialog.setWindowFlags(QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint )
        dialog.setFixedSize(dialog.width(), dialog.height())
        dialog.setWindowTitle(projectName + " - Details")		
        
        self.mainWindow = QtWidgets.QMainWindow()
        self.lblProjectName.setText("Project Name : " + str(projectName))
        self.lblProjectName.setStyleSheet('''color: rgb(0, 0, 0);font-size: 14px;font-weight:bold;''')
       
        self.lblProjectDetails.setStyleSheet('''color: rgb(0, 0, 0);font-size: 12px;font-weight:400;''')
       
        self.projectId = 0
        self.projectPath = ""
        
        # Add event to click test button
        self.btnClickTest.clicked.connect(self.TestApp)
        self.btnClickPlay.clicked.connect(self.playApp)
        
        
    def setProjectId(self, id):
        self.projectId = id
        print("Detalle Proyecto ID: %s" % (self.projectId))
        
    def setType(self, type):
        self.Type = type
        print("Detalle  Type: %s" % (self.Type))

    def getType(self):
        return self.Type
    
    def setToken(self, token):
        self.Token = token
        print("Detalle Token: %s" % (self.Token))

    def getToken(self):
        return self.Token

    def setIdTester(self, idtester):
        self.IdTester = idtester
        print("Detalle IdTester: %s" % (self.IdTester))

    def getIdTester(self):
        return self.IdTester
        
    def setProjectName(self, name):
        self.projectName = name
	
    def getProjectName(self):
        return self.projectName
    
    def setProjectPath(self, path):
        self.projectPath = path
        print("Detalle Path or URL: %s" % (self.projectPath))
    
    def getProjectPath(self):
        return self.projectPath
    
    """
    Methods for reloading UIs
    """
    def RefreshDescriptionLabel(self):
        self.lblProjectDetails.setText("""
        PATH: %s \n
        APPLICATION TYPE: %s \n
        """ % (self.getProjectPath(), self.getType()))
        
    
    def TestApp(self):
        self.confirmDialog = QtWidgets.QDialog()		
        self.ui = ConfirmAlertUiController(self.confirmDialog)
        self.ui.setTitle("Sure you wanna run a TEST?")
        self.ui.setTypeDialog(ConfirmAlertUiController.WARNING_DIALOG)
        self.ui.setMessage("""You are about to make a TEST for this app, please keep in mind those considerations: \n 
        1) This TEST WON'T generate any report.
        2) You SHOULDN'T move your mouse or run another app while the test is running.\n
        Please confirm or cancel in order to continue...""")
        # Attach events to buttons
        self.ui.btnConfirmDialog.clicked.connect(self.testAppExec)
        self.ui.btnCancelDialog.clicked.connect(self.confirmDialog.close)
        # Change confirm dialog title
        self.confirmDialog.setWindowTitle("You really run this TEST?")
        # Show dialog
        self.confirmDialog.show()
    
    def playApp(self):
        self.confirmDialog = QtWidgets.QDialog()		
        self.ui = ConfirmAlertUiController(self.confirmDialog)
        self.ui.setTitle("Sure you wanna play a TEST?")
        self.ui.setTypeDialog(ConfirmAlertUiController.WARNING_DIALOG)
        self.ui.setMessage("""You are about to play a TEST for this app, please keep in mind those considerations: \n 
        1) This TEST WILL generate some reports.
        2) You SHOULDN'T move your mouse or run another app while the test is running.\n
        Please confirm or cancel in order to continue...""")
        # Attach events to buttons
        self.ui.btnConfirmDialog.clicked.connect(self.playAppExec)
        self.ui.btnCancelDialog.clicked.connect(self.confirmDialog.close)
        # Change confirm dialog title
        self.confirmDialog.setWindowTitle("You really wanna play this TEST?")
        # Show dialog
        self.confirmDialog.show()
    
    def testAppExec(self):
        self.dialogGeneralDetail.showMinimized()
        self.dialogGeneralProjects.showMinimized()
        #self.confirmDialog.showMinimized()
        
        #web
        if(self.Type==1):
            self.web = AutoWeb()
            self.web.setInfo(self.Token,self.IdTester,self.projectId,self.projectPath)
            self.web.execAutoWeb(1)
        #desktop
        if(self.Type==2):
            #pathfinal = os.getcwd()+'\winium\Winium.Desktop.Driver.exe'
            #os.system(pathfinal)           
            self.desktop = AutoDesktop()
            self.desktop.setInfo(self.Token,self.IdTester,self.projectId,self.projectPath)
            #self.desktop.execAutoDesktop(1)
            download_thread = threading.Thread(target=self.desktop.execAutoDesktop, args=(1,))
            download_thread.start()
            #download_thread.isAlive()
        
        self.confirmDialog.close()
    
    def playAppExec(self):
        self.dialogGeneralDetail.showMinimized()
        self.dialogGeneralProjects.showMinimized()
        #web
        if(self.Type==1):
            self.web = AutoWeb()
            self.web.setInfo(self.Token,self.IdTester,self.projectId,self.projectPath)
            self.web.execAutoWeb(2)
        #desktop
        if(self.Type==2):
            self.desktop = AutoDesktop()
            self.desktop.setInfo(self.Token,self.IdTester,self.projectId,self.projectPath)
            #self.desktop.execAutoDesktop(2)
            download_thread = threading.Thread(target=self.desktop.execAutoDesktop, args=(2,))
            download_thread.start()
            #download_thread.isAlive()
       
        
        self.confirmDialog.close()
       
     
        
		
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    projectName = ""
    prog = ProjectDetailsUiController(dialog, projectName)
    dialog.show()
    sys.exit(app.exec_())
	
	
	
	