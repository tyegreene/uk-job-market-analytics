import json
from pathlib import Path

import pandas as pd

from config import PROJECT_ROOT


RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"


def get_latest_raw_file() -> Path:
    """Return the most recently created raw JSON file."""
    files = sorted(RAW_DATA_DIR.glob("adzuna_*.json"), key=lambda p: p.stat().st_mtime)
    if not files:
        raise FileNotFoundError(
            f"No raw files found in {RAW_DATA_DIR}. Run: python src/extract_jobs.py"
        )
    return files[-1]


def load_raw_jobs(filepath: Path) -> tuple[dict, list[dict]]:
    """Load metadata wrapper and jobs list from raw JSON."""
    with open(filepath, encoding="utf-8") as f:
        payload = json.load(f)

    metadata = {
        "extracted_at": payload.get("extracted_at"),
        "search_term": payload.get("search_term"),
        "country": payload.get("country"),
        "total_jobs": payload.get("total_jobs"),
    }
    jobs = payload.get("jobs", [])
    return metadata, jobs


def flatten_job(job: dict) -> dict:
    """Convert one nested job record into a flat dictionary."""
    location = job.get("location") or {}
    company = job.get("company") or {}
    category = job.get("category") or {}

    area = location.get("area") or []
    region = area[1] if len(area) > 1 else None

    return {
        "job_id": job.get("id"),
        "title": job.get("title"),
        "description": job.get("description"),
        "company": company.get("display_name"),
        "location": location.get("display_name"),
        "region": region,
        "category": category.get("label"),
        "contract_type": job.get("contract_type"),
        "contract_time": job.get("contract_time"),
        "salary_min": job.get("salary_min"),
        "salary_max": job.get("salary_max"),
        "salary_is_predicted": job.get("salary_is_predicted"),
        "created": job.get("created"),
        "latitude": job.get("latitude"),
        "longitude": job.get("longitude"),
        "redirect_url": job.get("redirect_url"),
    }


def profile_dataframe(df: pd.DataFrame) -> None:
    """Print a human-readable data profile."""
    print("\n" + "=" * 50)
    print("DATA PROFILE")
    print("=" * 50)

    print(f"\nRows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\n--- Column Types ---")
    print(df.dtypes)

    print("\n--- Missing Values ---")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100).round(1)
    profile = pd.DataFrame({"missing": missing, "pct": missing_pct})
    print(profile[profile["missing"] > 0].sort_values("missing", ascending=False))

    print("\n--- Sample: Top 5 Companies ---")
    print(df["company"].value_counts().head())

    print("\n--- Sample: Top 5 Regions ---")
    print(df["region"].value_counts().head())

    print("\n--- Salary Stats (where present) ---")
    print(df["salary_min"].describe())


def main() -> None:
    raw_file = get_latest_raw_file()
    print(f"Loading: {raw_file.name}")

    metadata, jobs = load_raw_jobs(raw_file)
    print(f"Extracted at: {metadata['extracted_at']}")
    print(f"Search term:  {metadata['search_term']}")
    print(f"Total jobs:   {metadata['total_jobs']}")

    flat_jobs = [flatten_job(job) for job in jobs]
    df = pd.DataFrame(flat_jobs)

    profile_dataframe(df)

    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = PROCESSED_DATA_DIR / "jobs_flat_preview.csv"
    df.to_csv(output_path, index=False, encoding="utf-8")

    print("\n" + "=" * 50)
    print(f"Preview CSV saved: {output_path}")
    print("=" * 50)


if __name__ == "__main__":
    main()