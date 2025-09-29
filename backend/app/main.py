from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, constr
from typing import Literal
import os
from .config import settings
from .sheets import append_row
from .db import Base, engine, get_db
from sqlalchemy.orm import Session
from .models import User, Registration as RegistrationModel
from .tma_open import router as tma_router
from .tickets import compose_ticket


class Registration(BaseModel):
    firstName: constr(strip_whitespace=True, min_length=2)
    lastName: constr(strip_whitespace=True, min_length=2)
    patronymic: constr(strip_whitespace=True, min_length=2)
    group: constr(strip_whitespace=True, pattern=r"^[А-ЯA-ZЁ]{2,5}\d{2}-\d{1,2}$")
    faculty: Literal[
        "ИТиАБД",
        "ВШУ",
        "НАБ",
        "СНиМК",
        "ФЭБ",
        "Финфак",
        "Юрфак",
    ]
    studentId: constr(strip_whitespace=True, min_length=4)


app = FastAPI(title="BAL API")
app.include_router(tma_router)


# CORS for local dev and GH Pages
allowed_origins = settings.cors_origins.split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/api/registrations")
def create_registration(payload: Registration, db: Session = Depends(get_db)):
    try:
        # Save to DB
        full_name = f"{payload.firstName} {payload.lastName}"
        reg = RegistrationModel(
            tg_id=0,
            first_name=payload.firstName,
            last_name=payload.lastName,
            patronymic=payload.patronymic,
            group=payload.group,
            faculty=payload.faculty,
            student_id=payload.studentId,
        )
        db.add(reg)
        db.commit()
        db.refresh(reg)

        # Generate ticket file
        qr_payload = f"bal:{payload.studentId}:{payload.lastName}"
        ticket_path = compose_ticket(full_name=full_name, student_id=payload.studentId, qr_data=qr_payload)
        reg.ticket_path = ticket_path
        db.commit()

        values = [
            payload.firstName,
            payload.lastName,
            payload.patronymic,
            payload.group,
            payload.faculty,
            payload.studentId,
        ]
        res = append_row(settings.gsheet_id, settings.gsheet_worksheet, values)
        updates = res.get("updates", {})
        return {"ok": True, "updated": updates.get("updatedCells", 0)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Create tables on startup
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)



