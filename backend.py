import time 
import urllib.request, urllib.parse, urllib.error
import json
import ssl

apiKey = "397e47df3ec6469e9f6244f8453ed6c7"
serviceUrl = "https://newsapi.org/v2/everything?"

listOfItems = ["author","title","description","url","urlToImage","publishedAt"]

# Ignore SSL certificate errors
checkCert = ssl.create_default_context()
checkCert.check_hostname = False
checkCert.verify_mode = ssl.CERT_NONE

searchStr= str(input("Enter search string: "))
urlParameters = dict()
urlParameters["q"]= searchStr
urlParameters['apiKey']=apiKey 
url = serviceUrl + urllib.parse.urlencode(urlParameters)

print('Retrieving', url)
urlHandle = urllib.request.urlopen(url, context=checkCert)
data = urlHandle.read().decode()
print('Retrieved', len(data), 'characters')

try:
    jsDict = json.loads(data)
except:
    jsDict = None
retry=0
while retry<3:
    if (not jsDict or 'status' not in jsDict or jsDict['status']!='ok') :
        time.sleep(2) 
        retry=retry+1
        urlHandle = urllib.request.urlopen(url, context=checkCert)
        data = urlHandle.read().decode()
        print('Retrieved', len(data), 'characters')
        try:
            jsDict = json.loads(data)
        except:
            jsDict = None
        continue
    else: break 

if 'status' in jsDict and 'status' in jsDict and jsDict['status'] == 'ok':
    print("Total results: ", jsDict["totalResults"])
    responses=dict()
    #responses[i]=[name,author,title,description,url,urlToImage,publishedAt]
    if jsDict["totalResults"]<5:
        noOfResults = int(jsDict["totalResults"])
    else:
        noOfResults=5
    for i in range(noOfResults):
        for results in range(7):
            if results != 0 :
                for item in listOfItems:
                    print(listOfItems.index(item))
                    responses[i][(listOfItems.index(item))+1] = jsDict["articles"][i][item]
            else:
                responses[i]=[""]*7
                responses[i][0]=jsDict["articles"][i]["source"]["name"]
    for j in range(noOfResults):
        for k in range(7):
            print(responses[i][k])   
else:
    print('==== Failure To Retrieve ====')