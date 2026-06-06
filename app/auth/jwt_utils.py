import jwt
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
from os import getenv
from typing import Any
from fastapi import HTTPException

load_dotenv()

SECRET_KEY: str =  getenv("SECRET_KEY")

# HS256
ALGORITHM: str = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def create_token(username: str) -> str:
    payload: dict[str, Any] = {
        "sub": username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    
    return jwt.encode(
        payload,
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )

def verify_token(token: str):
    try:
        decoded_payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_payload.get("sub")

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token is expired")    
    except jwt.InvalidTokenError:
        raise Exception(status_code=401, detail="Invalid token")
