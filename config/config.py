# config/config.py

# -------------------------------
# Project directories
# -------------------------------

PROJECT_ROOT = "."
DATA_DIR = "data"
RAW_DIR = f"{DATA_DIR}/raw"
DOCS_DIR = "docs"

# -------------------------------
# Database
# -------------------------------

DATABASE_URL = "postgresql://neondb_owner:npg_QRePcJNw4v6K@ep-wispy-king-al8eijpx-pooler.c-3.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

# -------------------------------
# Natural Earth datasets
# -------------------------------

COUNTRIES_URL = "https://naturalearth.s3.amazonaws.com/10m_cultural/ne_10m_admin_0_countries.zip"

PLACES_URL = "https://naturalearth.s3.amazonaws.com/10m_cultural/ne_10m_populated_places.zip"

# -------------------------------
# Copernicus flood dataset
# -------------------------------

FLOOD_ZIP_URL = "https://raw.githubusercontent.com/abr1001/postgis-spatial-analysis/main/Flood.zip"

# -------------------------------
# Table names
# -------------------------------

COUNTRIES_TABLE = "countries"
PLACES_TABLE = "places"
FLOOD_TABLE = "flood_extent_emsr517"

# -------------------------------
# Output files
# -------------------------------

TOP50_CSV = f"{DOCS_DIR}/flood_vulnerability_top50_emsr517.csv"
README_METRICS = f"{DOCS_DIR}/README_metrics.md"
MAP_OUTPUT = f"{DOCS_DIR}/flood_risk_map.html"