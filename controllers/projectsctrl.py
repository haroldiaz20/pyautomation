import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


from controllers.projectdetailsctrl import ProjectDetailsUiController
from utils.connection import ConnectionWS
from views.projects import Ui_dlgProjects

import subprocess



class QCustomQWidget(QtWidgets.QWidget):
    def __init__ (self, parent=None):
        super(QCustomQWidget, self).__init__(parent)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblProjectName = QtWidgets.QLabel()
        self.lblProjectName.setObjectName("lblProjectName")
        self.verticalLayout.addWidget(self.lblProjectName)
        self.lblProjectDesc = QtWidgets.QLabel()
        self.lblProjectDesc.setObjectName("lblProjectDesc")
        self.verticalLayout.addWidget(self.lblProjectDesc)
        self.horizontalLayout.addLayout(self.verticalLayout)
        
        self.setLayout(self.horizontalLayout)
      
        self.lblProjectName.setStyleSheet('''color: rgb(0, 0, 0);font-size: 20px;font-weight:bold;background-color: rgba(0,0,0,0%);''')
        self.lblProjectDesc.setStyleSheet('''color: rgb(118, 131, 143);background-color: rgba(0,0,0,0%);''')
        self.value = ""
        

	
    def setValue(self, newValue):
        self.value = newValue
		
    def setTextUp (self, text):
        self.lblProjectName.setText(text)
	
    def setTextDown (self, text):
        self.lblProjectDesc.setText(text)
	
    def setIcon (self, imagePath):
        pixmap = QtGui.QPixmap(imagePath)
        pixmapResized = pixmap.scaledToWidth(80)
        self.iconQLabel.setPixmap(pixmapResized)
		
    def getValue(self):
        return self.value
		
    def getText (self):
        return self.lblProjectName.text()
    
    def getType(self):
        return self.type
		
    def setType (self, type):
        self.type = type
    
    def setPath(self, path):
        self.projectPath = path
    
    def getPath(self):
        return self.projectPath
	

