from fastapi import FastAPI

from .routers import calculator, vector

app = FastAPI()

app.include_router(calculator.router, prefix='/v1/calculator')
app.include_router(vector.router, prefix='/v1/vector')
