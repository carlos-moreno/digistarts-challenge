from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse


router = APIRouter()

json_response = JSONResponse(
    status_code=status.HTTP_400_BAD_REQUEST,
    content={
        "message": "The request must contain two valid binary numbers between 0-255"
    },
)


class Item(BaseModel):
    number_one: str
    number_two: str


dict_of_operations = {
    "sum": lambda item: bin(int(item.number_one, 2) + int(item.number_two, 2)),
    "sub": lambda item: bin(int(item.number_one, 2) - int(item.number_two, 2)),
    "mult": lambda item: bin(int(item.number_one, 2) * int(item.number_two, 2)),
    "div": lambda item: bin(int(item.number_one, 2) // int(item.number_two, 2)),
    "mod": lambda item: bin(int(item.number_one, 2) % int(item.number_two, 2)),
}


def validate_number(item: Item):
    """Validates the numbers for the type and range allowed
    :param item: Item type object
    """
    if (
        not 0 <= int(item.number_one, 2) <= 255
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


@router.post("/sum/", tags=["calculator"])
def binary_sum(item: Item):
    """Returns the sum of two binary numbers"""
    try:
        validate_number(item)
        return format_return(dict_of_operations["sum"](item))
    except (ValueError, HTTPException):
        return json_response


@router.post("/sub/", tags=["calculator"])
def binary_sub(item: Item):
    """Returns the subtraction of two binary numbers"""
    try:
        validate_number(item)
        return format_return(dict_of_operations["sub"](item))
    except (ValueError, HTTPException):
        return json_response


@router.post("/mult/", tags=["calculator"])
def binary_mult(item: Item):
    """Returns the multiplication of two binary numbers"""
    try:
        validate_number(item)
        return format_return(dict_of_operations["mult"](item))
    except (ValueError, HTTPException):
        return json_response


@router.post("/div/", tags=["calculator"])
def binary_div(item: Item):
    """Returns the division of two binary numbers"""
    try:
        validate_number(item)
        return format_return(dict_of_operations["div"](item))
    except (ValueError, HTTPException):
        return json_response


@router.post("/mod/", tags=["calculator"])
def binary_mod(item: Item):
    """Returns the remainder of the division of two binary numbers"""
    try:
        validate_number(item)
        return format_return(dict_of_operations["mod"](item))
    except (ValueError, HTTPException):
        return json_response
