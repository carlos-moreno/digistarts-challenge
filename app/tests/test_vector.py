import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.routers.vector import validate_number_n

client = TestClient(app)


def test_raise_value_error():
    """Should return an error when the first element is less than 1"""
    with pytest.raises(ValueError):
        validate_number_n(0)


def test_validate_number_n():
    """Should return an error when the first element is greater than 1000"""
    payload = {"numbers": [1001, 2, 0, -125, 50, 1]}
    response = client.post("/v1/vector/set/", json=payload)
    assert response.json() == {
        "message": "The request must contain two valid binary numbers between 0-255"
    }


def test_validate_numbers_k_greater_1000():
    """Should return an error when any element is greater than 1000"""
    payload = {"numbers": [6, 2, 0, -125, 50, 10000, -12]}
    response = client.post("/v1/vector/set/", json=payload)
    assert response.json() == {
        "message": "The request must contain two valid binary numbers between 0-255"
    }


def test_validate_numbers_k_less_1000():
    """Should return an error when any element is less than -1000"""
    payload = {"numbers": [5, 3, -125, -1001, 90, -12]}
    response = client.post("/v1/vector/set/", json=payload)
    assert response.json() == {
        "message": "The request must contain two valid binary numbers between 0-255"
    }


def test_validate_list():
    """Should return an error when the first value of the first element is different from the number of items remaining in the list"""
    payload = {"numbers": [6, 2, 0, -125, 50, 1000, -12, 3, 985]}
    response = client.post("/v1/vector/set/", json=payload)
    assert response.json() == {
        "message": "The request must contain two valid binary numbers between 0-255"
    }


def test_validate_list_empty():
    """Should return an error when the list is empty"""
    payload = {"numbers": []}
    response = client.post("/v1/vector/set/", json=payload)
    assert response.json() == {
        "message": "The request must contain two valid binary numbers between 0-255"
    }


def test_result_is_1():
    """Must return a single element of value 1"""
    payload = {"numbers": [5, 1, 1, 1, 1, 1]}
    response = client.post("/v1/vector/set/", json=payload)
    assert response.json() == {"result": [1]}


def test_result_is_6_7_8_9_10():
    """Must return a single element of value 1"""
    payload = {"numbers": [10, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6]}
    response = client.post("/v1/vector/set/", json=payload)
    assert response.json() == {"result": [6, 7, 8, 9, 10]}
