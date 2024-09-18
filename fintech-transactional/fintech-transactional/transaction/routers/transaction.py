import threading, logging
from typing import List

from confluent_kafka import Producer

import avro.schema
import avro.io
import io

from fastapi import Depends, FastAPI, HTTPException, status, APIRouter, Request

from kafka_connector import prod_conf, on_delivery

from transaction.adapters import *
from transaction.schemes import *
from transaction.models import *
from transaction.serialize_avro.create_transactions import create_transactions_schema
from transaction.serialize_avro.proving_transactions import proving_transactions_schema
from transaction.serialize_avro.create_deposit_time import create_deposit_time_schema
from transaction.serialize_avro.create_funds_raise_schema import create_funds_raise_schema
from excep.exceptions import *

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/create-transaction/")
async def post_create_transaction(
        token: str = Depends(get_current_user),
        data: CreateTransactionsSchemes = Depends(check_before_trans)
):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('member-create-trans'))
        record = avro.io.DatumWriter(create_transactions_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "unique_code": data['unique_code'],
            "amount": data['amount'],
            "payment_with": data['payment_with']
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='member-create-trans', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info("Success Producing user {} records to topic {}".format(data['username'], 'member-create-trans'))
        return except_status_200
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "records to topic member-create-trans")
        return except_status_500


@router.get("/transaction-history/", response_model=List[GetOnGoingTransactionSchemes])
async def get_transactions_history(token: str = Depends(get_current_user),):
    try:
        dump = list(TransactionDepositVerified.objects.filter(
            transaction_deposit_verified_user_related=token.username
        ).extra(
            select={'amount':
                        'transaction_transactiondeposittransit.transaction_deposit_transit_gt_amount',
                    'transaction_type':
                        'transaction_transactiondeposittransit.transaction_deposit_transit_type',
                    'created_date':
                        'transaction_transactiondeposittransit.transaction_deposit_transit_created_date'},
            tables=['transaction_transactiondeposittransit'],
            where=['transaction_transactiondeposittransit.transaction_deposit_transit_code='
                   'transaction_transactiondepositverified.transaction_deposit_verified_transit_code']
        ).order_by('-transaction_deposit_verified_created_date')[:20])
        return dump
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Get Data Transaction History")
        return except_status_500


@router.post("/prove-transaction/")
async def post_prove_transaction(
        token: str = Depends(get_current_user),
        data: ProvingTransactionsSchemes = Depends(check_proving_trans)
):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('member-proving-transactions'))
        record = avro.io.DatumWriter(proving_transactions_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "trans_id": data['trans_id'],
            "image": data['image']
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='member-proving-transactions', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info("Success Producing user {} records to topic {}".format(data['username'], 'member_proving_transactions'))
        return except_status_200
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Get Data Transaction History")
        return except_status_500


@router.post("/create-transaction-deposit-period/")
async def post_create_deposit_period(token: str = Depends(get_current_user),
                                     data: DepositPeriodSchemes = Depends(check_deposit_period)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('member-create-deposit-time'))
        record = avro.io.DatumWriter(create_deposit_time_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "product_type": data['product_type'],
            "amount": data['amount'],
            "period_base": data['period_base'],
            "payment_with": data['payment_with']
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='member-create-deposit-time', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info(
            "Success Producing user {} records to topic {}".format(data['username'], 'member-create-deposit-time'))
        return except_status_200
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Get Data Transaction History")
        return except_status_500


@router.post("/funds-raise/")
async def post_funds_raise(token: str = Depends(get_current_user),
         data: FundRaiseSchemes = Depends(check_funds_raise)):
    try:
        data_produce = Producer(prod_conf)
        logger.info("Producing user records to topic {}".format('member-create-funds-raise'))
        record = avro.io.DatumWriter(create_funds_raise_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        record.write({
            "username": data['username'],
            "code": data['code'],
            "amount": data['amount'],
            "get_saving": data['get_saving'],
            "from_saving_amount": data['from_saving_amount'],
            "unique_code": data['unique_code'],
            "payment_with": data['payment_with']
        }, encoder)
        data_record = bytes_writer.getvalue()
        if token.username != data['username']:
            raise except_status_403
        data_produce.produce(topic='member-create-funds-raise', value=data_record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
        threading.Thread(target=data_produce.poll(1))
        logger.info(
            "Success Producing user {} records to topic {}".format(data['username'], 'member-create-funds-raise'))
        return except_status_200

    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Get Data Transaction History")
        return except_status_500
