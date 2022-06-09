from flask import request
from services.services import Services

class Update:

    def resolve(name, quality, sell_in):
        if request.method == 'PUT':
            return Update.updateItem(name, quality, sell_in)

    def updateItem(name, quality, sell_in):
        return Services.updateByName(name, quality, sell_in)