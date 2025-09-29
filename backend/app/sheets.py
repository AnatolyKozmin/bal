from __future__ import annotations

import base64
import json
import os
from typing import List

from google.oauth2 import service_account
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def _load_credentials():
    """Load service account credentials.

    Reads either GOOGLE_APPLICATION_CREDENTIALS_JSON (raw JSON) or
    GOOGLE_APPLICATION_CREDENTIALS_B64 (base64-encoded JSON) from env.
    """
    raw_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    b64_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_B64")

    info = None
    if raw_json:
        info = json.loads(raw_json)
    elif b64_json:
        info = json.loads(base64.b64decode(b64_json).decode("utf-8"))
    else:
        path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if not path:
            raise RuntimeError(
                "Missing Google credentials. Set GOOGLE_APPLICATION_CREDENTIALS_JSON or GOOGLE_APPLICATION_CREDENTIALS_B64 or GOOGLE_APPLICATION_CREDENTIALS path."
            )
        with open(path, "r", encoding="utf-8") as f:
            info = json.load(f)

    return service_account.Credentials.from_service_account_info(info, scopes=SCOPES)


def append_row(spreadsheet_id: str, worksheet_name: str, values: List[str]):
    creds = _load_credentials()
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    body = {"values": [values]}
    result = sheet.values().append(
        spreadsheetId=spreadsheet_id,
        range=f"{worksheet_name}!A1",
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body=body,
    ).execute()
    return result


