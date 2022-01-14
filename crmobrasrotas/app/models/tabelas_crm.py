from app import db,Schema,fields,app,pd
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, post_load, fields
import json
from sqlalchemy import MetaData, Table, Column, Integer



class Arquiteto(db.Model):
    __tablename__ = 'Arquiteto'
    IdArquiteto = db.Column(db.Integer, primary_key=True)
    NomeArquiteto = db.Column(db.String(200), unique=True)
    Email = db.Column(db.String(200), nullable=True)
    Telefone = db.Column(db.String(20), nullable=True)
    Idade = db.Column(db.Integer, nullable=True)
    Logradouro = db.Column(db.String(200), nullable=True)
    Numero = db.Column(db.String(10), nullable=True)
    Complemento = db.Column(db.String(200), nullable=True)
    Bairro = db.Column(db.String(200), nullable=True)
    Cep = db.Column(db.String(20), nullable=True)
    IdCidade = db.Column(db.Integer, nullable=True)
    Cidade = db.Column(db.String(200), nullable=True)
    Uf = db.Column(db.String(100), nullable=True)
    RazaoSocial = db.Column(db.String(100), nullable=True)
    TipoVinculo = db.Column(db.String(100), nullable=True)
    UfEscritorio = db.Column(db.String(2), nullable=True)
    BitAtivo = db.Column(db.Boolean,default=True)
    DataInserido = db.Column(DateTime(timezone=True), server_default=func.now())
    obrasFeitas = db.relationship('Obrasfeitas', back_populates='obrasFeitas')
    obras = db.relationship('Obras', back_populates='obras')


    def __init__(self,NomeArquiteto, Email, Telefone, Idade,Logradouro, Numero,Complemento, Bairro,Cep,IdCidade, Cidade,Uf,RazaoSocial,TipoVinculo,UfEscritorio):
        self.NomeArquiteto = NomeArquiteto
        self.Email = Email
        self.Telefone = Telefone
        self.Idade = Idade
        self.Logradouro = Logradouro
        self.Numero = Numero
        self.Complemento = Complemento
        self.Bairro = Bairro
        self.Cep = Cep
        self.IdCidade = IdCidade
        self.Cidade = Cidade
        self.Uf = Uf
        self.RazaoSocial = RazaoSocial
        self.TipoVinculo = TipoVinculo
        self.UfEscritorio = UfEscritorio


class Obrasfeitas(db.Model):
    __tablename__ = 'ArquitetoObras'
    IdArqObra = db.Column(db.Integer,primary_key=True, unique=True)
    ArquitetoId = db.Column(db.Integer, db.ForeignKey('Arquiteto.IdArquiteto')) #IdArqObra
    idObra = db.Column(db.Integer)
    Nome = db.Column(db.String(60),nullable=True,unique = False)
    QuantidadeObrasRegiao = db.Column(db.Integer, nullable=True,unique = False)
    QuantidadeObrasProfissional = db.Column(db.Integer, nullable=True,unique = False)
    GrupoQuantidadeMetrosObras = db.Column(db.Float, nullable=True,unique = False)
    GrupoQuantidadeObras = db.Column(db.String(50), nullable=True,unique = False)
    Meses = db.Column(db.String(50), nullable=True,unique = False)
    GrupoMeses = db.Column(db.String(50), nullable=True,unique = False)
    obrasFeitas = db.relationship("Arquiteto", back_populates='obrasFeitas')




    def __init__(self, Nome,ArquitetoId, QuantidadeObrasRegiao, QuantidadeObrasProfissional,GrupoQuantidadeMetrosObras,GrupoQuantidadeObras,
                 Meses,GrupoMeses):

        self.Nome = Nome
        self.ArquitetoId = ArquitetoId
        self.QuantidadeObrasRegiao = QuantidadeObrasRegiao
        self.QuantidadeObrasProfissional = QuantidadeObrasProfissional
        self.GrupoQuantidadeMetrosObras = GrupoQuantidadeMetrosObras
        self.GrupoQuantidadeObras = GrupoQuantidadeObras
        self.Meses = Meses
        self.GrupoMeses = GrupoMeses


