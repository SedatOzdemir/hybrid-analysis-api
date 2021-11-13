import json
from config import Config
from analyzer import Analyzer
    
if __name__ == "__main__":        
    
    # Sample usages
    
    Result = Analyzer.analyzeVirusTotal("http://site.planetanetbl.com.br/cadastro.php")
    #Result = Analyzer.analyzeURLScanIO("http://site.planetanetbl.com.br/cadastro.php")
    #Result = Analyzer.getAnalyzeResultbyId("618d2bdff2d8ad019c09cdf8")
    #Result = Analyzer.getAnalyzeResultbyHash("c9212dbfc737fcdd09eb3ae26a89209ede449d85d23f7ccd8b7ecb8ca8001813")
    #Result = Analyzer.getServiceStatus()
    print(Result)