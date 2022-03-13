from flask import request
from services.services import Services


class Create:

    def resolve(name,quality,sell_in):
        if request.method == 'POST':
            return Create.post(name,quality,sell_in)

    def post(name, quality, sell_in):
        return Services.createDoc(name,quality,sell_in)
        
