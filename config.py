from urllib.parse import quote_plus


parametros = ("Driver={SQL Server Native Client 11.0};"
                          "Server=w2019.hausz.com.br;"
                          "Database=HauszMapa;"
                          "UID=Aplicacao;"
                          "PWD=S3nh4Apl!caca0")


url_db = quote_plus(parametros)
SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=%s' %url_db
SQLALCHEMY_TRACK_MODIFICATIONS = False

