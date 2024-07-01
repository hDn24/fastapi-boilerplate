from datetime import timedelta
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.cruds import login as crud
from app.api.schemas.token import Token
from app.api.schemas.user import UserOut
from app.api.utils import security
from app.configs import settings
from app.database import get_db
from app.dependencies import CurrentUser

router = APIRouter()


@router.post("/login/access-token")
def create_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Session = Depends(get_db),
) -> Token:
    user = crud.authenticate(session, form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(access_token=security.create_access_token(user.id, expires_delta=access_token_expires))


@router.post("/login/test-token", response_model=UserOut)
def test_token(current_user: CurrentUser) -> Any:
    """
    Test access token
    """
    return current_user
