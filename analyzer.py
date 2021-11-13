import urllib.parse
import requests
from requests.structures import CaseInsensitiveDict
from config import Config

headers = CaseInsensitiveDict()
headers["accept"] = Config.getConfig("headerAccept")
headers["user-agent"] = Config.getConfig("userAgent")
headers["api-key"] = Config.getConfig("getApiKey")
headers["Content-Type"] = Config.getConfig("contentType")

class Analyzer:
    def analyzeVirusTotal(urlAddress):
        quickScanUrl2 = Config.getConfig("quickScanUrl2")
        encodedUrl = urllib.parse.quote(urlAddress)
        Data = "scan_type=lookup_virustotal&url="+encodedUrl+"&no_share_third_party=true&allow_community_access=false"
        Response = requests.post(quickScanUrl2, headers=headers, data=Data)
        return str(Response.text)

    def analyzeURLScanIO(urlAddress):
        quickScanUrl2 = Config.getConfig("quickScanUrl2")
        encodedUrl = urllib.parse.quote(urlAddress)
        Data = "scan_type=scan_urlscanio&url="+encodedUrl+"&no_share_third_party=true&allow_community_access=false"
        Response = requests.post(quickScanUrl2, headers=headers, data=Data)
        return str(Response.text)

    def getAnalyzeResultbyHash(sha256):
        hashLookupUrl = Config.getConfig("hashLookupUrl")
        Data = "hash=" + sha256
        Response = requests.post(hashLookupUrl, headers=headers, data=Data)
        return str(Response.text)

    def getAnalyzeResultbyId(analyzeId):
        quickScanUrl = Config.getConfig("quickScanUrl")
        Response = requests.get(quickScanUrl + analyzeId, headers=headers)
        return str(Response.text)

    def getServiceStatus():
        serviceStateUrl = Config.getConfig("serviceStateUrl")
        Response = requests.get(serviceStateUrl, headers=headers)
        return str(Response.text)