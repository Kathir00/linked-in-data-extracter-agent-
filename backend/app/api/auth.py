import secrets

from fastapi import APIRouter, HTTPException

from app.schemas.auth import (
    LoginRequest,
    LoginResponse,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


# Development credentials only.
# Replace with database authentication later.
DEMO_USERNAME = "admin"
DEMO_PASSWORD = "admin123"

VALID_TOKENS: set[str] = set()


@router.post(
    "/login",
    response_model=LoginResponse
)
def login(request: LoginRequest):

    if (
        request.username != DEMO_USERNAME
        or request.password != DEMO_PASSWORD
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = secrets.token_urlsafe(32)

    VALID_TOKENS.add(token)

    return {
        "access_token": token,
        "token_type": "bearer",
    }