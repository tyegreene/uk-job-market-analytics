# UK Job Market Analytics Platform

An end-to-end Data Engineering project that ingests, transforms, and analyses
UK job market data to surface hiring trends, in-demand skills, and regional insights.

## Project Status

🚧 **In Progress** — Currently setting up project foundation.

## Overview

This platform demonstrates a complete data pipeline:

- **Extract** — Collect job listings from public UK job sources
- **Transform** — Clean, standardise, and enrich job data
- **Load** — Store structured data in PostgreSQL
- **Analyse** — SQL transformations and skill extraction
- **Visualise** — Power BI dashboard for stakeholders

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python |
| Data Processing | Pandas |
| Database | PostgreSQL |
| Querying | SQL |
| Visualisation | Power BI |
| Version Control | Git / GitHub |

## Project Structure
market_analytics_proj/ ├── data/ │ ├── raw/ # Raw ingested job listings │ └── processed/ # Cleaned and transformed data ├── src/ # Python ETL scripts ├── sql/ # SQL transformation scripts ├── notebooks/ # Exploratory analysis ├── docs/ # Architecture diagrams and documentation ├── tests/ # Unit tests ├── requirements.txt # Python dependencies └── README.md

## Getting Started
### Prerequisites
- Python 3.10+
- PostgreSQL 15+ (set up in a later step)
- Git
### Installation
```bash
git clone https://github.com/tyegreene/uk-job-market-analytics.git
cd uk-job-market-analytics
python -m venv .venv
# Git Bash
source .venv/Scripts/activate
# PowerShell
# .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Author
Tyese Greene — Data Engineering Portfolio Project

License
MIT