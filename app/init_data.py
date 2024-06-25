import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))


from app.api.cruds import user as crud
from app.api.schemas.user import UseCreate
from app.database import Base, SessionLocal, engine


def init_data():
    session = SessionLocal()
    reset_database()

    user_create = UseCreate(
        username="hDn24",
        email="hDn24@gmail.com",
        password="2ES69y0EFiPynrhAelkcmBTgOGTTirDBJ4G0R-y9qcQ",
        is_superuser=True,
        is_active=True,
    )

    crud.create_user(session, user_create)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("DONE")


init_data()
