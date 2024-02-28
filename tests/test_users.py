from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    res = client.get('/')
    print(res.json().get('message'))
    assert res.json().get('message') == 'Hello world'
    assert res.status_code == 200


def test_create_user():
    res = client.post(
        "/users/", json={"email": "test123@gmail.com", "password": "password123"})
    print(res.json())
    assert res.status_code == 201
