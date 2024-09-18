from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from account.models import AccountProfile
from loan.schemes import TokenSchemes
from loan.models import LoanApproval, LoanApplication
from utils.models import Province, District, SubDistrict
from excep.exceptions import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.KEY_HASHED, algorithms=[settings.ALGORITHM])
        username: Optional[str] = payload.get("sub")
        token_data = TokenSchemes(username=username)
    except JWTError: raise except_status_401
    if not User.objects.using('default_slave').filter(username=username): raise except_status_401
    return token_data


async def check_current_loan(data: dict):
    try:
        payload = data.copy()
        email: Optional[str] = payload.get('email')
        type_usage: Optional[str] = payload.get('type_usage')
        amount: Optional[float] = payload.get('amount')
        installment_month: Optional[int] = payload.get('installment_month')
        reason: Optional[str] = payload.get('reason')
        collateral: Optional[str] = payload.get('collateral')
        proving_collateral: Optional[str] = payload.get('proving_collateral')
        url: Optional[str] = payload.get('url')
        check_email = User.objects.using('default_slave').filter(
            username=email,
        )
        if not check_email: raise except_status_403
        not_finished = LoanApproval.objects.using('funds_slave').filter(
            loan_approval_user_related=email, loan_approval_finish_status=False, loan_approval_status='Approve'
        )
        check_member = AccountProfile.objects.using('default_slave').filter(
            account_profile_user_related=email,
            account_profile_cooperative_number__isnull=True
        )
        check_applications = LoanApproval.objects.using('funds_slave').filter(
            loan_approval_user_related=email, loan_approval_status='On Manual Verify'
        )
        if check_member: raise except_status_406_not_member
        if not_finished: raise except_status_406_not_finish_loan
        if check_applications: raise except_status_406_still_on_application
        return data
    except(TypeError, ValueError, OverflowError): raise except_status_500


async def update_current_job(data: dict):
    try:
        format = "%Y-%m-%d"
        payload = data.copy()
        email: Optional[str] = payload.get('email')
        code: Optional[str] = payload.get('code')
        company_name: Optional[str] = payload.get('company_name')
        company_phone: Optional[str] = payload.get('company_phone')
        company_address: Optional[str] = payload.get('company_address')
        company_address_prov: Optional[str] = payload.get('company_address_prov')
        company_address_dist: Optional[str] = payload.get('company_address_dist')
        company_address_sub_dist: Optional[str] = payload.get('company_address_sub_dist')
        company_address_postal_code: Optional[str] = payload.get('company_address_postal_code')
        company_establish_from: Optional[str] = payload.get('company_establish_from')
        company_unit_category: Optional[str] = payload.get('company_unit_category')
        jobs_started_date: Optional[str] = payload.get('jobs_started_date')
        jobs_status: Optional[str] = payload.get('jobs_status')
        jobs_salary: Optional[float] = payload.get('jobs_salary')
        jobs_placement: Optional[str] = payload.get('jobs_placement')
        jobs_evident: Optional[str] = payload.get('jobs_evident')
        check_email = User.objects.using('default_slave').filter(
            username=email,
        )
        check_code = LoanApplication.objects.using('funds_slave').filter(
            loan_application_code_related=code
        )
        check_province = Province.objects.using('default_slave').filter(province_code=company_address_prov)
        check_district = District.objects.using('default_slave').filter(district_code=company_address_dist)
        check_sub = SubDistrict.objects.using('default_slave').filter(sub_district_code=company_address_sub_dist)
        check_format = datetime.strptime(jobs_started_date, format)
        if not check_email: raise except_status_403
        if not check_code: raise except_status_403
        if not check_province: raise except_status_406
        if not check_district: raise except_status_406
        if not check_sub: raise except_status_406
        if not check_format: raise except_status_406
        return data
    except(TypeError, ValueError, OverflowError):raise except_status_500


