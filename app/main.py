from fastapi import FastAPI  # type: ignore

from app.api.routers.item import router as item_router
from app.api.routers.login import router as login_router
from app.api.routers.user import router as user_router
from app.configs import settings

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")


app.include_router(login_router, prefix=settings.API_V1_STR)
app.include_router(user_router, prefix=settings.API_V1_STR)
app.include_router(item_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn  # type: ignore

    uvicorn.run(app, host="0.0.0.0", port=8000)
