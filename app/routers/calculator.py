from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()

json_response = JSONResponse(
    status_code=status.HTTP_400_BAD_REQUEST,
    content={
        "message": "The request must contain two valid binary numbers between 0-255"
    },
)


class Item(BaseModel):
    number_one: str = None
    number_two: str = None


dict_of_operations = {
    "sum": lambda item: bin(int(item.number_one, 2) + int(item.number_two, 2)),
    "sub": lambda item: bin(int(item.number_one, 2) - int(item.number_two, 2)),
    "mult": lambda item: bin(int(item.number_one, 2) * int(item.number_two, 2)),
    "div": lambda item: bin(int(item.number_one, 2) // int(item.number_two, 2)),
    "mod": lambda item: bin(int(item.number_one, 2) % int(item.number_two, 2)),
}


def is_none(item: Item):
    """Checks if any of the fields are null"""
    return item.number_one is None or item.number_two is None


def validate_number(item: Item):
    """Validates the numbers for the type and range allowed
    :param item: Item type object
    """
    if (
        is_none(item)
        or not 0 <= int(item.number_one, 2) <= 255
        or not 0 <= int(item.number_two, 2) <= 255
    ):
        raise ValueError


def format_return(number: str):
    """Returns the number formatted in binary
    :param number: number to be formatted
    """
    result = (
        "-" + number[3:].zfill(8) if number.startswith("-") else number[2:].zfill(8)
    )
    return {"result": result}


@router.post("/sum/", tags=["Calculator"])
def binary_sum(item: Item):
    """Returns the sum of two binary numbers"""
    try:
        validate_number(item)
        return format_return(dict_of_operations["sum"](item))
    except ValueError:
        return json_response


@router.post("/sub/", tags=["Calculator"])
def binary_sub(item: Item):
    """Returns the subtraction of two binary numbers"""
    try:
        validate_number(item)
        return format_return(dict_of_operations["sub"](item))
    except ValueError:
        return json_response


@router.post("/mult/", tags=["Calculator"])
def binary_mult(item: Item):
    """Returns the multiplication of two binary numbers"""
    try:
        validate_number(item)
        return format_return(dict_of_operations["mult"](item))
    except ValueError:
        return json_response


@router.post("/div/", tags=["Calculator"])
def binary_div(item: Item):
    """Returns the division of two binary numbers"""
    try:
        validate_number(item)
        return format_return(dict_of_operations["div"](item))
    except ValueError:
        return json_response


@router.post("/mod/", tags=["Calculator"])
def binary_mod(item: Item):
    """Returns the remainder of the division of two binary numbers"""
    try:
        validate_number(item)
        return format_return(dict_of_operations["mod"](item))
    except ValueError:
        return json_response
