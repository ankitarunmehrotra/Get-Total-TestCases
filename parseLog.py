import pandas as pd
import json
import re






def getURLsFromString(urlRegex, message):
    listOfURLs = []
    for exp in urlRegex:
        urls = re.findall(exp, message)
        if(urls.__len__() != 0 ):
            for url in urls:
                if (listOfURLs.__len__() == 0 ):
                    listOfURLs.append(url)
                else:
                    matching = [s for s in listOfURLs if url in s]
                    if(matching.__len__() == 0):
                        listOfURLs.append(url)
    return listOfURLs;


def displayValuesOfInterest(jsonObject, extractionFields, stringObject):
    printBuffer = ""
    for field in extractionFields:
        stringField = str(field)
        fieldList = stringField.split('.')
        # if(len(fieldList) > 0):
            # for item in fieldList:
        if (len(fieldList) == 1):
            if field in jsonObject:
                printBuffer += (jsonObject[field] + ",")
        elif((fieldList[0] in jsonObject) and (fieldList[1] in jsonObject[fieldList[0]])):
            printBuffer += (jsonObject[fieldList[0]][fieldList[1]] + ",")
        else:
            printBuffer += (",")
    
    if(len(stringObject) != 0 ):
       printBuffer += (stringObject)
    
    return(printBuffer + "\n")
   
   
if __name__ == "__main__":
    baseDirectoryPath="./sampleFiles/"
    #fileName = "sample-calls.txt"
    fileName = "sas-planning.txt"
    printBuffer = ""
    extractionFields = [
        'level', 'timeStamp', 'source','properties.__session', 'properties.username'
    ]
    
    fileHandler = open(baseDirectoryPath + fileName)
    allLines = fileHandler.readlines()
    fileHandler.close()
    urlRegex = [ 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 
                 '/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+']

    for line in allLines:
        jsonLine = json.loads(line)
        listOfURLs = getURLsFromString(urlRegex, jsonLine["message"])                      
    #    print( jsonLine["level"] + "\t" + jsonLine["timeStamp"] + "\t" + str(listOfURLs) + "\t" + jsonLine["source"] + "\t" + jsonLine["properties"]["__session"] + "\t" + jsonLine["properties"]["username"])
        
        printBuffer += displayValuesOfInterest(jsonLine, extractionFields, str(listOfURLs))
    
    print(printBuffer)