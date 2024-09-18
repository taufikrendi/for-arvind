import rocksdb, logging
from datetime import timedelta
from django.conf import settings
from django.contrib.auth import authenticate

from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from account.adapters import create_access_token, get_current_user, get_validate_user
from account.schemes import TokenSchemes, AuthSchemes
from excep.exceptions import *

router = APIRouter()

opts = rocksdb.Options()
opts.create_if_missing = True
opts.max_open_files = 300000
opts.write_buffer_size = 67108864
opts.max_write_buffer_number = 3
opts.target_file_size_base = 67108864

opts.table_factory = rocksdb.BlockBasedTableFactory(
    filter_policy=rocksdb.BloomFilterPolicy(10),
    block_cache=rocksdb.LRUCache(2 * (1024 ** 3)),
    block_cache_compressed=rocksdb.LRUCache(500 * (1024 ** 2)))

db = rocksdb.DB("rocks.db", opts)
logger = logging.getLogger(__name__)


@router.post("/auth/")
async def post_token_access(data: AuthSchemes = Depends(get_validate_user)):
    try:
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": data['username']},
            expires_delta=access_token_expires
        )

        transform_1 = bytes(data['username'], 'utf-8')
        transform_2 = bytes(access_token, 'utf-8')

        db.put(transform_1, transform_2)
        return except_status_200
    except (TypeError, ValueError, OverflowError, BufferError):
        logger.error("TypeError or Value or Overflow or Buffer error Producing"
                     "on API post_token_access")
        return except_status_500


@router.post("/token/get/")
async def post_token_auth(username: TokenSchemes):
    try:
        data = bytes(str(username.username), 'utf8')
        transform = db.get(data)

        return HTTPException(status_code=200, detail={"access_token": transform}, headers={"WWW-Authenticate": "Bearer"})
    except (TypeError, ValueError, OverflowError):
        return except_status_500


@router.post("/token/revoke/")
async def post_revoke_token(data: TokenSchemes = Depends(get_current_user)):
    try:
        data = bytes(str(data.username), 'utf8')
        get_token = db.get(data)
        blocked = bytes(str('VadQssw5c'), 'utf8')
        make = bytes(str(''), 'utf8').join([get_token, blocked])
        db.delete(data)
        db.put(data,make)
        return except_status_200
    except (TypeError, ValueError, OverflowError):
        return except_status_500


@router.post("/token/refresh/")
async def post_refresh_token(data: TokenSchemes = Depends(get_current_user)):
    try:
        await post_revoke_token(data)
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": data.username},
            expires_delta=access_token_expires
        )
        data = bytes(str(data.username), 'utf8')
        token_transform = bytes(str(access_token), 'utf8')
        db.delete(data)
        db.put(data,token_transform)
        new_token = db.get(data)

        return HTTPException(status_code=200, detail={"access_token": new_token}, headers={"WWW-Authenticate": "Bearer"},)
    except (TypeError, ValueError, OverflowError):
        return except_status_500


