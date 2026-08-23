from typing import Any


def prepare_profile_context(raw_profile: dict[str, Any]) -> dict[str, Any]:
    """
    Extract only the fields relevant to first name, last name,
    current company and current role.
    """

    first_name = raw_profile.get("firstName")
    last_name = raw_profile.get("lastName")
    headline = raw_profile.get("headline")

    experience = raw_profile.get("experience") or []

    relevant_experience = []

    for exp in experience:
        relevant_experience.append(
            {
                "position": exp.get("position"),
                "companyName": exp.get("companyName"),
                "employmentType": exp.get("employmentType"),
                "workplaceType": exp.get("workplaceType"),
                "period": exp.get("period"),
            }
        )

    # Keep only a reasonable amount of experience data.
    # Usually the first entry is the current/latest position.
    relevant_experience = relevant_experience[:5]

    return {
        "first_name": first_name,
        "last_name": last_name,
        "headline": headline,
        "experience": relevant_experience,
    }