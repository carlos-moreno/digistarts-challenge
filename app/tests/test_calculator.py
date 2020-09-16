from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sum_1_plus_1():
    """Must return 2 in binary"""
    payload = {"number_one": "00000001", "number_two": "00000001"}
    response = client.post("/sum/", json=payload)
    assert response.json() == {"result": "00000010"}


def test_sum_1_plus_2():
    """Must return 3 in binary"""
    payload = {"number_one": "00000001", "number_two": "00000010"}
    response = client.post("/sum/", json=payload)
    assert response.json() == {"result": "00000011"}


def test_sum_1_plus_3():
    """Must return 4 in binary"""
    payload = {"number_one": "00000001", "number_two": "00000011"}
    response = client.post("/sum/", json=payload)
    assert response.json() == {"result": "00000100"}


def test_sum_150_plus_35():
    """Must return 185 in binary"""
    payload = {"number_one": "10010110", "number_two": "00100011"}
    response = client.post("/sum/", json=payload)
    assert response.json() == {"result": "10111001"}


def test_sub_1_less_1():
    """Must return 0 in binary"""
    payload = {"number_one": "00000001", "number_two": "00000001"}
    response = client.post("/sub/", json=payload)
    assert response.json() == {"result": "00000000"}


def test_sub_2_less_1():
    """Must return 1 in binary"""
    payload = {"number_one": "00000010", "number_two": "00000001"}
    response = client.post("/sub/", json=payload)
    assert response.json() == {"result": "00000001"}


def test_sub_5_less_2():
    """Must return 3 in binary"""
    payload = {"number_one": "00000101", "number_two": "00000010"}
    response = client.post("/sub/", json=payload)
    assert response.json() == {"result": "00000011"}


def test_sub_232_less_190():
    """Must return 42 in binary"""
    payload = {"number_one": "11101000", "number_two": "10111110"}
    response = client.post("/sub/", json=payload)
    assert response.json() == {"result": "00101010"}
