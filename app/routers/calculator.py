from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class Item(BaseModel):
    number_one: str
    number_two: str


dict_of_operations = {
    "sum": lambda Item: bin(int(Item.number_one, 2) + int(Item.number_two, 2)),
    "sub": lambda Item: bin(int(Item.number_one, 2) - int(Item.number_two, 2)),
    "mult": lambda Item: bin(int(Item.number_one, 2) * int(Item.number_two, 2)),
    "div": lambda Item: bin(int(Item.number_one, 2) // int(Item.number_two, 2)),
    "mod": lambda Item: bin(int(Item.number_one, 2) % int(Item.number_two, 2)),
}


def format_return(number: str):
    return {"result": number[2:].zfill(8)}


@router.post("/sum/", tags=["calculator"])
def binary_sum(item: Item):
    return format_return(dict_of_operations["sum"](item))


@router.post("/sub/", tags=["calculator"])
def binary_sub(item: Item):
    return format_return(dict_of_operations["sub"](item))


@router.post("/mult/", tags=["calculator"])
def binary_mult(item: Item):
    return format_return(dict_of_operations["mult"](item))


@router.post("/div/", tags=["calculator"])
def binary_div(item: Item):
    return format_return(dict_of_operations["div"](item))


@router.post("/mod/", tags=["calculator"])
def binary_mod(item: Item):
    return format_return(dict_of_operations["mod"](item))
