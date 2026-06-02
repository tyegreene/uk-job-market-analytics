CREATE TABLE IF NOT EXISTS job_listings (
    job_id              VARCHAR(50) PRIMARY KEY,
    title               VARCHAR(500) NOT NULL,
    description         TEXT,
    company             VARCHAR(255),
    location            VARCHAR(255),
    region              VARCHAR(100),
    category            VARCHAR(100),
    contract_type       VARCHAR(50),
    contract_time       VARCHAR(50),
    salary_min          NUMERIC(12, 2),
    salary_max          NUMERIC(12, 2),
    salary_is_predicted BOOLEAN,
    created             TIMESTAMPTZ,
    latitude            DOUBLE PRECISION,
    longitude            DOUBLE PRECISION,
    redirect_url        TEXT,
    search_term         VARCHAR(100),
    extracted_at        TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    loaded_at           TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
-- Indexes for common analytics queries (Power BI / SQL later)
CREATE INDEX IF NOT EXISTS idx_job_listings_region
    ON job_listings (region);
CREATE INDEX IF NOT EXISTS idx_job_listings_company
    ON job_listings (company);
CREATE INDEX IF NOT EXISTS idx_job_listings_created
    ON job_listings (created);
CREATE INDEX IF NOT EXISTS idx_job_listings_search_term
    ON job_listings (search_term);