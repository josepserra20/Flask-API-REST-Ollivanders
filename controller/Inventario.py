from flask import render_template
from services.services import Services 

class Inventario:

    def get():
        return render_template('inventario.html', lista=Services.getStock())
    



