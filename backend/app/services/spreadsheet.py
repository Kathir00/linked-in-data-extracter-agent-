from pathlib import Path
from typing import Any

from openpyxl import Workbook


BASE_DIR = Path(__file__).resolve().parents[2]
EXPORT_DIR = BASE_DIR / "exports"

EXPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def save_profile_to_excel(
    profile: dict[str, Any],
    filename: str
) -> str:

    filepath = EXPORT_DIR / filename

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "LinkedIn Profile"

    headers = [
        "First Name",
        "Last Name",
        "Role",
        "Company",
    ]

    worksheet.append(headers)

    worksheet.append(
        [
            profile.get("first_name"),
            profile.get("last_name"),
            profile.get("role"),
            profile.get("company"),
        ]
    )

    # Basic column widths
    worksheet.column_dimensions["A"].width = 20
    worksheet.column_dimensions["B"].width = 20
    worksheet.column_dimensions["C"].width = 45
    worksheet.column_dimensions["D"].width = 35

    workbook.save(filepath)

    return str(filepath)