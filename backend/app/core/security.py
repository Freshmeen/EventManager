from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from uuid import uuid4

ACCESS_SECRET_KEY = "SALT1"
REFRESH_SECRET_KEY = "SALT2"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 10
REFRESH_TOKEN_EXPIRE_DAYS = 30


def create_access_token(subject: str) -> str:
    payload = {
        "sub": subject,
        "type": "access",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(payload, ACCESS_SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(subject: str) -> str:
    payload = {
        "sub": subject,
        "jti": str(uuid4()),
        "type": "refresh",
        "exp": datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
    }
    return jwt.encode(payload, REFRESH_SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> str | None:
    try:
        payload = jwt.decode(token, ACCESS_SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "access":
            return None
        return payload["sub"]
    except JWTError:
        return None


def decode_refresh_token(token: str) -> tuple[str, str] | None:
    try:
        payload = jwt.decode(token, REFRESH_SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "refresh":
            return None
        return payload["sub"], payload["jti"]
    except JWTError:
        return None
