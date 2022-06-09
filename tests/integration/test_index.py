import pytest

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<h1>This is the main page of ollivaders API REST</h1>" in response.data
