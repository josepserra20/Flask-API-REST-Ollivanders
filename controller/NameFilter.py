from flask import render_template, request
from services.services import Services

class NameFilter:

    @staticmethod
    def resolve(name):
        if request.method == "GET":
            return NameFilter.get(name)
        if request.method == "DELETE":
            return NameFilter.delete(name)

    @staticmethod
    def get(name):
        return render_template('inventarioName.html', lista=Services.getName(name))

    @staticmethod
    def delete(name):
        return Services.DeleteByName(name)
