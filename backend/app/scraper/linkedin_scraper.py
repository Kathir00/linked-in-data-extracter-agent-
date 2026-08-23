import os
from typing import Any

from apify_client import ApifyClient
from dotenv import load_dotenv


load_dotenv()


APIFY_TOKEN = os.getenv("APIFY_TOKEN")

ACTOR_ID = "harvestapi/linkedin-profile-scraper"


class LinkedInScraperError(Exception):
    pass


def scrape_linkedin_profile(
    linkedin_url: str,
) -> dict[str, Any]:

    if not APIFY_TOKEN:
        raise LinkedInScraperError(
            "APIFY_TOKEN is missing in .env"
        )

    client = ApifyClient(APIFY_TOKEN)

    try:

        # ==========================================
        # RUN APIFY ACTOR
        # ==========================================

        run = client.actor(ACTOR_ID).call(
            run_input={
                "urls": [linkedin_url]
            }
        )

        # ==========================================
        # GET DATASET ID
        # SAME LOGIC AS YOUR WORKING SCRIPT
        # ==========================================

        dataset_id = (
            run.get("defaultDatasetId")
            if isinstance(run, dict)
            else getattr(
                run,
                "default_dataset_id",
                None
            )
        )

        if not dataset_id:
            raise LinkedInScraperError(
                "Could not get Apify dataset ID."
            )

        # ==========================================
        # READ DATASET
        # ==========================================

        items = list(
            client
            .dataset(dataset_id)
            .iterate_items()
        )

        if not items:
            raise LinkedInScraperError(
                "Apify returned no profile data."
            )

        # ==========================================
        # RETURN RAW PROFILE
        # ==========================================

        return items[0]

    except LinkedInScraperError:
        raise

    except Exception as e:
        raise LinkedInScraperError(
            f"LinkedIn scraping failed: {str(e)}"
        ) from e