import threading, logging

import avro.schema
import avro.io
import io
import requests
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from confluent_kafka import Producer

from fastapi import Depends, FastAPI, HTTPException, status, APIRouter, Request

from kafka_connector import prod_conf, on_delivery

from loan.adapters import get_current_user, check_current_loan, update_current_job, update_spouse_data, \
    update_join_income, update_spouse_selfie
from loan.schemes import TokenSchemes, CreateApplicationSchemes, UpdateCurrentJobSchemes, UpdateSpouseDataSchemes, \
    UpdateJoinIncomeSchemes, UpdateSpouseSelfieSchemes
from loan.serialize_avro.create_loan_application import create_loan_application_schema
from loan.serialize_avro.update_current_jobs import update_current_job_schema
from loan.serialize_avro.update_spouse_data import update_spouse_data_schema
from loan.serialize_avro.update_join_income_data import update_join_income_schema
from loan.serialize_avro.update_spouse_selfie_data import update_spouse_selfie_data_schema
from excep.exceptions import except_status_500, except_status_200, except_status_403



router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/get-loan/")
async def get_loan(token: TokenSchemes = Depends(get_current_user)):
    dump = {'data': token.username}
    return dump


@router.get("/get-loan-application/")
async def get_loan_application(token: TokenSchemes = Depends(get_current_user)):
    dump = {'data': token.username}
    return dump


@router.get("/get-loan-history/")
async def get_loan_history(token: TokenSchemes = Depends(get_current_user)):
    dump = {'data': token.username}
    return dump


@router.post("/create-loan-application/")
async def post_create_loan_application(token: str = Depends(get_current_user),
                          data: CreateApplicationSchemes = Depends(check_current_loan)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('member-create-loan-application'))
        record = avro.io.DatumWriter(create_loan_application_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "type_usage": data['type_usage'],
            "amount": data['amount'],
            "installment_month": data['installment_month'],
            "reason": data['reason'],
            "collateral": data['collateral'],
            "proving_collateral": data['proving_collateral'],
            "url": data['url']
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='member-create-loan-application', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info("Success Producing user {} records to topic {}".format(
            data['username'], 'member-create-loan-application'))
        return except_status_200
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "records to topic member-create-loan-application")
        return except_status_500


@router.patch("/update-jobs/")
async def post_update_job_for_loans(token: str = Depends(get_current_user),
                          data: UpdateCurrentJobSchemes = Depends(update_current_job)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('update-current-jobs'))
        record = avro.io.DatumWriter(update_current_job_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "code": data['code'],
            "company_name": data['company_name'],
            "company_phone": data['company_phone'],
            "company_address": data['company_address'],
            "company_address_prov": data['company_address_prov'],
            "company_address_dist": data['company_address_dist'],
            "company_address_sub_dist": data['company_address_sub_dist'],
            "company_address_postal_code": data['company_address_postal_code'],
            "company_establish_from": data['company_establish_from'],
            "company_unit_category": data['company_unit_category'],
            "jobs_started_date": data['jobs_started_date'],
            "jobs_status": data['jobs_status'],
            "jobs_salary": data['jobs_salary'],
            "jobs_placement": data['jobs_placement'],
            "jobs_evident": data['jobs_evident']
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='update-current-jobs', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info(
            "Success Producing user {} records to topic {}".format(data['username'], 'update-current-jobs'))
        return except_status_200
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "records to topic update-current-jobs")
        return except_status_500


@router.patch("/update-spouse/")
async def post_update_spouse_for_loans(token: str = Depends(get_current_user),
                          data: UpdateSpouseDataSchemes = Depends(update_spouse_data)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('update-spouse-data'))
        record = avro.io.DatumWriter(update_spouse_data_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "code": data['code'],
            "guarantor": data['guarantor'],
            "full_name": data['full_name'],
            "status": data['status'],
            "dob": data['dob'],
            "pob": data['pob'],
            "address": data['address'],
            "province": data['province'],
            "district": data['district'],
            "sub_district": data['sub_district'],
            "postal_code": data['postal_code'],
            "phone_number": data['phone_number']
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='update-spouse-data', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info(
            "Success Producing user {} records to topic {}".format(data['username'], 'update-spouse-data'))
        return except_status_200
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "records to topic update-spouse-data")
        return except_status_500


@router.patch("/update-joint-income/")
async def post_update_joint_income(token: str = Depends(get_current_user),
                          data: UpdateJoinIncomeSchemes = Depends(update_join_income)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('update-join-income'))
        record = avro.io.DatumWriter(update_join_income_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "code": data['code'],
            "join_income": data['join_income'],
            "company_name": data['company_name'],
            "company_phone": data['company_phone'],
            "company_address_prov": data['company_address_prov'],
            "company_address_district": data['company_address_district'],
            "company_address_sub_district": data['company_address_sub_district'],
            "company_address": data['company_address'],
            "company_postal_code": data['company_postal_code'],
            "company_establish_from": data['company_establish_from'],
            "company_category": data['company_category'],
            "job_started_date": data['job_started_date'],
            "job_status": data['job_status'],
            "job_evident": data['job_evident'],
            "salary": data['salary'],
            "placement": data['placement']
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='update-join-income', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info(
            "Success Producing user {} records to topic {}".format(data['username'], 'update-join-income'))
        return except_status_200
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "records to topic update-spouse-data")
        return except_status_500


@router.patch("/update-spouse-selfie/")
async def post_update_spouse_selfie(token: str = Depends(get_current_user),
                          data: UpdateSpouseSelfieSchemes = Depends(update_spouse_selfie)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('update-spouse-selfie'))
        record = avro.io.DatumWriter(update_spouse_selfie_data_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "code": data['code'],
            "selfie": data['selfie'],
            "selfie_eidentity": data['selfie_eidentity'],
            "eidentity": data['eidentity'],
            "enpwp": data['enpwp'],
            "family_card": data['family_card'],
            "marriage_certificate": data['marriage_certificate']
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='update-spouse-selfie', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info(
            "Success Producing user {} records to topic {}".format(data['username'], 'update-spouse-selfie'))
        return except_status_200

    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                 "records to topic update-spouse-selfie")
    return except_status_500
