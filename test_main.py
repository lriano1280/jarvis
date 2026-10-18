from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hola_default():
    r = client.get("/hola")
    assert r.status_code == 200
    assert r.json() == {"mensaje": "hola mundo"}

def test_hola_nombre():
    r = client.get("/hola?nombre=Leo")
    assert r.status_code == 200
    assert r.json()["mensaje"] == "hola Leo"

def test_salud():
    r = client.get("/salud")
    assert r.status_code == 200
    assert r.json() == {"estado": "ok"}
