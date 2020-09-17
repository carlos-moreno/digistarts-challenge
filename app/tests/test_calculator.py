from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sum_1_plus_1():
    """Must return 2 in binary"""
    payload = {"number_one": "00000001", "number_two": "00000001"}
    response = client.post("/v1/calculator/sum/", json=payload)
    assert response.json() == {"result": "00000010"}


def test_sum_1_plus_2():
    """Must return 3 in binary"""
    payload = {"number_one": "00000001", "number_two": "00000010"}
    response = client.post("/v1/calculator/sum/", json=payload)
    assert response.json() == {"result": "00000011"}


def test_sum_1_plus_3():
    """Must return 4 in binary"""
    payload = {"number_one": "00000001", "number_two": "00000011"}
    response = client.post("/v1/calculator/sum/", json=payload)
    assert response.json() == {"result": "00000100"}


def test_sum_150_plus_35():
    """Must return 185 in binary"""
    payload = {"number_one": "10010110", "number_two": "00100011"}
    response = client.post("/v1/calculator/sum/", json=payload)
    assert response.json() == {"result": "10111001"}


def test_sub_1_less_1():
    """Must return 0 in binary"""
    payload = {"number_one": "00000001", "number_two": "00000001"}
    response = client.post("/v1/calculator/sub/", json=payload)
    assert response.json() == {"result": "00000000"}


def test_sub_2_less_1():
    """Must return 1 in binary"""
    payload = {"number_one": "00000010", "number_two": "00000001"}
    response = client.post("/v1/calculator/sub/", json=payload)
    assert response.json() == {"result": "00000001"}


def test_sub_5_less_2():
    """Must return 3 in binary"""
    payload = {"number_one": "00000101", "number_two": "00000010"}
    response = client.post("/v1/calculator/sub/", json=payload)
    assert response.json() == {"result": "00000011"}


def test_sub_232_less_190():
    """Must return 42 in binary"""
    payload = {"number_one": "11101000", "number_two": "10111110"}
    response = client.post("/v1/calculator/sub/", json=payload)
    assert response.json() == {"result": "00101010"}


def test_mult_1_by_1():
    """Must return 1 in binary"""
    payload = {"number_one": "00000001", "number_two": "00000001"}
    response = client.post("/v1/calculator/mult/", json=payload)
    assert response.json() == {"result": "00000001"}


def test_mult_2_by_1():
    """Must return 1 in binary"""
    payload = {"number_one": "00000010", "number_two": "00000001"}
    response = client.post("/v1/calculator/mult/", json=payload)
    assert response.json() == {"result": "00000010"}


def test_mult_40_by_3():
    """Must return 120 in binary"""
    payload = {"number_one": "00101000", "number_two": "00000011"}
    response = client.post("/v1/calculator/mult/", json=payload)
    assert response.json() == {"result": "01111000"}


def test_div_2_by_1():
    """Must return 2 in binary"""
    payload = {"number_one": "00000010", "number_two": "00000001"}
    response = client.post("/v1/calculator/div/", json=payload)
    assert response.json() == {"result": "00000010"}


def test_div_180_by_3():
    """Must return 60 in binary"""
    payload = {"number_one": "10110100", "number_two": "00000011"}
    response = client.post("/v1/calculator/div/", json=payload)
    assert response.json() == {"result": "00111100"}


def test_div_12_by_4():
    """Must return 3 in binary"""
    payload = {"number_one": "00001100", "number_two": "00000100"}
    response = client.post("/v1/calculator/div/", json=payload)
    assert response.json() == {"result": "00000011"}


def test_mod_2_by_1():
    """Must return 0 in binary"""
    payload = {"number_one": "00000010", "number_two": "00000001"}
    response = client.post("/v1/calculator/mod/", json=payload)
    assert response.json() == {"result": "00000000"}


def test_mod_10_by_4():
    """Must return 2 in binary"""
    payload = {"number_one": "00001010", "number_two": "00000100"}
    response = client.post("/v1/calculator/mod/", json=payload)
    assert response.json() == {"result": "00000010"}


def test_mod_100_by_5():
    """Must return 0 in binary"""
    payload = {"number_one": "01100100", "number_two": "00000101"}
    response = client.post("/v1/calculator/mod/", json=payload)
    assert response.json() == {"result": "00000000"}
