# Flood Risk Exposure WebGIS (PostGIS + Python + Folium)

## Project Overview

- Copernicus EMS flood polygons (EMSR517) loaded into PostGIS

- Natural Earth populated places loaded as spatial points

- Flood risk classified based on distance from flood extent

- Interactive web map built with Folium


## Key Results

- HIGH risk places (≤5 km from flood): **1**

- Total exposed places (≤50 km): **4**

- Estimated population in HIGH risk: **0**

- Estimated exposed population: **0**


## Risk Categories

- **HIGH** — within 5 km of flood extent

- **MEDIUM** — between 5–50 km of flood extent

- **LOW** — beyond 50 km


## Key Spatial Functions (PostGIS)

- `ST_Distance` — compute distance to flood polygons

- `ST_DWithin` — proximity checks

- `ST_Buffer` and `ST_Difference` — hazard bands

- GiST spatial indexes for fast spatial queries


## Output Tables

- `flood_extent_emsr517` — Copernicus flood polygons

- `places_flood_risk` — risk classification + distance to flood

- `flood_risk_summary_emsr517` — aggregated statistics by risk level

- `flood_band_0_5km_emsr517`, `flood_band_5_50km_emsr517` — hazard band polygons

- `flood_vulnerability_top50_emsr517` — top exposed places (exported to CSV)


## Risk Summary Table


| risk_category   |   n_places |   total_population |
|:----------------|-----------:|-------------------:|
| HIGH            |          1 |                  0 |
| MEDIUM          |          3 |                  0 |
| LOW             |       7338 |                  0 |

