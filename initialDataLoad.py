import datetime
from backend import findResults
listOfTopics=['Pakistan today', 'Covid 2022', 'Pakistan Elections','Covid vaccine', 'Imran Khan']
fileHandle=open(str(datetime.datetime.now()),'w')
initialData=findResults(listOfTopics)
for key in initialData:
    for detail in initialData[key]:
        try:
            fileHandle.write(detail+"\n")
        except:
            continue 
fileHandle.close()
