import json

class Config:
    def getConfig(parameter):
        with open('config.json') as configFile:
            Configs = json.load(configFile)
        
        if parameter == "quickScanUrl":
            return Configs['urls'][0]['quickScanUrl']
        
        elif parameter == "quickScanUrl2":
            return Configs['urls'][0]['quickScanUrl2']
        
        elif parameter == "serviceStateUrl":
            return Configs['urls'][0]['serviceStateUrl']
        
        elif parameter == "hashLookupUrl":
            return Configs['urls'][0]['hashLookupUrl']
        
        elif parameter == "getApiKey":
            return Configs['hybridanalysis']['api-key']
        
        elif parameter == "headerAccept":
            return Configs['hybridanalysis']['header-accept']
        
        elif parameter == "userAgent":
            return Configs['hybridanalysis']['user-agent']
        
        elif parameter == "contentType":
            return Configs['hybridanalysis']['content-type']