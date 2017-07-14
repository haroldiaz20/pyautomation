from utils.connection import ConnectionWS
from selenium import webdriver
import os
import sys
from selenium.webdriver import ActionChains
import time
import datetime


class AutoDesktop():
	
    token = ''
    idtester = 0
    idtestgroup = 0
    path = ''
    
    idreport = 0    
    	
    def __init__(self):
        self.token = ''
        self.idtester = 0
        self.idtestgroup = 0
        self.path = ''
        
        self.idreport = 0
    
    def setInfo(self,token,idtester,idtestgroup,path):
        self.token = token
        self.idtester = idtester     
        self.idtestgroup = idtestgroup
        self.path = path
        
    def iniReport(self):
        #func=iniReport&idtester=1&idtestgroup=5&token=02cf02457229148726e35de23298791c
        conn = ConnectionWS()
        conn.addParam(('token', self.token))
        conn.addParam(('idtester', self.idtester))
        conn.addParam(('idtestgroup', self.idtestgroup))
        conn.addParam(('func', ConnectionWS.INI_REPORT))
        conn.generateUrl()
        conn.makeRequest()
        
        if(conn.response['status'] == 1):
            return conn.response['data']['IdReport']
        else:
            return 0
        
    def getCountReportAction(self):
        #func=getCountReportAction&idtester=1&idtestgroup=5&token=02cf02457229148726e35de23298791c
        conn = ConnectionWS()
        conn.addParam(('token', self.token))
        conn.addParam(('idtester', self.idtester))
        conn.addParam(('idtestgroup', self.idtestgroup))
        conn.addParam(('func', ConnectionWS.GET_COUNT_REPORT_ACTION))
        conn.generateUrl()
        conn.makeRequest()
        
        if(conn.response['status'] == 1):
            return conn.response['data'][0]['NumberAction']
        else:
            return 0    
        
    def setReport(self,idreport,statusreport,totalitems,totalitemserror,totalitemssuccess,progress,information):
        #func=setReport&idtester=1&idreport=2&token=02cf02457229148726e35de23298791c&statusreport=1&totalitems=2&totalitemserror=1&totalitemssuccess=1&progress=10
        conn = ConnectionWS()
        conn.addParam(('token', self.token))
        conn.addParam(('idtester', self.idtester))
        conn.addParam(('idreport', idreport))
        conn.addParam(('statusreport', statusreport))
        conn.addParam(('totalitems', totalitems))
        conn.addParam(('totalitemserror', totalitemserror))
        conn.addParam(('totalitemssuccess', totalitemssuccess))
        conn.addParam(('progress', progress))
        conn.addParam(('information', information))
        conn.addParam(('func', ConnectionWS.SET_REPORT))
        conn.generateUrl()
        conn.makeRequest()
         
        if(conn.response['status'] == 1):
            return 1
        else:
            return 0
        
    def setReportDetail(self,idreport,idaction,status,information):
        #func=setReportDetail&idtester=1&idreport=4&token=02c&idaction=1&status=5&information=hola
        conn = ConnectionWS()
        conn.addParam(('token', self.token))
        conn.addParam(('idtester', self.idtester))
        conn.addParam(('idreport', idreport))
        conn.addParam(('idaction', idaction))
        conn.addParam(('status', status))
        conn.addParam(('information', information))
        conn.addParam(('func', ConnectionWS.SET_REPORT_DETAIL))
        conn.generateUrl()
        conn.makeRequest()
        
        if(conn.response['status'] == 1):
            return 1
        else:
            return 0
        
        
        
    def getActionGroup(self):
        #func=getActionGroup&idtester=1&idtestgroup=5&token=02cf02457229148726e35de23298791c
        conn = ConnectionWS()
        conn.addParam(('token', self.token))
        conn.addParam(('idtester', self.idtester))
        conn.addParam(('idtestgroup', self.idtestgroup))
        conn.addParam(('func', ConnectionWS.GET_ACTION_GROUP))
        conn.generateUrl()
        conn.makeRequest()
        
        if(conn.response['status'] == 1):
            return conn.response['data']
        else:
            return []

    def getAction(self,idactiongroup):
        #func=getAction&idtester=1&idactiongroup=49&token=02cf02457229148726e35de23298791c
        conn = ConnectionWS()
        conn.addParam(('token', self.token))
        conn.addParam(('idtester', self.idtester))
        conn.addParam(('idactiongroup', idactiongroup))
        conn.addParam(('func', ConnectionWS.GET_ACTION))
        conn.generateUrl()
        conn.makeRequest()
        
        if(conn.response['status'] == 1):
            return conn.response['data']
        else:
            return []
        
    def getProgress(self,t,e,s):
        if(int(t)==0):
            return 100        
        if(int(t)<(int(e)+int(s) )):
            return 100
        else:
            val =  (int(e)+int(s))/int(t) * 100
            return int(val)
        
        return 100
    
    def saveFile(self,label):
        try:
            var = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " -> "+label.strip()
            print(var)
            ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
            ruta = os.path.join(ruta, 'log_desktop.txt')
            file = open(ruta, 'a')             
            file.write(var+"\n")
            file.close()
        except BaseException as e:
            print("Error save log "+ str(e))    
    
    
    def sleepElement(self,driver,intentos,tipo):
        
        if(tipo == 0):
            time.sleep(2)
            print("Espera -> No lee ni escribe dataharol" )
        else:        
            count=1
            #driver.implicitly_wait(1)
            while (intentos > count):
                try:
                    var = driver.find_element_by_id('fsdfs55hola')#
                    print("Espera -> lo encontro" )
                    count = intentos
                except BaseException as e:
                    print("Espera -> " + str(e))
                    if(str(e).lower().find('timed out')==-1):
                        count = intentos
                    else:
                        count = count + 1
        
        return 1
    
    def find_element_string(self,stringMultiple,driver):
        lista  = stringMultiple.strip().split('->')
        frame = driver
        for item in lista:
            variable  = item.strip().split('=')
            Ini = int(str(variable[1]).find('['))
            Fin = int(str(variable[1]).find(']'))
            if(variable[0].strip().lower() =='id'):
                if(Ini!=-1 & Fin!=-1):
                    frame = frame.find_elements_by_id(variable[1][:Ini])[int(variable[1][Ini+1:Fin])]
                else:
                    frame = frame.find_element_by_id(variable[1])
            if(variable[0].strip().lower() =='name'):
                if(Ini!=-1 & Fin!=-1):
                    frame = frame.find_elements_by_name(variable[1][:Ini])[int(variable[1][Ini+1:Fin])]
                else:               
                    frame = frame.find_element_by_name(variable[1])
            if(variable[0].strip().lower() =='class'):
                if(Ini!=-1 & Fin!=-1):
                    frame = frame.find_elements_by_class_name(variable[1][:Ini])[int(variable[1][Ini+1:Fin])]
                else:
                    frame = frame.find_element_by_class_name(variable[1])
           
        return frame
	
        
        
        
        
        
        
        
    def execAutoDesktop(self, testplay):
        ## tesplay : 1 = test , 2 = play
        
        #get elements , ini elements
        self.countaction = self.getCountReportAction()
        self.errors = 0
        self.success = 0
        
        ##cargar el reporte  y devuelve el id reporte   
        if(testplay==2):
            self.idreport = self.iniReport()
            
            
        ##actualiza el reporte devuelve 1 o 0
        if(testplay==2):
            self.updateReport = self.setReport(self.idreport,'1','0','0','0','0','update')
        
        try:
            driver = webdriver.Remote(
                command_executor='http://localhost:9999',
                desired_capabilities={
                    "debugConnectToRunningApp": 'false',
                    "app": r""+self.path+""
                }) 
            time.sleep(2)
            self.saveFile("Good ini : Driver ini correct!!")
        except BaseException as e:
            self.saveFile("Exception ini : " + str(e))
            if(testplay==2):
                self.updateReport = self.setReport(self.idreport,'3',self.countaction,'0','0','100',str(e))
     
          	
        frame = driver
        self.actiongroup = self.getActionGroup()
        for itemactiongroup in self.actiongroup:
            self.action = self.getAction(itemactiongroup['IdActionGroup'])
            for itemaction in self.action:
                try:
                    if(int(itemaction['TypeEvent'])==1): #KEY
                        if(int(itemaction['TypeIdentifier'])==1): #id
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                keyf = driver.find_element_by_id(itemaction['IdInput'])
                            else: #from the last
                                keyf = frame.find_element_by_id(itemaction['IdInput'])
                        if(int(itemaction['TypeIdentifier'])==2): #name
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                keyf = driver.find_element_by_name(itemaction['IdInput'])
                            else: #from the last
                                keyf = frame.find_element_by_name(itemaction['IdInput'])
                        if(int(itemaction['TypeIdentifier'])==3): #classname
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                keyf = driver.find_element_by_class_name(itemaction['IdInput'])
                            else: #from the last
                                keyf = frame.find_element_by_class_name(itemaction['IdInput'])
                        if(int(itemaction['TypeIdentifier'])==5): #multiple
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                keyf = self.find_element_string(itemaction['IdInput'],driver)
                            else: #from the last
                                keyf = self.find_element_string(itemaction['IdInput'],frame)
                        keyf.send_keys(itemaction['ValueInput'])
                        


                    if(int(itemaction['TypeEvent'])==2): #CLICK
                        if(int(itemaction['TypeIdentifier'])==1): #id
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                clickf = driver.find_element_by_id(itemaction['IdInput'])
                            else: #from the last
                                clickf = frame.find_element_by_id(itemaction['IdInput'])
                        if(int(itemaction['TypeIdentifier'])==2): #name
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                clickf = driver.find_element_by_name(itemaction['IdInput'])
                            else: #from the last
                                clickf = frame.find_element_by_name(itemaction['IdInput'])
                        if(int(itemaction['TypeIdentifier'])==3): #classname
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                clickf = driver.find_element_by_class_name(itemaction['IdInput'])
                            else: #from the last
                                clickf = frame.find_element_by_class_name(itemaction['IdInput'])
                        if(int(itemaction['TypeIdentifier'])==5): #multiple
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                clickf = self.find_element_string(itemaction['IdInput'],driver)
                            else: #from the last
                                clickf = self.find_element_string(itemaction['IdInput'],frame)
                        if(int(itemaction['UseOffSet'])==0): #No usa mover click
                            clickf.click()
                        else:
                            actions = ActionChains(driver)
                            actions.move_to_element_with_offset(clickf,int(itemaction['XOffSet']),int(itemaction['YOffSet']))
                            actions.click()
                            actions.perform()                            
                        self.sleepElement(clickf,5,int(itemaction['ReadOrSaveData']))
                        
                       

                    if(int(itemaction['TypeEvent'])==4): #VALIDATE
                        if(int(itemaction['TypeValidate'])==1): #success
                            if(int(itemaction['TypeIdentifierSuccess'])==1): #id
                                if(int(itemaction['MoveFrom'])==1): #from parent
                                    valif = driver.find_element_by_id(itemaction['IdInputSuccess'])
                                else: #from the last
                                    valif = frame.find_element_by_id(itemaction['IdInputSuccess'])
                            if(int(itemaction['TypeIdentifierSuccess'])==2): #name
                                if(int(itemaction['MoveFrom'])==1): #from parent
                                    valif = driver.find_element_by_name(itemaction['IdInputSuccess'])
                                else: #from the last
                                    valif = frame.find_element_by_name(itemaction['IdInputSuccess'])
                            if(int(itemaction['TypeIdentifierSuccess'])==3): #classname
                                if(int(itemaction['MoveFrom'])==1): #from parent
                                    valif = driver.find_element_by_class_name(itemaction['IdInputSuccess'])
                                else: #from the last
                                    valif = frame.find_element_by_class_name(itemaction['IdInputSuccess'])
                            if(int(itemaction['TypeIdentifierSuccess'])==5): #multiple
                                if(int(itemaction['MoveFrom'])==1): #from parent
                                    valif = self.find_element_string(itemaction['IdInputSuccess'],driver)
                                else: #from the last
                                    valif = self.find_element_string(itemaction['IdInputSuccess'],frame)
                            texto = ''
                            if(int(itemaction['GetTextFrom'])==1): #GetTextFrom :  1 = Name
                                texto = valif.get_attribute('Name')                               
                            if(int(itemaction['GetTextFrom'])==3): #GetTextFrom :  3 = Text
                                texto = valif.text
                            if(str(texto).lower().find(str(itemaction['ValueInputSuccess']).lower())!=-1): #existe
                                self.saveFile("Validate Success Exists: OrderExec = " + itemaction['OrderExec'] + " "+texto)
                                self.success = self.success + 1
                                if(testplay==2):
                                    self.updateReportDetail = self.setReportDetail(self.idreport,itemaction['IdAction'],'2','Update validate Success , The string exists')
                                    self.updateReport = self.setReport(self.idreport,'1',self.countaction,self.errors,self.success,str(self.getProgress(self.countaction,self.errors,self.success)),'update')
                            else:
                                self.saveFile("Validate Success No Exists: OrderExec = " + itemaction['OrderExec'] + " "+texto)
                                self.errors = self.errors + 1
                                if(testplay==2):
                                    self.updateReportDetail = self.setReportDetail(self.idreport,itemaction['IdAction'],'1','Update validate Success , The string NO exists')
                                    self.updateReport = self.setReport(self.idreport,'1',self.countaction,self.errors,self.success,str(self.getProgress(self.countaction,self.errors,self.success)),'update')
                            
                        if(int(itemaction['TypeValidate'])==2): #error
                            if(int(itemaction['TypeIdentifierError'])==1): #id
                                if(int(itemaction['MoveFrom'])==1): #from parent
                                    valif = driver.find_element_by_id(itemaction['IdInputError'])
                                else: #from the last
                                    valif = frame.find_element_by_id(itemaction['IdInputError'])
                            if(int(itemaction['TypeIdentifierError'])==2): #name
                                if(int(itemaction['MoveFrom'])==1): #from parent
                                    valif = driver.find_element_by_name(itemaction['IdInputError'])
                                else: #from the last
                                    valif = frame.find_element_by_name(itemaction['IdInputError'])
                            if(int(itemaction['TypeIdentifierError'])==3): #classname
                                if(int(itemaction['MoveFrom'])==1): #from parent
                                    valif = driver.find_element_by_class_name(itemaction['IdInputError'])
                                else: #from the last
                                    valif = frame.find_element_by_class_name(itemaction['IdInputError'])
                            if(int(itemaction['TypeIdentifierError'])==5): #multiple
                                if(int(itemaction['MoveFrom'])==1): #from parent
                                    valif = self.find_element_string(itemaction['IdInputError'],driver)
                                else: #from the last
                                    valif = self.find_element_string(itemaction['IdInputError'],frame)
                            texto = ''
                            if(int(itemaction['GetTextFrom'])==1): #GetTextFrom :  1 = Name
                                texto = valif.get_attribute('Name')                               
                            if(int(itemaction['GetTextFrom'])==3): #GetTextFrom :  3 = Text
                                texto = valif.text
                            if(str(texto).lower().find(str(itemaction['ValueInputError']).lower())==-1): # no existe
                                self.saveFile("Validate Error No Exits: OrderExec = " + itemaction['OrderExec']  + " "+texto)
                                self.success = self.success + 1
                                if(testplay==2):
                                    self.updateReportDetail = self.setReportDetail(self.idreport,itemaction['IdAction'],'2','Update validate Error , The string No exists')
                                    self.updateReport = self.setReport(self.idreport,'1',self.countaction,self.errors,self.success,str(self.getProgress(self.countaction,self.errors,self.success)),'update')
                            else:
                                self.saveFile("Validate Error Exists : OrderExec = " + itemaction['OrderExec'] + " "+texto)
                                self.errors = self.errors + 1
                                if(testplay==2):
                                    self.updateReportDetail = self.setReportDetail(self.idreport,itemaction['IdAction'],'1','Update validate Error , The string exists')
                                    self.updateReport = self.setReport(self.idreport,'1',self.countaction,self.errors,self.success,str(self.getProgress(self.countaction,self.errors,self.success)),'update')
                            
                       


                    if(int(itemaction['TypeEvent'])==5): #MOVE FRAME
                        if(int(itemaction['TypeIdentifier'])==1): #id
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                frame = driver.find_element_by_id(itemaction['IdInput'])
                            else: #from the last
                                frame = frame.find_element_by_id(itemaction['IdInput'])
                        if(int(itemaction['TypeIdentifier'])==2): #name
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                frame = driver.find_element_by_name(itemaction['IdInput'])
                            else: #from the last
                                frame = frame.find_element_by_name(itemaction['IdInput'])
                        if(int(itemaction['TypeIdentifier'])==3): #classname
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                frame = driver.find_element_by_class_name(itemaction['IdInput'])
                            else: #from the last
                                frame = frame.find_element_by_class_name(itemaction['IdInput'])
                        if(int(itemaction['TypeIdentifier'])==5): #multiple
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                frame = self.find_element_string(itemaction['IdInput'],driver)
                            else: #from the last
                                frame = self.find_element_string(itemaction['IdInput'],frame)
                        if(int(itemaction['TypeIdentifier'])==6): #parent init
                            frame = driver
                            


                    if(int(itemaction['TypeEvent'])==7): #DOUBLECLICK
                        if(int(itemaction['TypeIdentifier'])==1): #id
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                dclickf = driver.find_element_by_id(itemaction['IdInput'])
                            else: #from the last
                                dclickf = frame.find_element_by_id(itemaction['IdInput'])
                        if(int(itemaction['TypeIdentifier'])==2): #name
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                dclickf = driver.find_element_by_name(itemaction['IdInput'])
                            else: #from the last
                                dclickf = frame.find_element_by_name(itemaction['IdInput'])
                        if(int(itemaction['TypeIdentifier'])==3): #classname
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                dclickf = driver.find_element_by_class_name(itemaction['IdInput'])
                            else: #from the last
                                dclickf = frame.find_element_by_class_name(itemaction['IdInput'])
                        if(int(itemaction['TypeIdentifier'])==5): #multiple
                            if(int(itemaction['MoveFrom'])==1): #from parent
                                dclickf = self.find_element_string(itemaction['IdInput'],driver)
                            else: #from the last
                                dclickf = self.find_element_string(itemaction['IdInput'],frame)
                        if(int(itemaction['UseOffSet'])==0): #No usa mover click
                            actions = ActionChains(driver)
                            actions.move_to_element(dclickf)
                            actions.double_click()
                            actions.perform()
                        else:
                            actions = ActionChains(driver)
                            actions.move_to_element_with_offset(dclickf,int(itemaction['XOffSet']),int(itemaction['YOffSet']))
                            actions.double_click()
                            actions.perform()                            
                        self.sleepElement(dclickf,5,int(itemaction['ReadOrSaveData']))
                        

                                
                    if(int(itemaction['TypeEvent'])!=4): #Diferente a validate
                        self.saveFile("Good Event : OrderExec = " + itemaction['OrderExec'])
                        self.success = self.success + 1
                        if(testplay==2):
                            self.updateReportDetail = self.setReportDetail(self.idreport,itemaction['IdAction'],'2','Update')
                            self.updateReport = self.setReport(self.idreport,'1',self.countaction,self.errors,self.success,str(self.getProgress(self.countaction,self.errors,self.success)),'update')
                            
                except BaseException as e:
                    self.saveFile("Exeption Event : OrderExec = " + itemaction['OrderExec']+" "+str(e))
                    self.errors = self.errors + 1
                    if(testplay==2):
                        self.updateReportDetail = self.setReportDetail(self.idreport,itemaction['IdAction'],'1',str(e))
                        self.updateReport = self.setReport(self.idreport,'1',self.countaction,self.errors,self.success,str(self.getProgress(self.countaction,self.errors,self.success)),'update')
            time.sleep(1)
                        
        #driver.close()
        # 2 succes o 4 error update final
        statusFinal = '2'
        if(self.errors>0):
            statusFinal = '4'
			
        if(testplay==2):  
            self.updateReport = self.setReport(self.idreport,statusFinal,self.countaction,self.errors,self.success,'100','update')
		
        
                    
                    
        
        
        