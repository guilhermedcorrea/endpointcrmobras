from flask import Flask,jsonify,Response
from flask_sqlalchemy import SQLAlchemy
import flask_excel as excel
from flask_mail import Mail
from flask_marshmallow import Marshmallow,Schema,fields
import pandas as pd
from flask_restx import Api

app = Flask(__name__)
app.config.from_object('config')
excel.init_excel(app)
mail = Mail(app)
db = SQLAlchemy(app)
api = Api(app)


from app.routes import rotas_crm
from app.routes import rotas_obras_grandes