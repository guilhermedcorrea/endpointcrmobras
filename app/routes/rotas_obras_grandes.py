from base64 import encode
from app import app, jsonify, abort,cross_origin, request
from app.controllers import converte_json, exceptions
from app.controllers.filtrar_dados import Filtrar_dados
from app.models import consultas_db
import json
import pandas as pd
from collections import Counter
from app.controllers import consultas_tipos_obras



#Verificar regra tamanho obra
#Retorna Informações Obras
@app.route('/api/v1/crmobrasgrandes/CrmProspecaoPaginado/<int:iduni>/<int:pg>/<int:rows>', methods=['GET','POST'])
@cross_origin()
def prospecao(iduni,pg, rows,idcol=None):
    try:
        jsons = converte_json.CrmObras()
        jsons_all_obras = jsons.retorna_all_cadastros(iduni,pg, rows)
        return jsonify(jsons_all_obras),201
    except:
        return jsonify({"Valor":"Não localizado"},404)

#Retorna Fases
@app.route("/api/v1/CrmobrasgrandesPaginado/lixeira/<int:idFase>/<int:idUnidade>/<int:PageNumber>/<int:RowspPage>", methods=['GET','POST'])
@app.route("/api/v1/CrmobrasgrandesPaginado/sucesso/<int:tipo>/<int:idUnidade>/<int:PageNumber>/<int:RowspPage>", methods=['GET','POST'])
@app.route("/api/v1/CrmobrasgrandesPaginado/visita/<int:tipo>/<int:idUnidade>/<int:PageNumber>/<int:RowspPage>", methods=['GET','POST'])
@app.route("/api/v1/CrmobrasgrandesPaginado/interagindo/<int:tipo>/<int:idUnidade>/<int:PageNumber>/<int:RowspPage>", methods=['GET','POST'])
@app.route("/api/v1/CrmobrasgrandesPaginado/fases/<int:tipo>/<int:idUnidade>/<int:PageNumber>/<int:RowspPage>", methods=['GET','POST'])
@cross_origin()
def fases(idUnidade,PageNumber,RowspPage,idFase):
    print(idUnidade,PageNumber,RowspPage,idFase)
    try:
        values = consultas_tipos_obras.select_lead_fase_crm_obras(idUnidade,PageNumber,RowspPage,idFase)
        print(values)
        return jsonify(values),201
    
    except:
        return jsonify({"Valor":"Não encontrado"},404)



#Filtros Obras/Tipos Obras
@app.route("/api/v1/CrmobrasgrandesPaginado/categoriaobra/<string:tipo>/<int:idUnidade>/<int:PageNumber>/<int:RowspPage>", methods=['GET','POST'])
@cross_origin()
def selecao_tipo_obra_filtro(tipo, idUnidade, PageNumber, RowspPage):
    values = consultas_tipos_obras.select_query_filtro_crm_obrasgrandes(tipo,idUnidade,PageNumber, RowspPage)
  
    return jsonify(values)






