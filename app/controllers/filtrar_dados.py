import re
import pandas as pd
import json

class Filtrar_dados:
      
    def selecao_obras(self,elementos):
        if re.search("Jurifica", elementos):

            print(elementos)
        
    def jsons_obras(self, elementos):
        df = pd.json_normalize(elementos)
       
        
        
    
            
           
     
       
  