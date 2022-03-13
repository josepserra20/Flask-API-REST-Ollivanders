from mongoengine import Document, StringField, IntField
class Ollivanders(Document):
    name = StringField(max_length=100)
    quality = IntField(max_value=100)
    sell_in = IntField(max_value=100)
    