class Obras(db.Model):
    __tablename__ = 'Obra'
    IdObra = db.Column(db.Integer, primary_key=True,unique = True)
    ArquitetoId = db.Column(db.Integer, db.ForeignKey('Arquiteto.IdArquiteto'))
    NomeObra = db.Column(db.String(200), nullable=True, unique=False)
    Uf = db.Column(db.String(2), nullable=True, unique=False)
    IdCidade = db.Column(db.Integer, nullable=True, unique=False)
    Cidade = db.Column(db.String(200), nullable=True, unique=False)
    TipoObra = db.Column(db.String(200), nullable=True, unique=False)
    PrevisaoTermino = db.Column(db.Date, unique=False)
    GrupoAtividadeProfissional = db.Column(db.String(200), nullable=True, unique=False)
    TipoLogradouro = db.Column(db.String(150), nullable=True, unique=False)
    Logradouro = db.Column(db.String(150), nullable=True, unique=False)
    Numero = db.Column(db.String(20), nullable=True, unique=False)
    Complemento = db.Column(db.String(150), nullable=True, unique=False)
    Bairro = db.Column(db.String(150), nullable=True, unique=False)
    Cep = db.Column(db.String(20), nullable=True, unique=False)
    Grupo = db.Column(db.String(100), nullable=True, unique=False)
    GrupoTamanhoObra = db.Column(db.String(100), nullable=True, unique=False)
    obras = db.relationship("Arquiteto",back_populates="obras")


    def __init__(self,NomeObra,ArquitetoId, Uf,IdCidade, Cidade, TipoObra, PrevisaoTermino, GrupoAtividadeProfissional,TipoLogradouro,Logradouro,Numero,Complemento,Bairro, Cep, Grupo, GrupoTamanhoObra):
        self.NomeObra = NomeObra
        self.ArquitetoId = ArquitetoId
        self.Uf = Uf
        self.IdCidade = IdCidade
        self.Cidade = Cidade
        self.TipoObra = TipoObra
        self.PrevisaoTermino = PrevisaoTermino
        self.GrupoAtividadeProfissional = GrupoAtividadeProfissional
        self.TipoLogradouro = TipoLogradouro
        self.Logradouro = Logradouro
        self.Numero = Numero
        self.Complemento = Complemento
        self.Bairro = Bairro
        self.Cep = Cep
        self.Grupo = Grupo
        self.GrupoTamanhoObra = GrupoTamanhoObra

def all_select():
    
    listas = []
    all_valores = """ EXEC FiltrarAllObras"""
    all_obras = db.engine.execute(all_valores).all()
    print(all_obras)
    for all in all_obras:
        desc = {}
        desc['NomeArquiteto'] = all[1]
        desc["Email"] = all[2]
        desc["Telefone"] = all[3]
        desc["Idade"] = all[4]
        desc["Logradouro"] = all[5]
        desc["Numero"] = all[6]
        desc["Complemento"] = all[7]
        desc["Bairro"] = all[8]
        desc["Cep"] = all[9]
        desc["idCidade"] = all[10]
        desc["UF"] = all[11]
        desc["RazãoSocial"] = all[12]
        desc["UF Escritorio"] = all[13]
        desc["BitAtivo"] = all[14]
        desc["DataInserido"] = all[15]
        desc["Nome"] = all[16]
        desc["Quantidade de Obras Região"] = all[17]
        desc["Quantidade de Obras Profissional"] = all[18]
        desc["Grupo Quantidade de Metros Obras"] = all[19]
        desc["Grupo Quantidade Obras"] = all[20]
        desc["Meses"] = all[21]
        desc["Grupo Meses"] = all[22]
        desc["Nome Obra"] = all[23]
        desc["UF"] = all[24]
        desc["Cidade"] = all[25]
        desc["Tipo Obra"] = all[26]
        desc["Previsao Termino"] = all[27]
        desc["Grupo Atividade Profissional"] = all[28]
        desc["Tipo Logradouro"] = all[29]
        desc["Logradouro"] = all[30]
        desc["Numero"] = all[31]
        desc["complemento"] = all[32]
        desc["Bairro"] = all[33]
        desc["Cep"] = all[34]
        desc["Grupo"] = all[35]
        desc["Grupo TamanhoObra"] = all[36]

        listas.append(desc)

    return listas


        



        
   








