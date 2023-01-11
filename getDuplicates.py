import getopt, sys
import pathlib
import pandas as pd
import json

def usage():
    print("getDuplicates.py --options")
    print("-k, --key          get duplicates by key")
    print("-v, --value          get duplicates by value")
    

def processArguments(args):
    #print("args: ", args)
    byKey = byValue = False
    base = ""
    options, arguments = getopt.getopt(
        args,                      # Arguments
        "k v b:h:",                  # Short option definitions
        ["key ", "value ", "base =", "help "]) # Long option definitions
    #print("options: " , options)
    for o, a in options:
        
        if o in ("-k", "--key"):
            byKey = True             
        elif o in ("-h", "--help"):
            print(usage())
            sys.exit()
        elif o in ("-v", "--value"):
            byValue = True
        elif o in ("-b", "--base"):
            base = a
        else:
            usage()
            sys.exit(0)

    return byKey, byValue,base

def findAllI18NFiles(baseDirectoryPath,fileNameRegex):
    linkToBaseDirectory = pathlib.Path(baseDirectoryPath)
    files = list(linkToBaseDirectory.rglob(fileNameRegex))
    
    return files

def addKeyValuesToDictionary(globalI18NDictionary , fileToProcess,commentIdentifier ):
    records = pd.read_csv(fileToProcess, sep="=", header=None)
    dictionaryOfRecords = records.to_dict(orient="records")
    #print("\ndictionaryOfRecords: \n", dictionaryOfRecords  )
   
    for everyRecord in dictionaryOfRecords:
        #print("\neveryRecord: ", )        
        
        if(not everyRecord[0].strip().startswith(commentIdentifier)) :            
            if(globalI18NDictionary.get(everyRecord[1])) : 
                ##print("Key : " , everyRecord[1])
                fileNameList = globalI18NDictionary.get(everyRecord[1])
                fileNameList.append(str(fileToProcess))
            else:
                fileNameList = []
                fileNameList.append(str(fileToProcess))
                globalI18NDictionary[everyRecord[1]] = fileNameList
            
   
    return globalI18NDictionary 

def displayDuplicateEntries(globalI18NDictionary):
    
    for item in globalI18NDictionary.items():
        everyKey = item[0]
        everyValue = item[1] 
        if(len(everyValue) > 1):
            #print(everyKey , " : ", everyValue)
            print(json.dumps( item , indent= 4))
    
    
   
if __name__ == "__main__":
    
    byKey, byValue, baseDirectoryPath = processArguments(sys.argv[1:])
    print("byKey, byValue, baseDirectoryPath", byKey, byValue, baseDirectoryPath) 
    #sys.exit(0)
    if(byKey & byValue):
        usage()
        sys.exit(0)
    #print ("\nbyKey: ", byKey, "\t byValue: ", byValue)
    #baseDirectoryPath="C:\\Users\\sinanm\\Desktop\\Find Keys\\"
    fileNameRegex= "messagebundle.properties"
    commentIdentifier = "#"
    # Find All messagesFile Locations
    files = findAllI18NFiles(baseDirectoryPath, fileNameRegex)
    
    globalI18NDictionary = {}
    #For each file add the keys/values and the filename to a dictionary  
    for f in files:
        print( "Name: ", f)
        
        #Process each file 
        globalI18NDictionary = addKeyValuesToDictionary(globalI18NDictionary, f,commentIdentifier)
    
    #print(json.dumps( globalI18NDictionary, indent=4))    
    
    displayDuplicateEntries(globalI18NDictionary)
        
        
    