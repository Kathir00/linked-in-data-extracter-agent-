import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "anthropic/claude-haiku-4.5"
)

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


class OpenRouterError(Exception):
    pass


def extract_profile_data(profile_context: dict[str, Any]) -> dict[str, Any]:
    """
    Send only relevant LinkedIn profile data to Claude
    and return structured profile information.
    """

    if not OPENROUTER_API_KEY:
        raise OpenRouterError(
            "OPENROUTER_API_KEY is not configured in .env"
        )

    system_prompt = """
You are a LinkedIn profile data extraction agent.

Your task is to extract exactly four fields from the provided
LinkedIn profile context:

1. first_name
2. last_name
3. role
4. company

Rules:

- Use only the information provided.
- Do not invent information.
- first_name must contain only the person's first name.
- last_name must contain only the person's last name.
- role should represent the person's most recent/current professional role.
- company should represent the company associated with that role.
- Prefer the most recent/current experience.
- If a value cannot be determined, return null.
- Return ONLY valid JSON.
- Do not include markdown.
- Do not include explanations.

Required JSON format:

{
    "first_name": "...",
    "last_name": "...",
    "role": "...",
    "company": "..."
}
"""

    user_prompt = f"""
Extract the four requested fields from this LinkedIn profile context:

{json.dumps(profile_context, ensure_ascii=False)}
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        "temperature": 0,
    }

    try:
        response = requests.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload,
            timeout=120,
        )

        response.raise_for_status()

        result = response.json()

        content = result["choices"][0]["message"]["content"]

        # Remove accidental markdown fences if model returns them.
        content = content.strip()

        if content.startswith("```json"):
            content = content[7:]

        if content.startswith("```"):
            content = content[3:]

        if content.endswith("```"):
            content = content[:-3]

        content = content.strip()

        extracted = json.loads(content)

        return {
            "first_name": extracted.get("first_name"),
            "last_name": extracted.get("last_name"),
            "role": extracted.get("role"),
            "company": extracted.get("company"),
        }

    except requests.RequestException as exc:
        raise OpenRouterError(
            f"OpenRouter request failed: {str(exc)}"
        ) from exc

    except (KeyError, IndexError, json.JSONDecodeError) as exc:
        raise OpenRouterError(
            f"Invalid response received from OpenRouter: {str(exc)}"
        ) from exc