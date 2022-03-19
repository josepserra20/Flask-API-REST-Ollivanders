import pytest
from repository.model import Ollivanders

def test_deleteItem(client):
    resp = client.delete('/inventario/test')
    assert resp.status_code == 200
    assert Ollivanders.objects(name='test').count() == 0
    


