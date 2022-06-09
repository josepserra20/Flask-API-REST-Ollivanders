import json
import pytest

from repository.connect import db
from repository.model import Ollivanders

def test_getItem():
    db.getBbdd()
   
    test = Ollivanders.objects(name='test')
    json_data = test.to_json()
    dicts = json.loads(json_data)   
    for id in dicts:
        id.pop('_id')
        id['quality'] = int(id['quality'])
        id['sell_in'] = int(id['sell_in'])
    
    assert dicts == [{'name': 'test', 'quality': 2, 'sell_in': 3}]

