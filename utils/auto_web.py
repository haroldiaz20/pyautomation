import inspect
import http.client
import socket
import time

import os


from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.command import Command

from utils.connection import ConnectionWS


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NotEditableElement(WebDriverException):
    """Exception raised for errors in the URL.

    Attributes:
        foundURL -- URL that is found at the moment the exception ocurred
        message -- explanation of the error
    """

    def __init__(self, msg):
        super(NotEditableElement, self).__init__(msg)
        
        
        
class NotMatchingURLError(Error):
    """Exception raised for errors in the URL.

    Attributes:
        foundURL -- URL that is found at the moment the exception ocurred
        message -- explanation of the error
    """

    def __init__(self, foundURL, message):
        self.foundURL = foundURL
        self.message = message


class AutoWeb():
	
    token = ''
    idtester = 0
    idtestgroup = 0
    url = ''
    
    idreport = 0
    
    EVENT_KEY = 1
    EVENT_CLICK = 2
    EVENT_LINK = 3
    EVENT_VALIDATE = 4
    EVENT_MOVE_FRAME = 5
    EVENT_VALIDATE_LINK = 6
    EVENT_DOUBLE_CLICK = 7
    
    
    REPORT_STATUS = {"executing": 1, "finished": 2, "error_starting": 3, "error_action": 4}
    
    REPORT_DETAIL_STATUS = {"error": 1, "success": 2}
    
    
    def __init__(self):
        self.token = ''
        self.idtester = 0
        self.idtestgroup = 0
        self.url = ''
        
        
        self.currentURL = ""
        self.lastURL = ""
        
        self.idReport = 0
        self.actionGroups = []
    
    
    # Get status of driver, in case the window has been closed
    def get_status(self, driver):
        try:
            driver.execute(Command.STATUS)
            return "Alive"
        except (socket.error, http.client.CannotSendRequest):
            return "Dead"
    
    def setInfo(self, token, idtester, idtestgroup, url):
        self.token = token
        self.idtester = idtester     
        self.idtestgroup = idtestgroup
        self.url = url
        
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
        
    def setReport(self, idreport, statusreport, totalitems, totalitemserror, totalitemssuccess, progress, information):
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
        
    def setReportDetail(self, idreport, idaction, status, information):
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


    def getAction(self, idactiongroup):
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
    
    def getProgress(self, t, e, s):
        if(int(t) == 0):
            return 100        
        if(int(t) < (int(e) + int(s))):
            return 100
        else:
            val = (int(e) + int(s)) / int(t) * 100
            return int(val)
        
        return 100
    
    def find_element_string(self, stringMultiple, driver):
        lista  = stringMultiple.strip().split('->')
        frame = driver
        for item in lista:
            variable  = item.strip().split('=')
            Ini = int(str(variable[1]).find('['))
            Fin = int(str(variable[1]).find(']'))
            if(variable[0].strip().lower() == 'id'):
                if(Ini != -1 & Fin != -1):
                    frame = frame.find_elements_by_id(variable[1][:Ini])[int(variable[1][Ini + 1:Fin])]
                else:
                    frame = frame.find_element_by_id(variable[1])
            if(variable[0].strip().lower() == 'name'):
                if(Ini != -1 & Fin != -1):
                    frame = frame.find_elements_by_name(variable[1][:Ini])[int(variable[1][Ini + 1:Fin])]
                else:               
                    frame = frame.find_element_by_name(variable[1])
            if(variable[0].strip().lower() == 'class'):
                if(Ini != -1 & Fin != -1):
                    frame = frame.find_elements_by_class_name(variable[1][:Ini])[int(variable[1][Ini + 1:Fin])]
                else:
                    frame = frame.find_element_by_class_name(variable[1])
           
        return frame
    
    
    def saveScreenshot(self, driver, itemAction, itemActionGroup):
        # Generate the image name
        imageName = str(itemActionGroup['IdActionGroup']) + "_" + str(itemAction['IdAction']) + "." + "jpg"
        # Obtain the path of the directory 
        ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images', 'screenshot'))
        # Check if path doesn't exists
        if not os.path.exists(ruta):
            os.makedirs(ruta)
        # Join the name with the full path where the will be saved
        ruta = os.path.join(ruta, imageName)
        # Save the screenshot using the driver
        driver.save_screenshot(ruta)
    
	
    def execAutoWeb(self, testplay):
        if int(testplay) == 2:
            print("This is a PLAY action, son MUST generate a report...")            
        self.idReport = self.iniReport()

        # Let's get all the action groups for this test
        self.actionGroups = self.getActionGroup()

        ######################### VARIABLES #################
        finalStatus = AutoWeb.REPORT_STATUS['executing']
        # total errors
        totalErrors = 0            
        # total success
        totalSuccess = 0
        #total Actions
        totalActions = int(self.getCountReportAction())
        progress = 0
        # input ID
        inputID = 0
        # action ID
        actionID = 0

        try:
            # Let's initialize once the driver
            #driver = webdriver.Chrome()
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            
            # Obtain the path of the directory 
            driverPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'webdrivers', 'chromedriver', 'chromedriver.exe'))
            print(driverPath)
            driver = webdriver.Chrome(driverPath, chrome_options=chrome_options)
			
            driver.get(self.url)
            driver.implicitly_wait(3) # seconds

            for itemactiongroup in self.actionGroups:                
                self.action = self.getAction(itemactiongroup['IdActionGroup'])                    

                for itemaction in self.action:
                    try:
                        self.currentURL = driver.current_url
                        inputID = itemaction['IdInput']
                        actionID = itemaction['IdAction']
                        elem = None

                        """
                        ######################## KEY EVENT ########################
                        """
                        if int(itemaction['TypeEvent']) == AutoWeb.EVENT_KEY:
                            # Let's find the element
                            if int(itemaction['TypeIdentifier']) == 1:
                                elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, inputID)))
                            elif int(itemaction['TypeIdentifier']) == 2:
                                elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, inputID)))
                            elif int(itemaction['TypeIdentifier']) == 3:
                                elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS, inputID)))
                            elif int(itemaction['TypeIdentifier']) == 4:
                                elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, inputID)))
                            elif int(itemaction['TypeIdentifier']) == 5:
                                elem = self.find_element_string(inputID, driver)                                           
                            
                            #################### SAVE SCREENSHOT ###################
                            self.saveScreenshot(driver, itemaction, itemactiongroup)
                            ########################################################

                            # Clear the text from input
                            elem.clear()
                            # Type this text into the input
                            elem.send_keys(itemaction['ValueInput'])
                            
                            """
                            ######################## CLICK EVENT ########################
                            """
                        elif int(itemaction['TypeEvent']) == AutoWeb.EVENT_CLICK:
                            if str(self.lastURL) != str(self.currentURL):
                                driver.refresh()

                            # Let's find the element
                            if int(itemaction['TypeIdentifier']) == 1:
                                elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, inputID)))
                            elif int(itemaction['TypeIdentifier']) == 2:
                                elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, inputID)))
                            elif int(itemaction['TypeIdentifier']) == 3:
                                elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS, inputID)))
                            elif int(itemaction['TypeIdentifier']) == 4:
                                elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, inputID)))                                    
                            elif int(itemaction['TypeIdentifier']) == 5:
                                elem = self.find_element_string(inputID, driver)
                            
                            #################### SAVE SCREENSHOT ###################
                            self.saveScreenshot(driver, itemaction, itemactiongroup)
                            ########################################################
                            
                            # Click this element
                            elem.click()                            
                            
                            """
                            ######################## VALIDATE EVENT ########################
                            """
                        elif int(itemaction['TypeEvent']) == AutoWeb.EVENT_VALIDATE:                                
                            validationType = itemaction['TypeValidate']
                            stringToBeFound = " "
                            identifierType = None
                            textFromElement = ""
                            
                            if int(validationType) == 1:
                                identifierType = itemaction['TypeIdentifierSuccess']
                                inputID = itemaction['IdInputSuccess']
                                stringToBeFound = str(itemaction['ValueInputSuccess']).lower()                                

                                # Let's find the element
                                if int(identifierType) == 1:
                                    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, inputID)))
                                elif int(identifierType) == 2:
                                    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, inputID)))
                                elif int(identifierType) == 3:
                                    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS, inputID)))
                                elif int(identifierType) == 4:
                                    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, inputID)))
                                elif int(identifierType) == 5:
                                    elem = self.find_element_string(inputID, driver)
                                
                                # Let's find the way how we're gonna get the text of the element (HTML, TEXT or NAME)
                                if int(itemaction['GetTextFrom']) == 1:
                                    textFromElement = str(elem.get_attribute('Name'))
                                elif int(itemaction['GetTextFrom']) == 2:                                    
                                    textFromElement = str(elem.get_attribute('innerHTML'))
                                elif int(itemaction['GetTextFrom']) == 3:
                                    textFromElement = str(elem.text())
                                else:
                                    pass

                                ## Validate if textFromElement contains stringToBeFound
                                if textFromElement.strip().lower().find(stringToBeFound) != -1:
                                    print("""1111111111111111111""")
                                    totalSuccess += 1
                                    if int(testplay) == 2:
                                        #  idreport, idaction, status, information
                                        self.updateReportDetail = self.setReportDetail(self.idReport, actionID, AutoWeb.REPORT_DETAIL_STATUS["success"], 'updated')
                                    
                                        # Get Progress
                                        progress = self.getProgress(totalActions, totalErrors, totalSuccess)
                                    
                                        # Update report
                                        self.updateReport = self.setReport(self.idReport, AutoWeb.REPORT_STATUS["executing"], totalActions, totalErrors, totalSuccess, progress, 'updated')

                                else:
                                    print("""22222222222222222""")
                                    totalErrors += 1
                                    if int(testplay) == 2:
                                        # idreport, idaction, status, information
                                        self.updateReportDetail = self.setReportDetail(self.idReport, actionID, AutoWeb.REPORT_DETAIL_STATUS["error"], 'This string could not be found :(')
                                        # Get Progress
                                        progress = self.getProgress(totalActions, totalErrors, totalSuccess)
                                        # Update report
                                        self.updateReport = self.setReport(self.idReport, AutoWeb.REPORT_STATUS["executing"], totalActions, totalErrors, totalSuccess, progress, 'updated')



                            elif int(validationType) == 2:
                                identifierType = itemaction['TypeIdentifierError']
                                inputID = itemaction['IdInputError']
                                stringToBeFound = str(itemaction['ValueInputError']).lower()

                                # Let's find the element
                                if int(identifierType) == 1:
                                    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, inputID)))
                                elif int(identifierType) == 2:
                                    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, inputID)))
                                elif int(identifierType) == 3:
                                    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS, inputID)))
                                elif int(identifierType) == 4:
                                    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, inputID)))
                                elif int(identifierType) == 5:
                                    elem = self.find_element_string(inputID, driver)
                                
                                # Let's find the way how we're gonna get the text of the element (HTML, TEXT or NAME)
                                if int(itemaction['GetTextFrom']) == 1:
                                    print(elem.get_attribute('Name'))
                                    textFromElement = str(elem.get_attribute('Name'))
                                elif int(itemaction['GetTextFrom']) == 2:                                    
                                    print("String found!! " + str(elem.get_attribute('innerHTML')))
                                    textFromElement = str(elem.get_attribute('innerHTML'))
                                elif int(itemaction['GetTextFrom']) == 3:
                                    print("String: " + str(elem.text()))
                                    textFromElement = str(elem.text())
                                else:
                                    pass                                  

                                ## Validate if textFromElement contains stringToBeFound
                                if textFromElement.strip().lower().find(stringToBeFound) != -1:
                                    print("""3333333333333333333""")
                                    totalErrors += 1
                                    if int(testplay) == 2:
                                        #  idreport, idaction, status, information
                                        self.updateReportDetail = self.setReportDetail(self.idReport, actionID, AutoWeb.REPORT_DETAIL_STATUS["error"], 'This string error was found :)')
                                        # Get Progress
                                        progress = self.getProgress(totalActions, totalErrors, totalSuccess)
                                        # Update report
                                        self.updateReport = self.setReport(self.idReport, AutoWeb.REPORT_STATUS["executing"], totalActions, totalErrors, totalSuccess, progress, 'updated')

                                else:
                                    print("""4444444444444444444""")
                                    totalErrors += 1
                                    
                                    if int(testplay) == 2:
                                        #  idreport, idaction, status, information
                                        self.updateReportDetail = self.setReportDetail(self.idReport, actionID, AutoWeb.REPORT_DETAIL_STATUS["error"], 'This string could not be found :(')
                                        # Get Progress
                                        progress = self.getProgress(totalActions, totalErrors, totalSuccess)
                                        # Update report
                                        self.updateReport = self.setReport(self.idReport, AutoWeb.REPORT_STATUS["executing"], totalActions, totalErrors, totalSuccess, progress, 'updated')

                            else:
                                pass


                        elif int(itemaction['TypeEvent']) == AutoWeb.EVENT_VALIDATE_LINK:
                            # Let's wait a moment for the page to load
                            url = ""
                            try:
                                elem = driver.find_element_by_id("")
                                url = driver.current_url                              

                            except NoSuchElementException as e:
                                print(e.msg)
                                url = driver.current_url
                            
                            #### Validate if the current URL is the same as the expected one
                            if str(itemaction['MoveLinkFrame']) == str(url):
                                """
                                IMPORTANT!!!! MAKE A REFRESH IN ORDER TO LOAD ALL ELEMENTS INTO DRIVER
                                """
                                driver.refresh()
                            else:
                                raise WebDriverException("""This URL does not match the expected URL.\nURL: %s""" % (url))
                            
                            """
                            ######################## DOUBLE CLICK EVENT ########################
                            """
                        elif int(itemaction['TypeEvent']) == AutoWeb.EVENT_DOUBLE_CLICK:
                            print("""GONNA PERFORM A DOUBLE CLICK ACTION""")
                            # Let's find the element
                            if int(itemaction['TypeIdentifier']) == 1:
                                elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, inputID)))
                            elif int(itemaction['TypeIdentifier']) == 2:
                                elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, inputID)))
                            elif int(itemaction['TypeIdentifier']) == 3:
                                elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS, inputID)))
                            elif int(itemaction['TypeIdentifier']) == 4:
                                elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, inputID)))                                   
                            elif int(itemaction['TypeIdentifier']) == 5:
                                elem = self.find_element_string(inputID, driver)

                            #Perform the double click event
                            # ONLY WORKS ON CHROME DRIVER
                            actionChains = ActionChains(driver)
                            actionChains.move_to_element(elem)
                            actionChains.double_click()
                            actionChains.perform()

                            print(itemaction)
                            print("PERFORMED")
                            time.sleep(2)

                        else:
                            pass


                        if int(itemaction['TypeEvent']) != AutoWeb.EVENT_VALIDATE:
                            totalSuccess += 1
                            if int(testplay) == 2:
                                #  idreport, idaction, status, information
                                self.updateReportDetail = self.setReportDetail(self.idReport, actionID, AutoWeb.REPORT_DETAIL_STATUS["success"], 'updated')
                                # Get Progress
                                progress = self.getProgress(totalActions, totalErrors, totalSuccess)
                                # Update report
                                self.updateReport = self.setReport(self.idReport, AutoWeb.REPORT_STATUS["executing"], totalActions, totalErrors, totalSuccess, progress, 'updated')

                            self.lastURL = driver.current_url                            
                        
                        ######################## END OF ACTION, MUST WAIT 1 SEC ######################
                        time.sleep(1)
                    
                    except NoSuchWindowException as e:
                        print(self.get_status(driver))
                        print("ActionError NoSuchWindowException: ", e.msg)
                    
                    except ElementNotInteractableException as e:
                        print("ActionError ElementNotInteractableException: ", e.msg) 
                        print(itemactiongroup, itemaction)
                        
                        if int(testplay) == 2:
                            #  idreport, idaction, status, information
                            self.updateReportDetail = self.setReportDetail(self.idReport, actionID, AutoWeb.REPORT_DETAIL_STATUS["error"], str(e.msg))

                            if int(self.updateReportDetail) > 0:
                                print("Se envio el detalle del reporte")
                            else:
                                print("No se envio ni michi... %s" % (e.msg))

                            totalErrors += 1 

                            # Get Progress
                            progress = self.getProgress(totalActions, totalErrors, totalSuccess)

                            # Update report
                            self.updateReport = self.setReport(self.idReport, AutoWeb.REPORT_STATUS["error_action"], totalActions, totalErrors, totalSuccess, progress, 'There was an error in the actions...')

                        time.sleep(2)
                    
                    
                    except NoSuchElementException as e:
                        print(self.get_status(driver))
                        print("ActionError NoSuchElementException: ", e.msg) 
                        print(itemactiongroup, itemaction)
                        
                        if int(testplay) == 2:
                            #  idreport, idaction, status, information
                            self.updateReportDetail = self.setReportDetail(self.idReport, actionID, AutoWeb.REPORT_DETAIL_STATUS["error"], str(e.msg))

                            if int(self.updateReportDetail) > 0:
                                print("Se envio el detalle del reporte")
                            else:
                                print("No se envio ni michi... %s" % (e.msg))

                            totalErrors += 1
                            # Get Progress
                            progress = self.getProgress(totalActions, totalErrors, totalSuccess)
                            # Update report
                            self.updateReport = self.setReport(self.idReport, AutoWeb.REPORT_STATUS["error_action"], totalActions, totalErrors, totalSuccess, progress, 'There was an error in the actions...')

                        time.sleep(2)

                    
                    except WebDriverException as e:
                        print(self.get_status(driver))
                        print("ActionError WebDriverException: ", e.msg) 
                        print(itemactiongroup, itemaction)    
                        
                        if int(testplay) == 2:
                            mensaje = "--"
                            if str(e.msg).strip() != '':
                                mensaje = e.msg

                            #  idreport, idaction, status, information
                            self.updateReportDetail = self.setReportDetail(self.idReport, actionID, AutoWeb.REPORT_DETAIL_STATUS["error"], mensaje)

                            if int(self.updateReportDetail) > 0:
                                print("Se envio el detalle del reporte")
                            else:
                                print("No se envio ni michi... %s" % (mensaje))

                            totalErrors += 1 

                            # Get Progress
                            progress = self.getProgress(totalActions, totalErrors, totalSuccess)
                            # Update report
                            self.updateReport = self.setReport(self.idReport, AutoWeb.REPORT_STATUS["error_action"], totalActions, totalErrors, totalSuccess, progress, 'There was an error in the actions...')

                        time.sleep(2)
                        
                    except BaseException as e:
                        print(self.get_status(driver))
                        print("ActionError BaseException: ", e.msg) 
                        print(itemactiongroup, itemaction)
                        
                        if int(testplay) == 2:
                            mensaje = "--"
                            if str(e.msg).strip() != '':
                                mensaje = e.msg

                            #  idreport, idaction, status, information
                            self.updateReportDetail = self.setReportDetail(self.idReport, actionID, AutoWeb.REPORT_DETAIL_STATUS["error"], mensaje)

                            if int(self.updateReportDetail) > 0:
                                print("Se envio el detalle del reporte")
                            else:
                                print("No se envio ni michi... %s" % (mensaje))

                            totalErrors += 1 

                            # Get Progress
                            progress = self.getProgress(totalActions, totalErrors, totalSuccess)

                            # Update report
                            self.updateReport = self.setReport(self.idReport, AutoWeb.REPORT_STATUS["error_action"], totalActions, totalErrors, totalSuccess, progress, 'There was an error in the actions...')

                        time.sleep(2)

            

            if int(testplay) == 2:                
                # Get Progress
                progress = self.getProgress(totalActions, totalErrors, totalSuccess)

                # check if there is any error
                if totalErrors > 0:
                    finalStatus = AutoWeb.REPORT_STATUS['error_action']
                else:
                    finalStatus = AutoWeb.REPORT_STATUS['finished']

                # idreport, statusreport, totalitems, totalitemserror, totalitemssuccess, progress, information
                self.updateReport = self.setReport(self.idReport, finalStatus, totalActions, totalErrors, totalSuccess, progress, 'Finished')

                if int(self.updateReport) == 1:
                    print("correcto!!!!!!!")
                else:
                    print("incorrecto!!!!!")


        except WebDriverException as e:
           
            
            print("ActionGroupErrror WebDriverException: ", e.msg)
            print(itemactiongroup)
            
            if int(testplay) == 2:
                # Update report
                mensaje = "--"
                if str(e.msg).strip() != '':
                    mensaje = e.msg

                # Get Progress
                progress = self.getProgress(totalActions, totalErrors, totalSuccess)

                finalStatus = AutoWeb.REPORT_STATUS['error_starting']

                self.updateReport = self.setReport(self.idReport, finalStatus, totalActions, totalErrors, totalSuccess, progress, mensaje)

                if int(self.updateReport) > 0:
                    print("Se envio el detalle del reporte WebDriverException")
                else:
                    print("No se envio ni michi  WebDriverException... %s" % (e.msg))


        except BaseException as e:                
            print("ActionGroupErrror WebDriverException: ", e.msg)
            print(itemactiongroup)
            
            if int(testplay) == 2:
                # Update report
                mensaje = "--"
                if str(e.msg).strip() != '':
                    mensaje = e.msg

                # Get Progress
                progress = self.getProgress(totalActions, totalErrors, totalSuccess)

                finalStatus = AutoWeb.REPORT_STATUS['error_starting']

                self.updateReport = self.setReport(self.idReport, finalStatus, totalActions, totalErrors, totalSuccess, progress, mensaje)

                if int(self.updateReport) > 0:
                    print("Se envio el detalle del reporte WebDriverException")
                else:
                    print("No se envio ni michi  WebDriverException... %s" % (e.msg))
