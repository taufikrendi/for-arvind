import threading, logging
from typing import List
import time

from confluent_kafka import Producer

import avro.schema
import avro.io
import io

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.conf import settings

from fastapi import Depends, FastAPI, HTTPException, status, APIRouter, Request

from kafka_connector import prod_conf, on_delivery

from account.adapters import *
from account.models import AccountBankUsers
from account.schemes import *
from account.serialize_avro.registrations import registration_schema
from account.serialize_avro.forgot_password import forgot_password_schema
from account.serialize_avro.change_password import change_password_schema
from account.serialize_avro.set_pin import set_pin_schema
from account.serialize_avro.registered_bank_account import registered_bank_account_schema
from account.serialize_avro.change_pin import change_pin_schema
from account.serialize_avro.profile_filled import account_profile_schema
from account.serialize_avro.selfie_filled import selfie_filled_schema

from excep.exceptions import except_status_500, except_status_200, except_status_403, except_status_503,\
    except_status_200_request_forgot_password

router = APIRouter()
logger = logging.getLogger(__name__)
global data_produce


@router.post("/registrations/")
async def post_registered_account(data: UserRegistrationSchemes = Depends(get_current_data_user)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('member-registrations'))
        record = avro.io.DatumWriter(registration_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "email": data['email'],
            "first_name": data['first_name'],
            "password": make_password(password=data['password'], salt=settings.SALTED_PASSWORD, hasher='pbkdf2_sha256'),
            "phone_number": data['phone_number'],
            "agreement": data['agreement']
        }, encoder)
        data_record = bytes_writer.getvalue()
        record.email = data['email']
        data_produce.produce(topic='member-registrations', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info(
            "Success Producing user {} records to topic {}".format(record.email, 'member-registrations'))
        return except_status_200
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "records to topic member-registrations")
        return except_status_500


@router.post("/forgot-password/")
async def post_forgot_password(request: Request, data: TokenSchemes):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('member-forgot-password'))
        record = avro.io.DatumWriter(forgot_password_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data.username,
            "ip": request.client.host
        }, encoder)
        data_record = bytes_writer.getvalue()
        record.email = data.username
        data_produce.produce(topic='member-forgot-password', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info("Success Producing user {} records to topic {}".format(record.email, 'member-forgot-password'))
        return except_status_200_request_forgot_password
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "records to topic member-forgot-password")
        return except_status_500


@router.patch("/change-password/")
async def patch_change_password(request: Request, token: str = Depends(get_current_user),
        data: ChangePassSchemes = Depends(get_validate_user)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('member-change-password'))
        record = avro.io.DatumWriter(change_password_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "ip": request.client.host,
            "new_pwd": make_password(password=data['new_pwd'], salt=settings.SALTED_PASSWORD, hasher='pbkdf2_sha256')
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='member-change-password', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info("Success Producing user {} records to topic {}".format(token.username, 'member-change-password'))
        return except_status_200
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "records to topic member-forgot-password")
        raise except_status_500


@router.post("/set-pin/")
async def post_set_pin(
        request: Request, token: str = Depends(get_current_user),
        data: SetPinSchemes = Depends(check_user_pin)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('member-set-pin'))
        record = avro.io.DatumWriter(set_pin_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "ip": request.client.host,
            "pin": make_password(password=str(data['pin']), salt=settings.SALTED_PIN, hasher='pbkdf2_sha1'),
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='member-set-pin', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info("Success Producing user {} records to topic {}".format(data['username'], 'member-set-pin'))
        return except_status_200
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "records to topic member-set-pin")
        raise except_status_500


@router.patch("/set-pin/")
async def patch_set_pin(
        request: Request,  token: str = Depends(get_current_user),
        data: ChangePinSchemes = Depends(check_user_pin_existing)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('member-change-pin'))
        record = avro.io.DatumWriter(change_pin_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "ip": request.client.host,
            "pin": make_password(password=str(data['pin']), salt=settings.SALTED_PIN, hasher='pbkdf2_sha1'),
            "new_pin": make_password(password=str(data['new_pin']), salt=settings.SALTED_PIN, hasher='pbkdf2_sha1')
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='member-change-pin', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info("Success Producing user {} records to topic {}".format(data['username'], 'member-change-pin'))
        return except_status_200
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "records to topic member-change-pin")
        raise except_status_500


