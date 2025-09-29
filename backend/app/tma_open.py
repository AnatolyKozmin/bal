from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .db import get_db
from .models import User


router = APIRouter()


@router.post("/api/tma/open")
def tma_open(tg_id: int, tg_username: str | None = None, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.tg_id == tg_id).first()
    if user is None:
        user = User(tg_id=tg_id, tg_username=tg_username)
        db.add(user)
    else:
        user.tg_username = tg_username
    db.commit()
    return {"ok": True}


