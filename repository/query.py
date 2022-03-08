from flask import g
from repository.connect import db

class query:

    def get_stock():
        conexion = db.getBbdd()
        return list(conexion.find({}, {"_id": False }))

    def getStockByName(name):
        conexion = db.getBbdd()
        return list(conexion.find({"name":name}, {"_id" : False}))