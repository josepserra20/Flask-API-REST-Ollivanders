from flask import Flask
from controller.Inventario import Inventario
from controller.index import Index
from controller.NameFilter import NameFilter

app = Flask(__name__)

app.add_url_rule('/','',Index.get)

app.add_url_rule('/inventario','inventario',Inventario.get)

app.add_url_rule('/inventario/<name>','name',NameFilter.get)

# app.route_url_rule('deletebyname/<name>', 'delete', )
    