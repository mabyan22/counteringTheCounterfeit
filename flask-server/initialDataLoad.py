from datetime import date 
import json
from backend import findResults
from os.path import exists 

listOfTopics=['Imran Khan','Pakistan today', 'Covid 2022', 'Pakistan Elections','Covid vaccine', 'Cricket world cup']
initialData=None
def returnResults():
    if exists(str(date.today())):
        fileHandle=open(str(date.today()),'r')
        compiledResults=fileHandle.read()
    else:
        fileHandle=open(str(date.today()),'w')
        initialData=findResults(listOfTopics)
        compiledResults=dict()
        compiledResults['articles']=list()
        for key in initialData:
            compiledResults['articles'].extend(initialData[key]['articles'][0:2])
        compiledResults=json.dumps(compiledResults)
        fileHandle.write(compiledResults)
    fileHandle.close()
    return compiledResults

