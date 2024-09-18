from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class TokenSchemes(BaseModel):
    username: str


class CreateTransactionsSchemes(TokenSchemes):
    unique_code = int
    amount = float
    payment_with = str


class GetOnGoingTransactionSchemes(BaseModel):
    amount: int
    transaction_type: str
    created_date: Optional[datetime] = None

    class Config:
        orm_mode = True


class ProvingTransactionsSchemes(TokenSchemes):
    trans_id: str
    image: str


class DepositPeriodSchemes(TokenSchemes):
    amount: float
    period_base: int


class FundRaiseSchemes(TokenSchemes):
    code: str
    amount: float
    get_saving: str
    from_saving_amount: Optional[float] = None
    unique_code: Optional[int] = None
    payment_with: Optional[str] = None