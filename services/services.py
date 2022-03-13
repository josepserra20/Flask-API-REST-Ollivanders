from flask import abort
from repository.query import query
from repository.model import Ollivanders
from repository.connect import db
class Services():

    def getStock():
        stock = query.get_stock()
        itemsList = []
        for item in stock:
            itemsList.append({
                "name" : item.name,
                "quality" : item.quality,
                "sell_in": item.sell_in
            })
        return itemsList
    
    def getName(name):
        return query.getStockByName(name)

    def DeleteByName(nameToDelete):
        deleted = query.DeleteByName(nameToDelete)
        if not deleted:
            abort(404,message="no se ha encontrado el item")
        else:
            deleted.delete()
            return {
                "name": nameToDelete,
                "info": True if Ollivanders.objects(name=nameToDelete).count() == 0 else False
            }

    def createDoc(nameToAdd,qualityToAdd, sell_inToAdd):
        db.getBbdd()
        newItem = Ollivanders(
            name=nameToAdd,
            quality=qualityToAdd,
            sell_in=sell_inToAdd
        )
        newItem.save()
        itemid = newItem.id    
        return {
            'name': nameToAdd,
            'quality': qualityToAdd,
            'sell_in': sell_inToAdd,
            'Status': True if Ollivanders.objects.get(id=itemid) else False
        }
