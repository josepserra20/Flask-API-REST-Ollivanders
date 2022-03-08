from flask import render_template
from services.services import Services

class NameFilter:

    def get(name):
        return render_template('inventarioName.html', lista=Services.getName(name))