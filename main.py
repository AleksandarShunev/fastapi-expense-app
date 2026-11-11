from fastapi import FastAPI
from routers.transaction_router import transaction_router

app = FastAPI()

app.include_router(transaction_router)

