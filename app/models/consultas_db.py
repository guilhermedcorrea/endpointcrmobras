from app import db
'''
def paginacao_crm_prospecao(iduni, pag, rows):
    paginas = []
    ident = int(iduni)
    pagina = int(pag)
    linhas = int(rows)
    query = """EXEC Paginacaocrm @IdUnidade = 1, @RowsOfPage= 10, @PageNumber = 1""".format(ident, pagina, linhas)
        
    paginacao = db.session.execute(query).all()
    for pag in paginacao:
        for x in pag:
            print(x)
            paginas.append(x)
    return paginas
  

'''