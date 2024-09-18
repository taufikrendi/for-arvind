import logging

from fastapi import Depends, FastAPI, HTTPException, status, APIRouter, Request

from account.adapters import get_current_user
from account.schemes import TokenSchemes

from utils.models import Banks, Province, District, SubDistrict


router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/get/banks/{name}")
async def get_banks(name: str, data: TokenSchemes = Depends(get_current_user)):
    data = list(Banks.objects.using('default_slave').filter(bank_name__icontains=name).
                values('bank_code', 'bank_name')[:10])
    results = [{'bank_code': cards['bank_code'], 'bank_name': cards['bank_name']} for cards in data]
    if not results:
        return {'data': 'data not found'}
    return results


@router.get("/get/provinces/{name}")
async def get_provinces(name: str, data: TokenSchemes = Depends(get_current_user)):
    data = list(Province.objects.using('default_slave').filter(province_name__icontains=name).
                values('province_code', 'province_name')[:10])
    results = [{'province_code': cards['province_code'], 'province_name': cards['province_name']} for cards in data]
    if not results:
        return {'data': 'data not found'}
    return results


@router.get("/get/districts/{id}")
async def get_districts(id: str, data: TokenSchemes = Depends(get_current_user)):
    data = list(District.objects.using('default_slave').filter(district_relation=id).
                values('district_code', 'district_name')[:10])
    results = [{'district_code': cards['district_code'], 'district_name': cards['district_name']} for cards in data]
    if not results:
        return {'data': 'data not found'}
    return results


@router.get("/get/sub-districts/{id}")
async def get_sub_districts(id: str, data: TokenSchemes = Depends(get_current_user)):
    data = list(SubDistrict.objects.using('default_slave').filter(sub_district_relation=id).
                values('sub_district_name')[:10])
    results = [{'sub_district_name': cards['sub_district_name']} for cards in data]
    if not results:
        return {'data': 'data not found'}
    return results