
#import pandas as pd;

import yaml
import json
import sys




def getYAMLFile(folderPath, fileName):
    f = open(folderPath + fileName)
    try:
        file = yaml.load(f, Loader=yaml.FullLoader);
    except yaml.YAMLError as exc:
        print(exc)
    f.close()
    return file
    
#print(json.dumps(file['paths'], indent=4))
    
#with open(folderPath + fileName) as f:
#    file = yaml.load(f, Loader=yaml.FullLoader);
#    print(json.dumps(file['paths'], indent=4))
    
    # for path in :
        # for k,v in path.items():
            # print(k, " -> ", v )
    
    # file = yaml.scan(f, Loader=yaml.FullLoader);
    # 
    # for token in file: 
        # print(token)





if __name__ == "__main__":
    folderPath = "c:\\Users\\sinanm\\Desktop\\OpenAPI\\"
    fileName = "openapi-sample.yaml"
    
    #read Yaml File
    dictYaml = getYAMLFile(folderPath, fileName)
    #print(dictYaml)
    
    # Get All the End Points
    dictEndPoints = dictYaml['paths']
    
    # foreach end point get the HTTP methods supported and the supported response codes
    for endPoint in dictEndPoints.keys():
        print(endPoint , "##" , dictEndPoints[endPoint])
    
    