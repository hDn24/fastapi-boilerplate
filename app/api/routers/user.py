from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/users")


@router.get("/")
def get_users():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")
