import json
from datetime import datetime
from pathlib import Path

from adzuna_client import fetch_all_pages
from config import PROJECT_ROOT, settings


RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def save_raw_jobs(jobs: list[dict], search_term: str) -> Path:
    """Save raw job listings to a timestamped JSON file."""
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_term = search_term.replace(" ", "_")
    filename = f"adzuna_{safe_term}_{timestamp}.json"
    filepath = RAW_DATA_DIR / filename

    payload = {
        "extracted_at": datetime.now().isoformat(),
        "search_term": search_term,
        "country": settings.ADZUNA_COUNTRY,
        "total_jobs": len(jobs),
        "jobs": jobs,
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    return filepath


def main() -> None:
    search_term = "data engineer"

    print(f"Starting extraction for: '{search_term}'")
    print(f"Country: {settings.ADZUNA_COUNTRY}")
    print(f"Max pages: {settings.MAX_PAGES}")
    print("-" * 40)

    jobs = fetch_all_pages(search_term=search_term)

    if not jobs:
        print("No jobs found. Check your API keys or search term.")
        return

    filepath = save_raw_jobs(jobs, search_term)

    print("-" * 40)
    print(f"Extraction complete!")
    print(f"Total jobs saved: {len(jobs)}")
    print(f"File: {filepath}")


if __name__ == "__main__":
    main()