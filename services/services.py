import json
from flask import abort, jsonify
from repository.query import query
from repository.model import Ollivanders
from repository.connect import db

class Services():

    def getStock():
        stock = query.get_stock()
        # itemsList = []
        # for item in stock:
        #     itemsList.append({
        #         "name" : item.name,
        #         "quality" : item.quality,
        #         "sell_in": item.sell_in
        #     })
        # return itemsList
        json_data = stock.to_json()
        dicts = json.loads(json_data)
        for id in dicts:
            id.pop('_id')
            id['quality'] = int(id['quality'])
            id['sell_in'] = int(id['sell_in'])
        return dicts
       
    def getName(name):
        item = query.getStockByName(name)
        # itemList = []
        # for chac in item:
        #     itemList.append(
        #         {
        #             "name": chac.name,
        #             "quality": chac.quality,
        #             "sell_in": chac.sell_in
        #         }
        #     )
        # return itemList
        json_data = item.to_json()
        dicts = json.loads(json_data)
        for id in dicts:
            id.pop('_id')
            id['quality'] = int(id['quality'])
            id['sell_in'] = int(id['sell_in'])
        return dicts
        

    def DeleteByName(nameToDelete):
        deleted = query.DeleteByName(nameToDelete)
        deletedItemsNumber = deleted.count()
        if not deleted:
            abort(404,message="no se ha encontrado el item")
        else:
            deleted.delete()
            return {
                "name": nameToDelete,
                "info": True if Ollivanders.objects(name=nameToDelete).count() == 0 else False,
                "items deleted": deletedItemsNumber
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

    def updateByName(nameToFind, quality, sell_in):
        firstItem = query.getStockByNameFirst(nameToFind)
        firstItem.update(__raw__={"$set": {"quality": quality, "sell_in" : sell_in}})
        updatedid = firstItem.id
        return {
            'name': nameToFind,
            'quality': quality,
            'sell_in': sell_in,
            'Status': True if Ollivanders.objects.get(id=updatedid) else False
        }