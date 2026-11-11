from pydantic import BaseModel, Field
from datetime import date
from typing import Annotated
from decimal import Decimal

Decimal10_2 = Annotated[Decimal, Field(max_digits=10, decimal_places=2)]


class Transaction(BaseModel):
    id: int | None = None
    amount: Decimal10_2
    description: str
    entry_date: date = date.today()
    type: str
    category_id: int 