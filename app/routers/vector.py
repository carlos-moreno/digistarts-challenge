from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()

json_response = JSONResponse(
    status_code=status.HTTP_400_BAD_REQUEST,
    content={
        "message": "The list must obey the following rule: first element N (1 <= N <= 1000) and "
        "N integers K (-1000 <= K <= 1000)"
    },
)


class Vector(BaseModel):
    numbers: list


def validate_list(lst: list):
    """Checks whether the list is empty"""
    if not lst or (lst[0] != len(lst[1:])):
        raise ValueError


def validate_number_n(number: int):
    """Validates if the number N is in the range (1, 1000)
    :param number: number to be analyzed
    """
    if not 1 <= number <= 1000:
        raise ValueError


def validate_numbers_k(numbers: list):
    """Validates that the numbers in the list are in the range (-1000, 1000)
    :param numbers: list of numbers
    """
    for n in numbers:
        if not isinstance(n, int) or not -1000 <= n <= 1000:
            raise ValueError


@router.post("/set/", tags=["Vector"])
def make_set(vector: Vector):
    """Returns a set of numbers"""
    try:
        validate_list(vector.numbers)
        validate_number_n(vector.numbers[0])
        validate_numbers_k(vector.numbers[1:])
        return {"result": sorted(set(vector.numbers[1:]))}
    except ValueError:
        return json_response
