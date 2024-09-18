from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class TokenDataSchemes(BaseModel):
    username: Optional[str] = None


class GetDepositSchemes(BaseModel):
    email: str
    principal_amount: Optional[str] = None
    mandatory_amount: Optional[str] = None
    period_left: Optional[int] = None
    period_end: Optional[datetime] = None

    class Config:
        orm_mode = True