class ProjectsUiController(Ui_dlgProjects):
    
    def __init__(self, dialog, username=None, token=None):
        Ui_dlgProjects.__init__(self)
        
        self.setupUi(dialog)
        self.dialogGeneralProjects = dialog
        dialog.setWindowFlags(QtCore.Qt.WindowTitleHint  | QtCore.Qt.WindowMinimizeButtonHint)  #| QtCore.Qt.WindowCloseButtonHint
        dialog.setFixedSize(dialog.width(), dialog.height())
        
        self.mainWindow = QtWidgets.QMainWindow()
        self.lstWidgetProjects.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.lstWidgetProjects.itemClicked.connect(self.itemClickedEvent)
		
        # Pass the token & username params
        self.username = username
        self.firstName = ""
        self.token = token
        
        #self.loadProjects()
        
        # Change welcome text
        #newWelcomeText = self.lblWelcome.text().replace('__TEXT__', 'Welcome, %s' % (self.firstName))		
        #self.lblWelcome.setText(newWelcomeText)
        # Change window title
        dialog.setWindowTitle(self.username + " - My projects")	
        
        # Add event to refresh button
        self.btnRefreshProjectsList.clicked.connect(self.reloadProject)
        self.btnLogout.clicked.connect(self.closeIt) 
        
        try:       
            self.dialogo = dialog
            os.system("taskkill /f /im  Winium.Desktop.Driver.exe")
            SW_HIDE = 0
            info = subprocess.STARTUPINFO()
            info.dwFlags = subprocess.STARTF_USESHOWWINDOW
            info.wShowWindow = SW_HIDE
            self.process = subprocess.Popen(r'winium\Winium.Desktop.Driver.exe', startupinfo=info)        
            #subprocess.Popen(['winium\Winium.Desktop.Driver.exe'], stderr=subprocess.PIPE)
        except BaseException as e:
            print("Error save log "+ str(e))
       
            
    def closeIt(self):
        try:
            self.process.terminate()
            self.dialogo.close()
        except BaseException as e:
            self.dialogo.close()
            print("Error save log "+ str(e))

    def setIdTester(self, idTester):
        self.idTester = idTester
        
    def setWelcomeMessage(self, firstName):
        # Change welcome text
        self.firstName = firstName.title()
        newWelcomeText = self.lblWelcome.text().replace('__TEXT__', 'Welcome, %s' % (firstName))		
        self.lblWelcome.setText(newWelcomeText)
    
    def loadProjects(self):
        if self.idTester is None:
            print('No existe este parametro')
        else:
            print("IDDD: " + str(self.idTester))
        #return
        self.projectsList = self.listUserTestingProjects()
		
        for item in self.projectsList:
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(item['NameProyect'])
            
            if(int(item['TypeApp']) == 1):
                myQCustomQWidget.setTextDown('WEB')
                # Set the PATH or URL of this project
                myQCustomQWidget.setPath(str(item['UrlWeb']))
            elif(int(item['TypeApp']) == 2):
                myQCustomQWidget.setTextDown('DESKTOP')
                 # Set the PATH or URL of this project
                myQCustomQWidget.setPath(str(item['PathExe']))
            else:
                myQCustomQWidget.setTextDown('')
                # Set the PATH or URL of this project
                myQCustomQWidget.setPath(None)
                
            #myQCustomQWidget.setIcon('images/bot-image.png')
            myQCustomQWidget.setValue(item['IdTestGroup'])
            myQCustomQWidget.setType(int(item['TypeApp']))

			
            # Create QListWidgetItem
            myQListWidgetItem = QtWidgets.QListWidgetItem(self.lstWidgetProjects)
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            myQListWidgetItem.setSelected(False)
            # Add QListWidgetItem into QListWidget
            self.lstWidgetProjects.addItem(myQListWidgetItem)
            self.lstWidgetProjects.setItemWidget(myQListWidgetItem, myQCustomQWidget)
    
    def reloadProject(self):
        # Primero removemos todos los items de la lista
        self.lstWidgetProjects.clear()
        # Volvemos a cargar la lista con items
        self.loadProjects()
        
    
    def listUserTestingProjects(self):
        conn = ConnectionWS()
        conn.addParam(('token', self.token))
        conn.addParam(('idtester', self.idTester))
        conn.addParam(('func', ConnectionWS.PROJECTS_LIST))
        conn.generateUrl()
        
        print(conn.getUrl())
        conn.makeRequest()
		
        if(conn.response['status'] == 1):
            return conn.response['data']
        else:
            return []

    def itemClickedEvent(self, item):
        
        print("text", str(self.lstWidgetProjects.itemWidget(item).getText()))
        print("value", str(self.lstWidgetProjects.itemWidget(item).getValue()))
        print("row: ", str(self.lstWidgetProjects.row(item)))
		
        self.dlgProjectDetails = QtWidgets.QDialog()
        self.ui = ProjectDetailsUiController(self.dlgProjectDetails, str(self.lstWidgetProjects.itemWidget(item).getText()), self.dialogGeneralProjects)
        self.ui.setProjectId(int(self.lstWidgetProjects.itemWidget(item).getValue()))
        self.ui.setType(int(self.lstWidgetProjects.itemWidget(item).getType()))
        self.ui.setIdTester(self.idTester)
        self.ui.setToken(self.token)
        self.ui.setProjectPath(self.lstWidgetProjects.itemWidget(item).getPath())
        
        # Refresh labels from UI
        self.ui.RefreshDescriptionLabel()
        
        self.dlgProjectDetails.show()
		
        #print("flags", str(item.flags()))
        #self.msg = QtWidgets.QMessageBox()
        #self.msg.setIcon(QtWidgets.QMessageBox.Information)
        #self.msg.setText("This is a message box" + self.lstWidgetProjects.currentItem)
        #self.msg.setInformativeText("This is additional information")
        #self.msg.setWindowTitle("MessageBox demo")
        #self.msg.setDetailedText("The details are as follows:")
        #self.msg.open()
	
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = ProjectsUiController(dialog)
    dialog.show()
    sys.exit(app.exec_())
	
	
	
	