import json

from app import app, db, jsonify
from app.models import tabelas_crm
from marshmallow import Schema, fields
from itertools  import zip_longest

consu = """

			
	SELECT 
			ARQT.[IdArquiteto]
				,ARQT.[NomeArquiteto]
				,ARQT.[Email]
				,ARQT.[Telefone]
				,ARQT.[Idade]
				,ARQT.[Logradouro]
				,ARQT.[Numero]
				,ARQT.[Complemento]
				,ARQT.[Bairro]
				,ARQT.[Cep]
				,ARQT.[IdCidade]
				,ARQT.[Cidade]
				,ARQT.[Uf]
				,ARQT.[RazaoSocial]
				,ARQT.[TipoVinculo]
				,ARQT.[UfEscritorio]
				,ARQT.[bitAtivo]
				,ARQT.[DataInserido]
				,OB.[IdObra]
				,OB.[ArquitetoId]
				,OB.[NomeObra]
				,OB.[Uf]
				,OB.[IdCidade]
				,OB.[Cidade]
				,OB.[TipoObra]
				,OB.[PrevisaoTermino]
				,OB.[GrupoAtividadeProfissional]
				,OB.[TipoLogradouro]
				,OB.[Logradouro]
				,OB.[Numero]
				,OB.[Complemento]
				,OB.[Bairro]
				,OB.[Bairro]
				,OB.[Cep]
				,OB.[Grupo]
				,OB.[GrupoTamanhoObra]
				,ARO.[IdArqObra]
				,ARO.[ArquitetoId]
				,ARO.[IdObra]
				,ARO.[QuantidadeObrasRegiao]
				,ARO.[QuantidadeObrasProfissional]
				,ARO.[GrupoQuantidadeObras]
				,ARO.[GrupoQuantidadeMetrosObras]
				,ARO.[GrupoMeses]
				,ARO.[Nome]
				,ARO.[Meses]
				,CIT.Capital
				,CIT.IdEstado
				,CIT.Latitude
				,CIT.Longitude
				,CIT.Nome
				,UNI.[IdUnidade]
				,UNI.[IdCidade]
				,UNI.[IdUnidade]
				,UNI.[UF]
			FROM [HauszMapa].[Crm].[Arquiteto] AS ARQT
			JOIN [Crm].[ArquitetoObras] AS ARO
			ON ARO.ArquitetoId = ARQT.IdArquiteto
			JOIN [Crm].[Obra] AS OB
			ON OB.ArquitetoId = ARQT.IdArquiteto
			JOIN [Cadastro].[Cidade] AS CIT
			ON CIT.IdCidade = ARQT.IdCidade
			JOIN [Cadastro].[Unidade] AS UNI
			ON UNI.IdCidade = ARQT.IdCidade
			WHERE ISNUMERIC(UNI.IdUnidade) = 1  AND CIT.IdCidade = UNI.IdCidade AND OB.Uf = UNI.UF
			ORDER BY IdArquiteto
			

	"""

    
  
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
		
		
         



    


 
  





