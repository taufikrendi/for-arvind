import logging

from fastapi import Depends, FastAPI, HTTPException, status, APIRouter, Request

from deposits.adapters import get_current_user
from deposits.schemes import TokenDataSchemes


router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/get-loan/")
async def get_loan(data: TokenDataSchemes = Depends(get_current_user)):
    dump = {'data': data.username}
    return dump


@router.get("/get-loan-submission/")
async def get_loan_submission(data: TokenDataSchemes = Depends(get_current_user)):
    dump = {'data': data.username}
    return dump


@router.get("/get-loan-history/")
async def get_loan_history(data: TokenDataSchemes = Depends(get_current_user)):
    dump = {'data': data.username}
    return dump


@router.post("/loan-submission/")
async def post_submission(data: TokenDataSchemes = Depends(get_current_user)):
    dump = {'data': data.username}
    return dump