import json
from app import app, db, jsonify
from app.models import tabelas_crm
from marshmallow import Schema, fields
from itertools  import zip_longest


class CrmObras():
	
    	
	def select_columns(self,iduni,idcol):
			query = """SelectInfosCrm @identunid = {} @IdColab =NULL""".format(iduni)
			results = db.engine.execute(consu).keys()
			colunas = [colunas for colunas in results]
			return colunas


	def retorna_all_cadastros(self, iduni, idcol=None):
			query = """SelectInfosCrm @identunid = {} @IdColab =NULL""".format(iduni)
			listas_dict = []
			columns  = CrmObras()
			all_valores = consu

			#values = db.engine.execute(all_valores).all()
			values = db.session.execute(all_valores).all()
		
			keys = columns.select_columns(iduni,idcol=None)
			for k, v in zip_longest(keys, values):
					for val in values:
						desc = {}
						
						valor = len(val)
						key = len(keys)
						if valor == key:
								try:
									dict_from_list = dict(zip(keys, val))
									desc.update(dict_from_list)
									listas_dict.append(dict_from_list)
								except IndexError as e:
									Error="NotFound"

			return listas_dict              
		
		
         



    


 
  





