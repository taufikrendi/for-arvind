from typing import Optional
from pydantic import BaseModel


class UserRegistrationSchemes(BaseModel):
    email: str
    first_name: str
    password: str
    phone_number: str
    agreement: str


class TokenSchemes(BaseModel):
    username: str


class AuthSchemes(TokenSchemes):
    password: str


class ChangePassSchemes(AuthSchemes):
    new_pwd: str


class SetPinSchemes(TokenSchemes):
    pin: str


class ChangePinSchemes(SetPinSchemes):
    new_pin: str


class AccountBankSchemes(TokenSchemes):
    holder_bank_code: str
    holder_number: str
    holder_name: str


class GetAccountBankSchemes(BaseModel):
    bank_name: str
    holder_name: Optional[str] = None
    holder_number: Optional[str] = None

    class Config:
        orm_mode = True


class AccountProfileSchemes(TokenSchemes):
    ektp_number: str
    npwp_number: str
    dob: str
    pob: str
    sex: str
    address: str
    province: str
    district: str
    sub_district: str


class SelfieFilledSchemes(TokenSchemes):
    selfie: str
    selfie_ektp: str
    ektp: str


class GetAccountProfileSchemes(TokenSchemes):
    first_name: str
    cooperative_number: Optional[str] = None
    phone_number: str

    class Config:
        orm_mode = True


class GetAccountSelfie(TokenSchemes):
    selfie: Optional[str] = None

    class Config:
        orm_mode = True