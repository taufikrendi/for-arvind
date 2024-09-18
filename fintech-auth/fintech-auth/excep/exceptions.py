from fastapi import HTTPException, status


except_status_200 = HTTPException(
    status_code=200,
    detail="Process Success!",
    headers={"Content-Type": "application/json"},
)

except_status_200_request_forgot_password = HTTPException(
    status_code=200,
    detail="Process Success! If your Email Was Registered You Will Got Link For Changing Password!",
    headers={"Content-Type": "application/json"},
)

except_status_200_data_exits = HTTPException(
    status_code=200,
    detail="Data Exist!",
    headers={"Content-Type": "application/json"},
)

except_status_200_data_not_found = HTTPException(
    status_code=200,
    detail="Data not Found!",
    headers={"Content-Type": "application/json"},
)

except_status_200_email_duplicate = HTTPException(
    status_code=200,
    detail="Wrong E-Mail",
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

except_status_403_credentials_not_match = HTTPException(
    status_code=403,
    detail="Not Match",
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

except_status_406_was_filled = HTTPException(
    status_code=406,
    detail="Status Menunggu Persetujuan!",
    headers={"Content-Type": "application/json"},
)

except_status_406_duplicate = HTTPException(
    status_code=406,
    detail="Data Tidak Bisa Dirubah!",
    headers={"Content-Type": "application/json"},
)

except_status_406_not_true_data = HTTPException(
    status_code=406,
    detail="Pastikan Data Anda Benar!",
    headers={"Content-Type": "application/json"},
)

except_status_500 = HTTPException(
    status_code=500,
    detail="Process Error!",
    headers={"Content-Type": "application/json"},
)

except_status_503 = HTTPException(
    status_code=503,
    detail="Service Unavailable",
    headers={"Content-Type": "application/json"},
)