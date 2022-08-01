import time 
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = "397e47df3ec6469e9f6244f8453ed6c7"
service_url = "https://newsapi.org/v2/everything?"

# Ignore SSL certificate errors
checkCert = ssl.create_default_context()
checkCert.check_hostname = False
checkCert.verify_mode = ssl.CERT_NONE

searchStr= str(input("Enter search string: "))
urlParameters = dict()
urlParameters["q"]= searchStr
urlParameters['apiKey']=api_key 
url = service_url + urllib.parse.urlencode(urlParameters)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=checkCert)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None
retry=0
while retry<3:
    if (not js or 'status' not in js or js['status']!='ok') :
        time.sleep(2) 
        retry=retry+1
        uh = urllib.request.urlopen(url, context=checkCert)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')
        try:
            js = json.loads(data)
        except:
            js = None
        continue
    else: break 

if not js or 'status' not in js or js['status'] != 'ok':
    print('==== Failure To Retrieve ====')
else:
    print("Total results: ", js["totalResults"])
    responses=dict()
    #responses[i]=[name,author,title,description,url,urlToImage,publishedAt]
    if js["totalResults"]<5:
        noOfResults = int(js["totalResults"])
    else:
        noOfResults=5
    for i in range(noOfResults):
        responses[i]=[""]*7
        responses[i][0]=js["articles"][i]["source"]["name"]
        responses[i][1]=js["articles"][i]["author"]
        responses[i][2]=js["articles"][i]["title"]
        responses[i][3]=js["articles"][i]["description"]
        responses[i][4]=js["articles"][i]["url"]
        responses[i][5]=js["articles"][i]["urlToImage"]
        responses[i][6]=js["articles"][i]["publishedAt"]
    
for i in range(noOfResults):
    for k in range(7):
        print(responses[i][k])




