from fastapi import FastAPI

from app.api.routers.login import router as login_router
from app.api.routers.user import router as user_router
from app.configs import settings

app = FastAPI(title="fastapi-boilerplate", openapi_url=f"{settings.API_V1_STR}/openapi.json")


app.include_router(login_router, prefix=settings.API_V1_STR)
app.include_router(user_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
