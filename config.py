# importações
from flask import Flask, jsonify, render_template # preparar resposta HTTP no formato json
from flask_sqlalchemy import SQLAlchemy
import os
import json # usar json.loads para transformar texto json em dicionário python
import requests # para fazer requisição http; pip3 install requests

# configurações
app = Flask(__name__)
# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__)) # sugestao do Kaue
arquivobd = os.path.join(path, 'pessoas.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)