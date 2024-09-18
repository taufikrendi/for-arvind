from typing import List
import logging

from fastapi import Depends, FastAPI, HTTPException, status, APIRouter, Request

from deposits.adapters import get_current_user
from deposits.models import DepositMemberMandatory, DepositMemberPrincipal
from deposits.schemes import TokenDataSchemes, GetDepositSchemes
from excep.exceptions import *

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/get-deposit/", response_model=List[GetDepositSchemes])
async def get_deposit(data: TokenDataSchemes = Depends(get_current_user)):
    try:
        dump = list(DepositMemberMandatory.objects.filter(
            deposit_member_mandatory_user_related=data.username
        ).extra(
            select={'email': 'deposits_depositmemberprincipal.deposit_member_principal_user_related',
                    'principal_amount':
                        'deposits_depositmemberprincipal.deposit_member_principal_payment_principal_amount'},
            tables=['deposits_depositmemberprincipal'],
            where=['deposits_depositmemberprincipal.deposit_member_principal_user_related='
                   'deposits_depositmembermandatory.deposit_member_mandatory_user_related']
        ).order_by('-deposit_member_mandatory_created_date')[:20])
        return dump
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Get Data Deposit")
        return except_status_500


@router.get("/get-residual-income/")
async def get_residual_income(data: TokenDataSchemes = Depends(get_current_user)):
    dump = {'data': data.username}
    return dump
