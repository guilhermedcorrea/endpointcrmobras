from base64 import encode
from app import app, jsonify
from flask_restx import Resource
from app.controllers import converte_json
import json
import pandas as pd
from collections import Counter



@app.route('/api/v1/arquitetos/<int:iduni>', methods=['GET','POST'])
def teste_endpoint(iduni,idcol=None):
    jsons = converte_json.CrmObras()
    listas = []
    jsons_all_obras = jsons.retorna_all_cadastros(iduni)
    for js in jsons_all_obras:
        listas.append(js)

    return jsonify(listas)
	