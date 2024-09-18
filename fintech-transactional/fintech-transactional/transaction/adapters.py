from jose import JWTError, jwt
from typing import Optional

from django.conf import settings
from django.contrib.auth.models import User
from django.db import connections

from excep.exceptions import *

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from account.models import AccountBankUsers, AccountProfile
from deposits.models import DepositMemberPrincipal, DepositProductMaster
from loan.models import LoanApproval
from transaction.models import TransactionDepositVerified
from transaction.schemes import TokenSchemes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.KEY_HASHED, algorithms=[settings.ALGORITHM])
        username: Optional[str] = payload.get("sub")
        token_data = TokenSchemes(username=username)
    except JWTError:
        raise except_status_401
    if not User.objects.using('default_slave').filter(username=username): raise except_status_401
    return token_data


async def check_before_trans(data: dict):
    try:
        payload = data.copy()
        username: Optional[str] = payload.get('username')
        amount: Optional[str] = payload.get('amount')

        check_username = User.objects.using('default_slave').filter(username=username)
        check = AccountBankUsers.objects.using('default_slave').filter(
            account_bank_user_related_to_user=username
        )
        first_time = DepositMemberPrincipal.objects.using('funds_slave').filter(
            deposit_member_principal_user_related=username,
            deposit_member_principal_payment_principal_status=False,
        )
        if not check_username: raise except_status_403
        if not check: raise except_status_406_need_bank_account
        if first_time and amount < 210000:
            raise except_status_406_first_payment
        return data

    except(TypeError, ValueError, OverflowError):
        raise except_status_500


async def check_proving_trans(data: dict):
    try:
        payload = data.copy()
        username: Optional[str] = payload.get('username')
        trans_id: Optional[str] = payload.get('trans_id')
        image: Optional[str] = payload.get('image')
        check_username = User.objects.using('default_slave').filter(
            username=username,
        )
        if not trans_id or not username or not image: raise except_status_403
        if not check_username: raise except_status_403
        trans_verified = TransactionDepositVerified.objects.using('transaction_slave')
        check_trans_id = trans_verified.filter(
            transaction_deposit_verified_transit_code=trans_id,
            transaction_deposit_verified_user_related=username,
            transaction_deposit_verified_image_proof_status=True,
        )
        check_approval = trans_verified.filter(
            transaction_deposit_verified_transit_code=trans_id,
            transaction_deposit_verified_user_related=username,
            transaction_deposit_verified_approval_status=True
        )
        if check_trans_id or check_approval: raise except_status_200_data_not_found
        return data

    except(TypeError, ValueError, OverflowError):
        raise except_status_500


async def check_deposit_period(data: dict):
    try:
        payload = data.copy()
        email: Optional[str] = payload.get('email')
        product_type: Optional[str] = payload.get('product_type')
        amount: Optional[int] = payload.get('amount')
        check_email = User.objects.using('default_slave').filter(
            username=email,
        )
        check_member = AccountProfile.objects.using('default_slave').filter(
            account_profile_user_related=email,
            account_profile_cooperative_number__isnull=True
        )
        check_deposit_product = DepositProductMaster.objects.using('funds_slave').filter(
            deposit_product_master_id=product_type
        )
        if not check_email: raise except_status_403
        if check_member: raise except_status_406_not_member
        if not check_deposit_product: raise except_status_200_data_not_found
        if 2500000 > amount: raise except_status_406_minimal_amount
        return data
    except(TypeError, ValueError, OverflowError):
        raise except_status_500


async def check_funds_raise(data: dict):
    # try:
    payload = data.copy()
    email: Optional[str] = payload.get('email')
    code: Optional[str] = payload.get('code')
    amount: Optional[float] = payload.get('amount')
    get_saving: Optional[float] = payload.get('get_saving')
    from_saving_amount: Optional[float] = payload.get('from_saving_amount')
    unique_code: Optional[int] = payload.get('unique_code')
    payment_with: Optional[str] = payload.get('payment_with')

    check_email = User.objects.using('default_slave').filter(
        username=email,
    )
    check_code = LoanApproval.objects.using('funds_master').filter(
        loan_application_spouse_profile_code_related=code
    )
    if not check_email: raise except_status_403
    if not check_code: raise except_status_403
    ## check fullfil amount not yet.
    ## check funds raise code
    return data
    # except(TypeError, ValueError, OverflowError):
    #     raise except_status_500
