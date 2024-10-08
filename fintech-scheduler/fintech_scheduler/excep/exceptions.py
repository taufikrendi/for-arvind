from fastapi import HTTPException, status


except_status_200 = HTTPException(
    status_code=200,
    detail="Process Success!",
    headers={"Content-Type": "application/json"},
)

except_status_200_email_duplicate = HTTPException(
    status_code=200,
    detail="Wrong E-Mail",
    headers={"Content-Type": "application/json"},
)

except_status_200_data_not_found = HTTPException(
    status_code=200,
    detail="Data not Found!",
    headers={"Content-Type": "application/json"},
)

except_status_200_phone_duplicate = HTTPException(
    status_code=200,
    detail="Wrong Phone",
    headers={"Content-Type": "application/json"},
)

except_status_401 = HTTPException(
    status_code=401,
    detail="Unauthorized!",
    headers={"WWW-Authenticate": "Bearer"},
)

except_status_403 = HTTPException(
    status_code=403,
    detail="Forbidden Access!",
    headers={"WWW-Authenticate": "Bearer"},
)

except_status_404 = HTTPException(
    status_code=404,
    detail="Page Not Found!",
    headers={"Content-Type": "application/json"},
)

except_status_406 = HTTPException(
    status_code=406,
    detail="Format Error!",
    headers={"Content-Type": "application/json"},
)
except_status_500 = HTTPException(
    status_code=500,
    detail="Process Error!",
    headers={"Content-Type": "application/json"},
)