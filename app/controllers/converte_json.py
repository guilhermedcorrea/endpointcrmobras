import json
from app import app, db, jsonify
from app.models import tabelas_crm
from marshmallow import Schema, fields
from itertools import zip_longest
from app.models import consultas_db
import json
from app.controllers import consultas_tipos_obras

class CrmObras():

    def select_columns(self, iduni, pg, rows):
        query = """EXEC Paginacaocrm @IdUnidade = {},@PageNumber = {}, @RowsOfPage= {}""".format(iduni, pg, rows)

        results = db.engine.execute(query).keys()
        colunas = [colunas for colunas in results]
        return colunas

    def retorna_all_cadastros(self, iduni, pg, rows):
   
        valuesquery = """EXEC Paginacaocrm @IdUnidade = {}, @PageNumber = {}, @RowsOfPage= {}""".format(iduni, pg, rows)
        # query = consultas_db.paginacao_crm_prospecao(iduni,pg, rows)
        dict_items = []


        # values = db.engine.execute(all_valores).all()

        colunas = self.select_columns(iduni, pg, rows)
        results = db.session.execute(valuesquery).all()
        
        try:
            for result in results:
                cont = len(result)
                desc = {}
                try:
                    
                    for i in range(cont):
                        desc[colunas[i]] = result[i]
                   
                except Exception as e:
                    print(e)
                
                dict_items.append(desc)
        except Exception as e:
            print(e)

        return dict_items

class FasesLead():
    def select_colunas_fases(self, idfase, pg, rows):
        query = """ EXEC LeadIdUnidadeObrasCrm @idfase={}, @PageNumber ={}, @RowsOfPage={}""".format(idfase, pg, rows)
        results = db.session.execute(query).keys()
        colunas = [colunas for colunas in results]

        return colunas


    def retorna_all_fases(self, idfase, pg, rows):

        dict_items = []
        valuesquery = """ EXEC LeadIdUnidadeObrasCrm @idfase={}, @PageNumber ={}, @RowsOfPage={}""".format(idfase, pg,
                                                                                                          rows)
        colunas = self.select_colunas_fases(idfase, pg, rows)

        results = db.session.execute(valuesquery).all()
        
        try:
            for result in results:
                cont = len(result)
                desc = {}
                try:
                    for i in range(cont):
                        
                        desc[colunas[i]] = result[i]
                       
                except Exception as e:
                    print(e)
                dict_items.append(desc)
        except Exception as e:
            print(e)

        return dict_items



        

    
    

        
            


        
     

           
            
        

       





















