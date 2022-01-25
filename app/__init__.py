from flask import Flask,jsonify,Response, render_template,abort, request
from flask_sqlalchemy import SQLAlchemy
import flask_excel as excel
from flask_mail import Mail
from flask_marshmallow import Marshmallow,Schema,fields
import pandas as pd
from flask_restx import Api
from flask_cors import CORS, cross_origin
from flask.json import JSONEncoder


app = Flask(__name__)
app.config.from_object('config')
excel.init_excel(app)
mail = Mail(app)
db = SQLAlchemy(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

from app.routes import rotas_crm,rotas_obras_grandes
