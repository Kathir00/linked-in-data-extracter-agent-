from pydantic import BaseModel, HttpUrl
from typing import Optional


class ProfileRequest(BaseModel):
    linkedin_url: HttpUrl


class ProfileResult(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = None
    company: Optional[str] = None


class ProfileResponse(BaseModel):
    success: bool
    data: ProfileResult
    download_url: Optional[str] = None