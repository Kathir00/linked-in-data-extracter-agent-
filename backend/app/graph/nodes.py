from app.scraper.linkedin_scraper import scrape_linkedin_profile
from app.scraper.parser import prepare_profile_context
from app.services.openrouter import extract_profile_data
from app.services.spreadsheet import save_profile_to_excel

from .state import ProfileAgentState


def scrape_node(state: ProfileAgentState) -> ProfileAgentState:

    linkedin_url = state["linkedin_url"]

    raw_profile = scrape_linkedin_profile(
        linkedin_url
    )

    return {
        **state,
        "raw_profile": raw_profile,
    }


def prepare_context_node(
    state: ProfileAgentState
) -> ProfileAgentState:

    raw_profile = state["raw_profile"]

    profile_context = prepare_profile_context(
        raw_profile
    )

    return {
        **state,
        "profile_context": profile_context,
    }


def extraction_node(
    state: ProfileAgentState
) -> ProfileAgentState:

    profile_context = state["profile_context"]

    extracted_profile = extract_profile_data(
        profile_context
    )

    return {
        **state,
        "extracted_profile": extracted_profile,
    }


def spreadsheet_node(
    state: ProfileAgentState
) -> ProfileAgentState:

    profile = state["extracted_profile"]

    filename = "linkedin_profile.xlsx"

    save_profile_to_excel(
        profile=profile,
        filename=filename,
    )

    return {
        **state,
        "excel_filename": filename,
    }