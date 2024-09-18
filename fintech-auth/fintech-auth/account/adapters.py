from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from account.schemes import TokenSchemes
from account.models import AccountProfile, AccountUserPin, AccountBankUsers, AccountMemberVerifyStatus
from excep.exceptions import *
from utils.models import Banks, Province, District, SubDistrict

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_data_user(data: dict):
    try:
        payload = data.copy()
        email: Optional[str] = payload.get('email')
        phone_number: Optional[str] = payload.get('phone_number')
        get_email = User.objects.using('default_slave').filter(username=email)
        get_phone = AccountProfile.objects.using('default_slave').filter(account_profile_phone_number=phone_number)

        if get_email:
            raise except_status_200_email_duplicate
        elif get_phone:
            raise except_status_200_phone_duplicate

        return data
    except(TypeError, ValueError, OverflowError):
        raise except_status_500


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    try:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.KEY_HASHED, algorithm=settings.ALGORITHM)
        return encoded_jwt
    except(TypeError, ValueError, OverflowError):
        raise except_status_401


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.KEY_HASHED, algorithms=[settings.ALGORITHM])
        username: Optional[str] = payload.get("sub")
        token_data = TokenSchemes(username=username)
    except JWTError:
        raise except_status_401
    if not User.objects.filter(username=username): raise except_status_401
    return token_data


async def get_validate_user(data: dict):
    try:
        payload = data.copy()
        username: Optional[str] = payload.get('username')
        password: Optional[str] = payload.get('password')
        check = authenticate(username=username, password=password)

        if not check: raise except_status_403_credentials_not_match
        if check.is_staff is True or check.is_superuser is True or check.is_active is False:
            raise except_status_403
        return data
    except(TypeError, ValueError, OverflowError): raise except_status_401


async def check_user_pin(data: dict):
    try:
        payload = data.copy()
        username: Optional[str] = payload.get('username')
        check = AccountUserPin.objects.using('default_slave').filter(account_user_pin_related_user=username)
        check_username = User.objects.using('default_slave').filter(
            username=username,
        )
        if not check_username: raise except_status_403
        if check: raise except_status_200_data_exits
        return data
    except(TypeError, ValueError, OverflowError):
        raise except_status_500


async def check_user_pin_existing(data: dict):
    try:
        payload = data.copy()
        username: Optional[str] = payload.get('username')
        pin: Optional[str] = payload.get('pin')
        check = AccountUserPin.objects.using('default_slave'). \
            filter(account_user_pin_related_user=username,
                   account_user_pin_data=make_password(password=pin, salt=settings.SALTED_PIN, hasher='pbkdf2_sha1'))
        check_username = User.objects.using('default_slave').filter(
            username=username,
        )
        if not check_username: raise except_status_403
        if not check: raise except_status_403_credentials_not_match
        return data
    except(TypeError, ValueError, OverflowError):
        raise except_status_500


async def get_current_holder_number(data: dict):
    try:
        payload = data.copy()
        username: Optional[str] = payload.get('username')
        check_username = User.objects.using('default_slave').filter(
            username=username,
        )
        check = AccountBankUsers.objects.using('default_slave').filter(account_bank_user_related_to_user=username)
        if not check_username: raise except_status_403
        if check: raise except_status_200_data_exits
        return data
    except(TypeError, ValueError, OverflowError):
        raise except_status_500


async def check_approval_profile(data: dict):
    try:
        format = "%Y-%m-%d"
        payload = data.copy()
        username: Optional[str] = payload.get('username')
        nik: Optional[str] = payload.get('ektp_number')
        npwp: Optional[str] = payload.get('npwp_number')
        dob: Optional[str] = payload.get('dob')
        pob: Optional[int] = payload.get('pob')
        province: Optional[int] = payload.get('province')
        district: Optional[int] = payload.get('district')
        sub_district: Optional[int] = payload.get('sub_district')
        check = AccountMemberVerifyStatus.objects.using('default_slave').filter(
            account_member_verify_status_user_related=username, account_member_verify_status_profile_close_to_update=True)
        check_province = Province.objects.using('default_slave').filter(
            Q(province_code=pob) | Q(province_code=province))
        check_district = District.objects.using('default_slave').filter(district_code=district)
        check_sub = SubDistrict.objects.using('default_slave').filter(sub_district_code=sub_district)
        check_format = datetime.strptime(dob, format)
        check_username = User.objects.using('default_slave').filter(
            username=username,
        )
        check_filled = AccountProfile.objects.using('default_slave').filter(
            account_profile_user_related=username, account_profile_filled_status=True
        )
        check_nik = AccountProfile.objects.using('default_slave').filter(account_profile_identification_number=nik)
        check_npwp = AccountProfile.objects.using('default_slave').filter(
            account_profile_tax_identification_number=npwp)

        if not check_username: raise except_status_403
        if check: raise except_status_406_duplicate
        if check_filled: raise except_status_406_was_filled
        if check_nik: raise except_status_406_not_true_data
        if check_npwp: raise except_status_406_not_true_data
        if not check_province: raise except_status_406
        if not check_district: raise except_status_406
        if not check_sub: raise except_status_406
        if not check_format: raise except_status_406
        return data
    except(TypeError, ValueError, OverflowError):
        raise except_status_500


async def check_selfie(data: dict):
    try:
        payload = data.copy()
        username: Optional[str] = payload.get('username')
        check_username = User.objects.using('default_slave').filter(
            username=username,
        )
        check = AccountProfile.objects.using('default_slave') \
            .filter(account_profile_user_related=username,
                    account_profile_selfie__isnull=False,
                    account_profile_selfie_eidentity__isnull=False,
                    account_profile_eidentity__isnull=False,
                    account_profile_enpwp__isnull=False)
        check_2 = AccountMemberVerifyStatus.objects.using('default_slave') \
            .filter(account_member_verify_status_profile_close_to_update=True)
        if not check_username: raise except_status_403
        if check_2 or check: raise except_status_200_data_exits
        return data
    except(TypeError, ValueError, OverflowError):
        raise except_status_500
