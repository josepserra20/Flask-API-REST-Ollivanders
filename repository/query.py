from repository.connect import db
from mongoengine import * 
from repository.model import Ollivanders

class query:

    def get_stock():
        db.getBbdd()
        return Ollivanders.objects()
        
    def getStockByName(nametofind):
        db.getBbdd()
        return Ollivanders.objects(name=nametofind)
        
    def DeleteByName(nameToDelete):
        db.getBbdd()
        return Ollivanders.objects(name=nameToDelete)
    
    def getStockByNameFirst(nametofind):
        db.getBbdd()
        return Ollivanders.objects(name=nametofind)[0]



    