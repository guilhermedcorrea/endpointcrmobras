import json

from app import app, db, jsonify
from app.models import tabelas_crm

from marshmallow import Schema, fields

def all_select():
    
    litas = []
    all_valores = """EXEC FiltrarAllObras"""
   
    all_obras = db.engine.execute(all_valores).all()
    for al in all_obras:
        if all != None:
            litas.append(all)

    return litas
       



    

  
    
       
         
    


    


 
  





