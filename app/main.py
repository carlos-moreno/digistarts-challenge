from fastapi import FastAPI

from .routers import calculator

app = FastAPI()

app.include_router(calculator.router)
