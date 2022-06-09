import json
from mongoengine import connect

class db():

    def getBbdd():

        conexion = connect(host="mongodb+srv://m001-student:m001-mongodb-basics@cluster0.fdyqp.mongodb.net/ollivanders")
        return conexion["ollivanders"]["ollivanders"]

    # def testdb():
    #     conexion = connect(host="mongodb+srv://m001-student:m001-mongodb-basics@cluster0.fdyqp.mongodb.net/ollivanders")
    #     return conexion["ollivanders"]["testollivanders"]

    def restardb():
        db.getBbdd().drop()
        with open("tests\ollivanders.json") as f:
            db.getBbdd().insert_many(json.load(f))
            





    
