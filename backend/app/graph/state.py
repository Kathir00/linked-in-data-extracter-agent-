from typing import Any, Optional

from typing_extensions import TypedDict


class ProfileAgentState(TypedDict, total=False):
    linkedin_url: str

    raw_profile: dict[str, Any]

    profile_context: dict[str, Any]

    extracted_profile: dict[str, Optional[str]]

    excel_filename: str

    error: Optional[str]