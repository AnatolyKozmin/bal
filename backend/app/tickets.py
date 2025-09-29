from __future__ import annotations

import os
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import qrcode


ASSETS_DIR = os.getenv("TICKET_ASSETS_DIR", "/app/assets")
OUTPUT_DIR = os.getenv("TICKET_OUTPUT_DIR", "/app/generated_tickets")
TEMPLATE_NAME = os.getenv("TICKET_TEMPLATE", "ticket_template.png")
FONT_PATH = os.getenv("TICKET_FONT", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")


def ensure_dirs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_qr(data: str, size: int = 360) -> Image.Image:
    qr = qrcode.QRCode(border=1, box_size=10)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    return img.resize((size, size))


def compose_ticket(full_name: str, student_id: str, qr_data: str) -> str:
    ensure_dirs()
    template_path = os.path.join(ASSETS_DIR, TEMPLATE_NAME)
    base = Image.open(template_path).convert("RGB")

    # positions — подкорректируем позже по макету
    draw = ImageDraw.Draw(base)
    font_big = ImageFont.truetype(FONT_PATH, 48)
    font_small = ImageFont.truetype(FONT_PATH, 32)

    # Имя Фамилия
    draw.text((80, 120), full_name, fill=(0, 0, 0), font=font_big)
    # № студ билета
    draw.text((80, 190), f"ID: {student_id}", fill=(0, 0, 0), font=font_small)

    # QR
    qr_img = generate_qr(qr_data, size=360)
    base.paste(qr_img, (800, 60))

    out_path = os.path.join(OUTPUT_DIR, f"ticket_{student_id}.png")
    base.save(out_path, format="PNG")
    return out_path


