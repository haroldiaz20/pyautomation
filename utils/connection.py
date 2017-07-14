import json

from urllib.error import HTTPError
from urllib.error import URLError
import urllib.parse
import urllib.request

from urllib.parse import quote

class ConnectionWS():
	
    wsUrl = "http://192.168.0.16/Testing/webservice/ws.php" #192.168.0.223
    userAgent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
    
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4
	
    #FUNCTIONS
    USER_LOGIN = 'user_login'
    PROJECTS_LIST = 'getTestGroup'
    GET_ACTION_GROUP = 'getActionGroup'
    GET_ACTION = 'getAction'	
    INI_REPORT = 'iniReport'
    SET_REPORT = 'setReport'
    SET_REPORT_DETAIL = 'setReportDetail'
    GET_COUNT_REPORT_ACTION = 'getCountReportAction'
    
    def __init__(self):
        self.url = self.wsUrl
        self.params = []
        self.jsonValues = None
        self.method = ConnectionWS.GET
		
    def generateUrl(self):
        if(len(self.params) > 0):
            self.url = self.url + '?'
			
        indice = 1
#        for name, value in self.params:
#            #value = quote(value)
#            if(indice == len(self.params)):
#                self.url = self.url + name + '=' + value
#            else:
#                self.url = self.url + name + '=' + value + '&'
#			
#            indice = indice + 1
	
        self.url = ""
        self.url = self.wsUrl + '?' + urllib.parse.urlencode(dict(self.params))
        print(self.url)
        # Print the JSON formated object of params (key, value). Se debe usar dir para
        # obtener la secuencia de  key, value de una tupla convertida en un map
        json_string = json.dumps(dict(self.params))
        self.jsonValues = json_string
		
    def getUrl(self):		
        # print(self.jsonValues)
        return self.url
	
    def setMethod(self, methodA):
        self.method = methodA
		
    def addParam(self, param):
        self.params.append(param)
		
    def makeRequest(self):
        try:

            if (self.method == ConnectionWS.POST):
                if(self.jsonValues is None):
                    self.req = urllib.request.Request(self.url, None)
                else:
                    data = urllib.parse.urlencode(self.jsonValues)
                    data = data.encode('ascii') # data should be bytes
                    self.req = urllib.request.Request(url, data)
					
            elif (self.method == ConnectionWS.POST):
                self.req = urllib.request.Request(self.url)
				
            elif (self.method == ConnectionWS.PUT):
                self.req = urllib.request.Request(self.url)
				
            else:
                self.req = urllib.request.Request(self.url)
			
            # Read JSON response from webservice
            with urllib.request.urlopen(self.req) as response:
                self.response = response.read()
            
            # Transform the response into a JSON properly format
            self.response = json.loads(self.response)
			
        except HTTPError as e:
            # do something
            print('Error code: ', e.code)
            mensaje = {"status": 0, "message": str(e.code), "data": None}
            self.response = mensaje
           
        except URLError as e:
            # do something
            print('Reason: ', e.reason)
            mensaje = {"status": 0, "message": str(e.reason), "data": None}
            self.response = mensaje
           
          
		
		

# ola = ConnectionWS()
# ola.addParam(('name', '343fdfg'))
# ola.addParam(('email', 'dsd'))
# ola.addParam(('asssail', 43434))
# ola.setMethod(ConnectionWS.GET)
# ola.generateUrl()
# ola.makeRequest()
# print("Message: %s" % (ola.response['status']))
# #print(ola.getUrl())