@router.post("/bank-account/register/")
async def post_registered_bank_account(token: str = Depends(get_current_user),
        data: AccountBankSchemes = Depends(get_current_holder_number)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('member-register-account-bank'))
        record = avro.io.DatumWriter(registered_bank_account_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "holder_bank_code": data['holder_bank_code'],
            "holder_number": data['holder_number'],
            "holder_name": data['holder_name']
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='member-register-account-bank', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info("Success Producing user {} records to topic {}".format(data['username'], 'member-register-account-bank'))
        return except_status_200
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "records to topic member-register-account-bank")
        raise except_status_500


@router.get("/bank-account/register/", response_model=List[GetAccountBankSchemes])
async def get_bank_account_detail(token: str = Depends(get_current_user)):
    try:
        dump = list(AccountBankUsers.objects.using('default_slave')\
                    .filter(account_bank_user_related_to_user=token.username)\
                    .extra(
                        select={'bank_name': 'utils_banks.bank_name',
                                'holder_name': 'account_bank_user_name',
                                'holder_number': 'account_bank_user_number'},
                        tables=['utils_banks'],
                        where=['account_accountbankusers.account_bank_user_related_to_bank=utils_banks.bank_code']))
        return dump
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Get Data Bank Account Detail")
        return except_status_500


@router.patch("/patch-profile/")
async def patch_profile(token: str = Depends(get_current_user),
        data: AccountProfileSchemes = Depends(check_approval_profile)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('member-profile-filled'))
        record = avro.io.DatumWriter(account_profile_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "ektp_number": data['ektp_number'],
            "npwp_number": data['npwp_number'],
            "dob": data['dob'],
            "pob": int(data['pob']),
            "sex": data['sex'],
            "address": data['address'],
            "province": int(data['province']),
            "district": int(data['district']),
            "sub_district": int(data['sub_district'])
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='member-profile-filled', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info("Success Producing user {} records to topic {}".format(data['username'], 'member-profile-filled'))
        return except_status_200
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "records to topic member-profile-filled")
        raise except_status_500


@router.get("/patch-profile/", response_model=List[GetAccountProfileSchemes])
async def get_profile_detail(token: TokenSchemes = Depends(get_current_user)):
    try:
        dump = list(User.objects.using('default_slave').filter(username=token.username)\
                .extra(
                select={'cooperative_number':'account_accountprofile.account_profile_cooperative_number',
                        'phone_number': 'account_accountprofile.account_profile_phone_number'},
                tables=['account_accountprofile'],
                where=['account_accountprofile.account_profile_user_related=auth_user.username'])
            )
        return dump
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error get Profile Detail")
        return except_status_500


@router.patch("/patch-selfie/")
async def patch_selfie(token: str = Depends(get_current_user),
                       data: SelfieFilledSchemes = Depends(check_selfie)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('member-selfie-filled'))
        record = avro.io.DatumWriter(selfie_filled_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "selfie": data['selfie'],
            "selfie_ektp": data['selfie_ektp'],
            "ektp": data['ektp'],
            "enpwp": data['enpwp']
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='member-selfie-filled', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info(
            "Success Producing user {} records to topic {}".format(data['username'], 'member-selfie-filled'))
        return except_status_200
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "records to topic member-selfie-filled")
        return except_status_500


@router.get("/patch-selfie/", response_model=List[GetAccountSelfie])
async def get_selfie(token: TokenSchemes = Depends(get_current_user)):
    try:
        dump = list(User.objects.using('default_slave').filter(username=token.username)\
            .extra(
                select={'selfie': 'account_accountprofile.account_profile_selfie'},
                tables=['account_accountprofile'],
                where=['account_accountprofile.account_profile_user_related=auth_user.username'])
            )
        return dump
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Get Data Selfie")
        return except_status_500

