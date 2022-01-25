from flask import abort
from app import app, render_template, request


#Informar valor a ser retornado em caso de erro
@app.errorhandler(404)
def not_found(e):
    print(e)
    app.logger.error(f"Server Error: {e}, route: {request.url}")
    return "Valor não encontrado"

@app.errorhandler(500)
def server_error(e):
    print(e)
    app.logger.error(f"Server Error: {e}, route: {request.url}")
    return "Valor não encontrado"