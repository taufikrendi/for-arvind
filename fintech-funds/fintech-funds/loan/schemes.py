from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class TokenSchemes(BaseModel):
    username: str


class CreateApplicationSchemes(BaseModel):
    email: str
    type_usage: str
    amount: float
    installment_month: int
    reason: str
    collateral: str
    proving_collateral: str
    url: Optional[str] = None


class UpdateCurrentJobSchemes(BaseModel):
    email: str
    code: str
    company_name: str
    company_phone: str
    company_address: str
    company_address_prov: str
    company_address_dist: str
    company_address_sub_dist: str
    company_address_postal_code: str
    company_establish_from: str
    company_unit_category: str
    jobs_started_date: str
    jobs_status: str
    jobs_salary: float
    jobs_placement: str
    jobs_evident: str


class UpdateSpouseDataSchemes(BaseModel):
    email: str
    code: str
    guarantor: str
    full_name: str
    status: str
    dob: str
    pob: str
    address: str
    province: str
    district: str
    sub_district: str
    postal_code: str
    phone_number: str


class UpdateJoinIncomeSchemes(BaseModel):
    email: str
    code: str
    join_income: str
    company_name: Optional[str] = None
    company_phone: Optional[str] = None
    company_address_prov: Optional[str] = None
    company_address_district: Optional[str] = None
    company_address_sub_district: Optional[str] = None
    company_address: Optional[str] = None
    company_postal_code: Optional[str] = None
    company_establish_from: Optional[str] = None
    company_category: Optional[str] = None
    job_started_date: Optional[str] = None
    job_status: Optional[str] = None
    job_evident: Optional[str] = None
    salary: Optional[float] = None
    placement: Optional[str] = None


class UpdateSpouseSelfieSchemes(BaseModel):
    email: str
    code: str
    selfie: str
    selfie_eidentity: str
    eidentity: str
    enpwp: str
    family_card: str
    marriage_certificate: Optional[str] = None