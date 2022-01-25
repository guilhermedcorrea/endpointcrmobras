from app import db

keys = ['IdObra', 'CpfCnpjContratante', 'Contratante',
        'Telefone', 'Email', 'TipoPessoa', 'Endereco', 'Complemento',
        'Bairro', 'IdCidade', 'Cidade', 'Estado', 'Cep', 'Latitude',
        'Longitude', 'TipoObra', 'IdCategoria', 'IdAtividade', 'DataCadastro',
        'TamanhoObra', 'IdArquiteto', 'NomeArquiteto', 'TelefoneArquiteto',
        'DataInserido', 'bitAtivo', 'NumeroRRT', 'IdObra', 'CpfCnpjContratante',
        'Contratante', 'Telefone', 'Email', 'TipoPessoa', 'Endereco', 'Complemento',
        'Bairro', 'IdCidade', 'Cidade', 'Estado', 'Cep', 'Latitude', 'Longitude',
        'TipoObra', 'IdCategoria', 'IdAtividade', 'DataCadastro', 'TamanhoObra',
        'IdArquiteto', 'NomeArquiteto', 'TelefoneArquiteto',
        'DataInserido', 'bitAtivo', 'NumeroRRT', 'IdLeadObra', 'IdObra',
        'IdUnidade', 'IdColaborador', 'IdFase', 'DataInserido', 'bitAtivo', 'DataAgenda']


def select_lead_fase_crm_obras(idUnidade, PageNumber, RowspPage, idFase):
    print(idUnidade, idFase, PageNumber, RowspPage)
    query_fase = """
         DECLARE @idunidade AS INT
        DECLARE @PageNumber AS INT
        DECLARE @RowsOfPage AS INT
		DECLARE @idfaselead AS INT

        SET @idunidade = {}
        SET @PageNumber = {}
        SET @RowsOfPage = {}
		SET @idfaselead = {}


        SELECT 
                OBS.[IdObra],OBS.[CpfCnpjContratante],OBS.[Contratante],OBS.[Telefone],OBS.[Email],OBS.[TipoPessoa]
                ,OBS.[Endereco],OBS.[Complemento],OBS.[Bairro],OBS.[IdCidade],OBS.[Cidade],OBS.[Estado],OBS.[Cep]
                ,OBS.[Latitude],OBS.[Longitude],OBS.[TipoObra],OBS.[IdCategoria],OBS.[IdAtividade],OBS.[DataCadastro],OBS.[TamanhoObra]
                ,OBS.[IdArquiteto],OBS.[NomeArquiteto],OBS.[TelefoneArquiteto],OBS.[DataInserido],OBS.[bitAtivo],OBS.[NumeroRRT]
                ,OBR.[IdObra],OBR.[CpfCnpjContratante],OBR.[Contratante],OBR.[Telefone],OBR.[Email],OBR.[TipoPessoa],OBR.[Endereco],OBR.[Complemento]
                ,OBR.[Bairro],OBR.[IdCidade],OBR.[Cidade],OBR.[Estado],OBR.[Cep],OBR.[Latitude],OBR.[Longitude],OBR.[TipoObra]
                ,OBR.[IdCategoria],OBR.[IdAtividade],OBR.[DataCadastro],OBR.[TamanhoObra],OBR.[IdArquiteto]
                ,OBR.[NomeArquiteto],OBR.[TelefoneArquiteto],OBR.[DataInserido],OBR.[bitAtivo],OBR.[NumeroRRT],LOBRA.[IdLeadObra]
                ,LOBRA.[IdObra],LOBRA.[IdUnidade],LOBRA.[IdColaborador],LOBRA.[IdFase],LOBRA.[DataInserido],LOBRA.[bitAtivo]
                ,LOBRA.[DataAgenda]
        FROM 	
            [HauszMapa].[Crm].[ObRaS] AS OBS
                JOIN [Crm].[ObRaS] AS OBR
                ON OBR.IdObra = OBS.IdObra
                JOIN [HauszMapa].[Crm].[LeadObra] AS LOBRA
                ON LOBRA.IdObra = OBS.IdObra
                WHERE LOBRA.[IdUnidade] = @idunidade and OBR.[TipoPessoa] = 'Pessoa Juridica' and OBS.[TamanhoObra] > 500 AND LOBRA.[IdFase] = @idfaselead
                ORDER BY OBS.[IdArquiteto] 
                OFFSET (@PageNumber-1)*@RowsOfPage ROWS
                FETCH NEXT @RowsOfPage ROWS ONLY
    
    
        """.format(idUnidade, PageNumber, RowspPage, idFase)
    valores = []
    lista_dicts = []
    results = db.session.execute(query_fase).keys()
    colunas = [colunas for colunas in results]
    results = db.session.execute(query_fase).all()
    for result in results:
        cont = len(result)
        for i in range(cont):
            desc = {}
            print(desc)
            desc[colunas[i]] = result[i]
            lista_dicts.append(desc)
            

    return lista_dicts


