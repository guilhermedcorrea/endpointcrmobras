from base64 import encode
from app import app, jsonify
from app.controllers import converte_json
from app.models import tabelas_crm
import json
import pandas as pd

@app.route("/api/v1/arquitetos/allcadastros", methods = ["GET","POST"])
def all_obras():
   ajustes = []
   jsons = tabelas_crm.all_select()
   df = pd.DataFrame(jsons)
   js = df.to_json(orient = 'index', force_ascii=False)
   return js
   

@app.route("/api/v1/arquitetos/idobra/<int:idobra>", methods = ["GET",])
def retorna_id_obra(idobra):
   pass
       
       
    
       

    

         

   


  

          
      


