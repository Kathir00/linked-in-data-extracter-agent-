from pathlib import Path

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from fastapi.responses import FileResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.api.auth import VALID_TOKENS
from app.graph.graph import create_profile_graph
from app.schemas.profile import (
    ProfileRequest,
    ProfileResponse,
)


router = APIRouter(
    prefix="/profile",
    tags=["LinkedIn Profile"],
)

security = HTTPBearer()

profile_graph = create_profile_graph()


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    if token not in VALID_TOKENS:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired authentication token"
        )

    return token


@router.post(
    "/extract",
    response_model=ProfileResponse
)
def extract_profile(
    request: ProfileRequest,
    _: str = Depends(verify_token),
):

    try:

        result = profile_graph.invoke(
            {
                "linkedin_url": str(request.linkedin_url)
            }
        )

        extracted_profile = result.get(
            "extracted_profile"
        )

        if not extracted_profile:
            raise HTTPException(
                status_code=500,
                detail="Profile extraction returned no data."
            )

        return {
            "success": True,
            "data": extracted_profile,
            "download_url": "/profile/download/linkedin_profile.xlsx",
        }

    except HTTPException:
        raise

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )


@router.get(
    "/download/{filename}"
)
def download_excel(
    filename: str,
    _: str = Depends(verify_token),
):

    base_dir = Path(__file__).resolve().parents[2]

    file_path = (
        base_dir
        / "exports"
        / filename
    )

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Excel file not found."
        )

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type=(
            "application/vnd.openxmlformats-officedocument"
            ".spreadsheetml.sheet"
        ),
    )