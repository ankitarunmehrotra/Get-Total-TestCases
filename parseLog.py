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



   
if __name__ == "__main__":
    #baseDirectoryPath="C:\\Users\\sinanm\\Desktop\\logs\\"
    baseDirectoryPath="./sampleFiles/"
    fileName = "sample-calls.txt"
    #fileName = "sas-planning.txt"
    
    fileHandler = open(baseDirectoryPath + fileName)
    allLines = fileHandler.readlines()
    fileHandler.close()
    urlRegex = [ 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 
                 '/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+']
    for line in allLines:
        #print(line + "\n")
        jsonLine = json.loads(line)
        #print( jsonLine["level"] + "\t" + jsonLine["timeStamp"] + "\t" + jsonLine["message"] + "\t" + jsonLine["source"] + "\t" + jsonLine["properties"]["__session"] + "\t" + jsonLine["properties"]["username"])
        listOfURLs = getURLsFromString(urlRegex, jsonLine["message"])                      
        #print(jsonLine["message"] + "\t : " + str(listOfURLs) )
        print( jsonLine["level"] + "\t" + jsonLine["timeStamp"] + "\t" + str(listOfURLs) + "\t" + jsonLine["source"] + "\t" + jsonLine["properties"]["__session"] + "\t" + jsonLine["properties"]["username"])
    