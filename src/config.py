import os
from pathlib import Path

from dotenv import load_dotenv


# Project root is one level above src/
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load .env from project root
load_dotenv(PROJECT_ROOT / ".env")


class Settings:
    """Application settings loaded from environment variables."""

    # Adzuna API
    ADZUNA_APP_ID: str = os.getenv("ADZUNA_APP_ID", "")
    ADZUNA_APP_KEY: str = os.getenv("ADZUNA_APP_KEY", "")
    ADZUNA_COUNTRY: str = os.getenv("ADZUNA_COUNTRY", "gb")
    RESULTS_PER_PAGE: int = int(os.getenv("RESULTS_PER_PAGE", "50"))
    MAX_PAGES: int = int(os.getenv("MAX_PAGES", "5"))

    # PostgreSQL
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", "5432"))
    DB_NAME: str = os.getenv("DB_NAME", "uk_job_market")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")

    @property
    def database_url(self) -> str:
        """SQLAlchemy connection string."""
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    @classmethod
    def validate(cls) -> None:
        """Raise a clear error if required API credentials are missing."""
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

    @classmethod
    def validate_db(cls) -> None:
        """Raise if required DB credentials are missing."""
        if not cls.DB_PASSWORD:
            raise ValueError(
                "Missing DB_PASSWORD in .env. Add your PostgreSQL password."
            )


settings = Settings()
