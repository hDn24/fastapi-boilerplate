from fastapi.security import OAuth2PasswordBearer

from app.configs import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/login/access-token")