def select_query_filtro_crm_obrasgrandes(tipo, idUnidade, pgnumber, rows):
    query = """
               DECLARE @TipoObra VARCHAR(10)
        DECLARE @idunidade AS INT
        DECLARE @PageNumber AS INT
        DECLARE @RowsOfPage AS INT

        SET @TipoObra = '{}'
        SET @idunidade = {}
        SET @PageNumber = {}
        SET @RowsOfPage = {}


        SELECT 
                OBS.[IdObra],OBS.[CpfCnpjContratante],OBS.[Contratante],OBS.[Telefone],OBS.[Email],OBS.[TipoPessoa]
                ,OBS.[Endereco],OBS.[Complemento],OBS.[Bairro],OBS.[IdCidade],OBS.[Cidade],OBS.[Estado],OBS.[Cep]
                ,OBS.[Latitude],OBS.[Longitude],OBS.[TipoObra],OBS.[IdCategoria],OBS.[IdAtividade],OBS.[DataCadastro],OBS.[TamanhoObra]
                ,OBS.[IdArquiteto],OBS.[NomeArquiteto],OBS.[TelefoneArquiteto],OBS.[DataInserido],OBS.[bitAtivo],OBS.[NumeroRRT]
                ,OBR.[IdObra],OBR.[CpfCnpjContratante],OBR.[Contratante],OBR.[Telefone],OBR.[Email],OBR.[TipoPessoa],OBR.[Endereco],OBR.[Complemento]
                ,OBR.[Bairro],OBR.[IdCidade],OBR.[Cidade],OBR.[Estado],OBR.[Cep],OBR.[Latitude],OBR.[Longitude],OBR.[TipoObra]
                ,OBR.[IdCategoria],OBR.[IdAtividade],OBR.[DataCadastro],OBR.[TamanhoObra],OBR.[IdArquiteto]
                ,OBR.[NomeArquiteto],OBR.[TelefoneArquiteto],OBR.[DataInserido],OBR.[bitAtivo],OBR.[NumeroRRT],LOBRA.[IdLeadObra]
                ,LOBRA.[IdObra],LOBRA.[IdUnidade],LOBRA.[IdColaborador],LOBRA.[IdFase],LOBRA.[DataInserido],LOBRA.[bitAtivo]
                ,LOBRA.[DataAgenda]
        FROM 	
            [HauszMapa].[Crm].[ObRaS] AS OBS
                JOIN [Crm].[ObRaS] AS OBR
                ON OBR.IdObra = OBS.IdObra
                JOIN [HauszMapa].[Crm].[LeadObra] AS LOBRA
                ON LOBRA.IdObra = OBS.IdObra
                WHERE LOBRA.[IdUnidade] = @idunidade and OBR.[TipoPessoa] = 'Pessoa Juridica' and OBR.[TipoObra] = @TipoObra and OBS.[TamanhoObra] > 500
                ORDER BY OBS.[IdArquiteto] 
                OFFSET (@PageNumber-1)*@RowsOfPage ROWS
                FETCH NEXT @RowsOfPage ROWS ONLY

            """.format(tipo, idUnidade, pgnumber, rows)

    lista_dicts = []
    results = db.session.execute(query).keys()
    colunas = [colunas for colunas in results]
    results = db.session.execute(query).all()
    for result in results:
        cont = len(result)
        for i in range(cont):
            desc = {}
            desc[colunas[i]] = result[i]
            lista_dicts.append(desc)

    return lista_dicts
