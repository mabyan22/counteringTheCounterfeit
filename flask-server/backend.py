import time 
import urllib.request, urllib.parse, urllib.error
import json
import ssl

def findResults(listOfTopics):
    apiKey = "397e47df3ec6469e9f6244f8453ed6c7"
    serviceUrl = "https://newsapi.org/v2/everything?"
    listOfItems = ["author","title","description","url","urlToImage","publishedAt"]
    checkCert = ssl.create_default_context()
    checkCert.check_hostname = False
    checkCert.verify_mode = ssl.CERT_NONE
    urlParameters=dict()
    urlParameters['apiKey']=apiKey 
    topicsResponse = dict()
    for topic in listOfTopics:
        urlParameters["q"]=topic
        url = serviceUrl + urllib.parse.urlencode(urlParameters)
        urlHandle = urllib.request.urlopen(url, context=checkCert)
        data = urlHandle.read().decode()
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
                try:
                    jsDict = json.loads(data)
                except:
                    jsDict = None
                continue
            else: break 
        topicsResponse[topic]=jsDict
        

    return topicsResponse
     

def searchResults(query):
    # Ignore SSL certificate errors
    checkCert = ssl.create_default_context()
    checkCert.check_hostname = False
    checkCert.verify_mode = ssl.CERT_NONE

    apiKey = "397e47df3ec6469e9f6244f8453ed6c7"
    serviceUrl = "https://newsapi.org/v2/everything?"

    listOfItems = ["author","title","description","url","urlToImage","publishedAt"]

    searchStr= query
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
        responses['articles']=list()
        #responses[i]=[name,author,title,description,url,urlToImage,publishedAt]
        if jsDict["totalResults"]<10:
            noOfResults = int(jsDict["totalResults"])
        else:
            noOfResults=10
        for key in jsDict:
            responses['articles'].extend(jsDict['articles'][:noOfResults])
        return responses
    else:
        return "====Failure To Retrieve===="