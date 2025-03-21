from fastapi import FastAPI  # type: ignore

from app.api.routers.init_db import router as init_db_router
from app.api.routers.item import router as item_router
from app.api.routers.login import router as login_router
from app.api.routers.user import router as user_router
from app.configs import settings

app = FastAPI(title=settings.PROJECT_NAME)


app.include_router(login_router, prefix=settings.API_V1_STR)
app.include_router(user_router, prefix=settings.API_V1_STR)
app.include_router(item_router, prefix=settings.API_V1_STR)
app.include_router(init_db_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn  # type: ignore

    uvicorn.run(app, host="0.0.0.0", port=8000)