async def update_spouse_data(data: dict):
    try:
        format = "%Y-%m-%d"
        payload = data.copy()
        email: Optional[str] = payload.get('email')
        code: Optional[str] = payload.get('code')
        guarantor: Optional[str] = payload.get('guarantor')
        full_name: Optional[str] = payload.get('full_name')
        status: Optional[str] = payload.get('status')
        dob: Optional[str] = payload.get('dob')
        pob: Optional[str] = payload.get('pob')
        address: Optional[str] = payload.get('address')
        province: Optional[str] = payload.get('province')
        district: Optional[str] = payload.get('district')
        sub_district: Optional[str] = payload.get('sub_district')
        postal_code: Optional[str] = payload.get('postal_code')
        phone_number: Optional[str] = payload.get('phone_number')
        check_email = User.objects.using('default_slave').filter(
            username=email,
        )
        check_code = LoanApplication.objects.using('funds_slave').filter(
            loan_application_code_related=code
        )
        check_province = Province.objects.using('default_slave').filter(Q(province_code=pob) | Q(province_code=province))
        check_district = District.objects.using('default_slave').filter(district_code=district)
        check_sub = SubDistrict.objects.using('default_slave').filter(sub_district_code=sub_district)
        check_format = datetime.strptime(dob, format)
        if not check_email: raise except_status_403
        if not check_code: raise except_status_403
        if not check_province: raise except_status_406
        if not check_district: raise except_status_406
        if not check_sub: raise except_status_406
        if not check_format: raise except_status_406
        return data
    except(TypeError, ValueError, OverflowError):raise except_status_500


async def update_join_income(data: dict):
    # try:
    format = "%Y-%m-%d"
    payload = data.copy()
    email: Optional[str] = payload.get('email')
    code: Optional[str] = payload.get('code')
    join_income: Optional[str] = payload.get('join_income')
    company_name: Optional[str] = payload.get('company_name')
    company_phone: Optional[str] = payload.get('company_phone')
    company_address_prov: Optional[str] = payload.get('company_address_prov')
    company_address_district: Optional[str] = payload.get('company_address_district')
    company_address_sub_district: Optional[str] = payload.get('company_address_sub_district')
    company_address: Optional[str] = payload.get('company_address')
    company_postal_code: Optional[str] = payload.get('company_postal_code')
    company_establish_from: Optional[str] = payload.get('company_establish_from')
    company_category: Optional[str] = payload.get('company_category')
    job_started_date:  Optional[str] = payload.get('job_started_date')
    job_status: Optional[str] = payload.get('job_status')
    job_evident: Optional[str] = payload.get('job_evident')
    salary: Optional[float] = payload.get('salary')
    placement: Optional[float] = payload.get('placement')

    check_email = User.objects.using('default_slave').filter(
        username=email,
    )
    check_code = LoanApplication.objects.using('funds_slave').filter(
        loan_application_code_related=code
    )
    if company_address_prov is None:
        check_province = Province.objects.using('default_slave').filter(province_code=company_address_prov)
        if not check_province: raise except_status_406
    if company_address_district is None:
        check_district = District.objects.using('default_slave').filter(district_code=company_address_district)
        if not check_district: raise except_status_406
    if company_address_sub_district is None:
        check_sub = SubDistrict.objects.using('default_slave').filter(sub_district_code=company_address_sub_district)
        if not check_sub: raise except_status_406
    if job_started_date is None:
        check_format = datetime.strptime(job_started_date, format)
        if not check_format: raise except_status_406
    if not check_email: raise except_status_403
    if not check_code: raise except_status_403
    return data
    # except(TypeError, ValueError, OverflowError):raise except_status_500


async def update_spouse_selfie(data: dict):
    # try:
    payload = data.copy()
    email: Optional[str] = payload.get('email')
    code: Optional[str] = payload.get('code')
    selfie: Optional[str] = payload.get('selfie')
    selfie_eidentity: Optional[str] = payload.get('selfie_eidentity')
    eidentity: Optional[str] = payload.get('eidentity')
    enpwp: Optional[str] = payload.get('enpwp')
    family_card: Optional[str] = payload.get('family_card')
    marriage_certificate: Optional[str] = payload.get('marriage_certificate')
    check_email = User.objects.using('default_slave').filter(
        username=email,
    )
    check_code = LoanApplication.objects.using('funds_slave').filter(
        loan_application_code_related=code
    )
    check_province = Province.objects.using('default_slave').filter(Q(province_code=pob) | Q(province_code=province))
    check_district = District.objects.using('default_slave').filter(district_code=district)
    check_sub = SubDistrict.objects.using('default_slave').filter(sub_district_code=sub_district)
    if not check_email: raise except_status_403
    if not check_code: raise except_status_403
    if not check_province: raise except_status_406
    if not check_district: raise except_status_406
    if not check_sub: raise except_status_406
    return data
    # except(TypeError, ValueError, OverflowError):raise except_status_500