import json
import pytest

def test_createItem(client):
    resp = client.post('/create/testcreated/1/1')
    assert resp.status_code == 200

    resp = client.get('/inventario/testcreated')
    assert resp.status_code == 200
    data = str(resp.data).split("\\n")
    lines = ""
    for line in data:
        if line.strip().startswith("<!--"):
            lines = line.strip().replace("&#39;", "\"")[5:-4]

    assert json.loads(lines) == [{"name": "testcreated", "quality": 1, "sell_in": 1}]
    client.delete('/inventario/testcreated')