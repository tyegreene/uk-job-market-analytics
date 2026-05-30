import os
from pathlib import Path

from dotenv import load_dotenv


# Project root is one level above src/
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load .env from project root
load_dotenv(PROJECT_ROOT / ".env")


class Settings:
    """Application settings loaded from environment variables."""

    ADZUNA_APP_ID: str = os.getenv("ADZUNA_APP_ID", "")
    ADZUNA_APP_KEY: str = os.getenv("ADZUNA_APP_KEY", "")
    ADZUNA_COUNTRY: str = os.getenv("ADZUNA_COUNTRY", "gb")
    RESULTS_PER_PAGE: int = int(os.getenv("RESULTS_PER_PAGE", "50"))
    MAX_PAGES: int = int(os.getenv("MAX_PAGES", "5"))

    @classmethod
    def validate(cls) -> None:
        """Raise a clear error if required credentials are missing."""
        missing = []
        if not cls.ADZUNA_APP_ID:
            missing.append("ADZUNA_APP_ID")
        if not cls.ADZUNA_APP_KEY:
            missing.append("ADZUNA_APP_KEY")

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}. "
                "Copy .env.example to .env and add your Adzuna API credentials."
            )


settings = Settings()