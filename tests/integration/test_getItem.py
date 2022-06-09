import json
import pytest


def test_getItem(client):
    response = client.get('/inventario/test')
    assert response.status_code == 200
    
    data = str(response.data).split("\\n")
    lines = ""
    for line in data:
        if line.strip().startswith("<!--"):
            lines = line.strip().replace("&#39;", "\"")[5:-4]

    assert json.loads(lines) == [{"name": "test", "quality": 1, "sell_in": 1}]
