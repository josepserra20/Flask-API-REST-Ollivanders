import json
import pytest

def test_updateItem(client):
    resp = client.put('/update/test/2/3')
    assert resp.status_code == 200

    resp = client.get('/inventario/test')
    assert resp.status_code == 200
    data = str(resp.data).split("\\n")
    lines = ""
    for line in data:
        if line.strip().startswith("<!--"):
            lines = line.strip().replace("&#39;", "\"")[5:-4]

    assert json.loads(lines) == [{"name": "test", "quality": 2, "sell_in": 3}]