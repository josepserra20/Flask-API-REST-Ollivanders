from flask import Flask
from flask_restful import Resource, Api
from controller.Index import Index

app = Flask(__name__)
api = Api(app, catch_all_404s=True)


api.add_resource(Index, '/')