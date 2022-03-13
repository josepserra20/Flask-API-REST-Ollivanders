from flask import Flask
from controller.Inventario import Inventario
from controller.index import Index
from controller.NameFilter import NameFilter
from controller.CreateDoc import Create

app = Flask(__name__)

app.add_url_rule('/','',Index.get)
app.add_url_rule('/inventario','inventario',Inventario.get)
app.add_url_rule('/inventario/<name>','name',NameFilter.resolve, methods=['GET', 'DELETE'])
app.add_url_rule('/inventario/<name>/<quality>/<sell_in>', 'create',Create.resolve, methods=['POST'])
    