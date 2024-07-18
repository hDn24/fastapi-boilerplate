from datetime import datetime, timedelta
from typing import Any

from jose import jwt  # type: ignore
from passlib.context import CryptContext  # type: ignore

from app.configs import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(subject: str | Any, expires_delta: timedelta) -> str:
    """
    Creates a JSON Web Token (JWT) with the given subject and expiration time.

    Args:
        subject: The subject of the JWT.
        expires_delta: The time delta after which the JWT will expire.

    Returns:
        The encoded JWT.
    """
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify if the given plain password matches the hashed password.

    Args:
        plain_password: The plain password to be verified.
        hashed_password: The hashed password to compare against.

    Returns:
        True if the plain password matches the hashed password, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Hashes a given password using the `pwd_context` algorithm.

    Args:
        password: The password to be hashed.

    Returns:
        The hashed password.
    """
    return pwd_context.hash(password)
