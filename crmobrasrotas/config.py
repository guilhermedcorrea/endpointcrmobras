from urllib.parse import quote_plus
Server = "server.hausz.com.br"
Database = "RRT"
driver = "SQL Server Native Client 11.0"
UID = "Aplicacao"
PWD = "S3nh4Apl!caca0"


parametros = (
"Driver={SQL Server Native Client 11.0};"
"Server=GUILHERME-PC\DEVMSSQLSERVER;"
"Database=obrascrm;"
"UID=sa;"
"PWD=Mudar@123"

)


url_db = quote_plus(parametros)
SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=%s' %url_db
SQLALCHEMY_TRACK_MODIFICATIONS = False