from flask import Flask
from controller.CreateDoc import Create

from controller.Inventario import Inventario
from controller.NameFilter import NameFilter
from controller.UpdateItem import Update
from controller.index import Index
from repository.connect import db


class Factory:
    def create_app():
        app = Flask(__name__)
        app.add_url_rule('/','',Index.get)
        app.add_url_rule('/inventario','inventario',Inventario.get)
        app.add_url_rule('/inventario/<name>','name',NameFilter.resolve, methods=['GET', 'DELETE'])
        app.add_url_rule('/create/<name>/<quality>/<sell_in>', 'create',Create.resolve, methods=['POST'])
        app.add_url_rule('/update/<name>/<quality>/<sell_in>', 'update', Update.resolve, methods=['PUT'])
        
        db.restardb()
        
        return app