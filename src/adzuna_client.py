import requests

from config import settings


BASE_URL = "https://api.adzuna.com/v1/api/jobs"


def fetch_jobs_page(
    page: int = 1,
    search_term: str = "data engineer",
    location: str = "",
) -> dict:
    """
    Fetch one page of job listings from the Adzuna API.

    Args:
        page: Page number (starts at 1)
        search_term: Job title or keyword to search for
        location: Optional location filter (e.g. 'London')

    Returns:
        JSON response as a Python dictionary
    """
    settings.validate()

    url = f"{BASE_URL}/{settings.ADZUNA_COUNTRY}/search/{page}"

    params = {
        "app_id": settings.ADZUNA_APP_ID,
        "app_key": settings.ADZUNA_APP_KEY,
        "results_per_page": settings.RESULTS_PER_PAGE,
        "what": search_term,
    }

    if location:
        params["where"] = location

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    return response.json()


def fetch_all_pages(
    search_term: str = "data engineer",
    location: str = "",
) -> list[dict]:
    """
    Fetch multiple pages of job listings.

    Returns:
        List of all job result dictionaries across all pages
    """
    all_jobs = []

    for page in range(1, settings.MAX_PAGES + 1):
        print(f"Fetching page {page} of {settings.MAX_PAGES}...")
        data = fetch_jobs_page(page=page, search_term=search_term, location=location)

        results = data.get("results", [])
        if not results:
            print(f"No results on page {page}. Stopping.")
            break

        all_jobs.extend(results)
        print(f"  → Got {len(results)} jobs (total so far: {len(all_jobs)})")

    return all_jobs