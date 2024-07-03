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

router = APIRouter(prefix="/login", tags=["login"])


@router.post("/access-token")
def create_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
) -> Token:
    """
    Create an access token for the user.

    Args:
        form_data: The form data containing the user's username and password.
        db: The database session. Defaults to the session obtained from the `get_db` dependency.

    Returns:
        The access token for the user.

    Raises:
        HTTPException: If the username or password is incorrect or the user is inactive.
    """
    # Authenticate the user
    user = crud.authenticate(db, form_data.username, form_data.password)

    # Check if the user exists and is active
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    elif not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not active")

    # Create the access token with the user's ID and expiration time
    access_token_expiration = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(user.id, expires_delta=access_token_expiration)

    # Return the access token as a response
    return Token(access_token=access_token)


@router.post("/test-token", response_model=UserOut)
def test_token(current_user: CurrentUser) -> Any:
    """
    This endpoint is used to test the validity of the access token by returning the current user object.

    Args:
        current_user: The current user object obtained from the dependency.

    Returns:
        Any: The current user object.
    """
    return current_user
