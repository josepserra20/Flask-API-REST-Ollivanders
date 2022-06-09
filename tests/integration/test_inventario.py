import pytest

def test_inventario(client):
    resp = client.get('/inventario')
    data = str(resp.data).split("\\n")
    assert resp.status_code == 200
    lines = ""
    for line in data:
        if line.strip().startswith("<!--"):    
            lines = line.strip().replace("&#39;","\"")[6:-5]
    assert lines == '{"name": "Aged_brie", "quality": 3, "sell_in": 4}, {"name": "Aged_brie", "quality": 12, "sell_in": 0}, {"name": "Sulfuras", "quality": 4, "sell_in": 8}, {"name": "Sulfuras", "quality": 4, "sell_in": 4}, {"name": "Sulfuras", "quality": 4, "sell_in": 4}, {"name": "Aged_Brie", "quality": 34, "sell_in": 30}, {"name": "Aged_Brie", "quality": 12, "sell_in": 3}, {"name": "Aged_Brie", "quality": 12, "sell_in": 3}, {"name": "Aged_Brie", "quality": 12, "sell_in": 3}, {"name": "Aged_Brie", "quality": 55, "sell_in": 4}, {"name": "test", "quality": 1, "sell_in": 1}'