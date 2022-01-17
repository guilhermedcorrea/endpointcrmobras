from base64 import encode
from app import app, jsonify, db, api
from flask_restx import Resource
from app.controllers import converte_json
import json
import pandas as pd
from collections import Counter


@app.route('/api/v1/arquitetos/allarquitetos', methods=['GET','POST'])
def retorna_select_all_obras():
      jsons = converte_json.CrmObras()
      listas = []
      jsons_all_obras = jsons.retorna_all_cadastros()
      for js in jsons_all_obras:
            listas.append(js)

      return jsonify(listas)



                       
      
          
     
 



    

         

   


  

          
      


