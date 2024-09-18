from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional

from django.conf import settings
from django.contrib.auth.models import User
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from deposits.schemes import TokenDataSchemes
from excep.exceptions import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.KEY_HASHED, algorithms=[settings.ALGORITHM])
        username: Optional[str] = payload.get("sub")
        token_data = TokenDataSchemes(username=username)
    except JWTError: raise except_status_401
    if not User.objects.using('default_slave').filter(username=username): raise except_status_401
    return token_data