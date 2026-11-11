from fastapi import APIRouter, status, HTTPException
from data.models import Transaction
from services import transaction_service

transaction_router = APIRouter(prefix='/transactions', tags=['Transactions'])

@transaction_router.post('', status_code=status.HTTP_201_CREATED)
def add_transaction(transaction: Transaction):
    added_transaction = transaction_service.add_transaction(transaction)
    if added_transaction is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return added_transaction