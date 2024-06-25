from fastapi import Depends, FastAPI

from app.api.routers.login import router
from app.configs import settings
from app.dependencies import oauth2_scheme

app = FastAPI()


@app.get("/", tags=["root"])
def root(token: str = Depends(oauth2_scheme)):
    return {"message": "Hello World"}


app.include_router(router, prefix=settings.API_V1_STR, tags=["login"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
