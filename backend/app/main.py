from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, constr
from typing import Literal
import os
from .config import settings
from .sheets import append_row


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
def create_registration(payload: Registration):
    try:
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


