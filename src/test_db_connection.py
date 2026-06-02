from sqlalchemy import create_engine, text

from config import settings


def main() -> None:
    settings.validate_db()

    engine = create_engine(settings.database_url)

    with engine.connect() as conn:
        version = conn.execute(text("SELECT version();")).scalar()
        count = conn.execute(text("SELECT COUNT(*) FROM job_listings;")).scalar()

    print("Database connection successful!")
    print(f"PostgreSQL: {str(version)[:60]}...")
    print(f"job_listings row count: {count}")


if __name__ == "__main__":
    main()