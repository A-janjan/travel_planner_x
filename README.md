# Travel Planner X

An AI-assisted travel-planning web app that collects trip preferences, discovers attractions from OpenStreetMap-based services, recommends places, builds a day-by-day itinerary, estimates a budget, and visualizes places on a map.

## Features

- Conversational collection of trip details and constraints
- Attraction discovery and personalized ranking
- Itinerary and budget generation, including an offline fallback
- Route ordering and map data
- Weather, nearby-place, fuel-price, and optional car-rental integrations
- Server-rendered FastAPI frontend with a streaming response endpoint

## Quick start

Requires Python 3.10 or newer.

Run the following commands from the repository root:

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
cp .env.example .env
```

Add an `OPENAI_API_KEY` to `.env` to enable the full AI planning experience. The application can start without credentials, but some planning features will be limited and use deterministic fallbacks. Set `RAPIDAPI_KEY` only if you want live car-rental search; do not commit `.env`.

Run the server from the repository root:

```bash
uvicorn main:app --host 0.0.0.0 --port "${PORT:-8000}"
```

Then open <http://localhost:8000>. For local development with automatic reload:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Configuration

| Variable | Required | Purpose |
|---|---:|---|
| `OPENAI_API_KEY` | Recommended | Enables LLM-powered chat, ranking, strategy, and confirmation |
| `OPENAI_MODEL` | No | Example model setting for deployments; some agents currently use their own model defaults |
| `RAPIDAPI_KEY` | No | Enables the optional car-rental API integration |
| `PORT` | No | Port used when launching through `python main.py` (default `8000`) |

See [Configuration](docs/configuration.md) for integration details and [Security](docs/security.md) before deployment.

## Project layout

```text
agents/                 Domain agents for chat, discovery, recommendations, strategy, and routing
services/               External API and data-provider adapters
workflows/               Session workflow and optional evaluation helper
frontend/templates/      Jinja templates
frontend/static/         CSS and JavaScript
frontend/data/           Sample popular-attractions data
data/                    Attraction and reference data
main.py                  FastAPI application and HTTP endpoints
docs/                    Setup, architecture, API, and security documentation
tests/                   Repository health tests
```

## API overview

- `GET /` — application page
- `GET /health` — process health check
- `POST /api/process` — process a workflow step using JSON
- `GET /api/stream` — Server-Sent Events workflow response
- `GET /api/attractions/{city}` — search attractions for a city
- `GET /api/nearby/{lat},{lng}` — nearby places for coordinates
- `GET /api/reset?session_id=...` — reset/create an in-memory session
- `GET /api/sessions` — development session diagnostics
- `DELETE /api/sessions/{session_id}` — delete a session

Request and response details are in [API reference](docs/api.md).

## Development checks

```bash
pytest
python -m compileall -q agents services workflows main.py utils.py
ruff check .
```

## Data, attribution, and licensing

The supplied source archive did not include a license file, and its original project reference could not be verified during this cleanup. No new license is asserted here. Before publishing this derivative publicly, confirm that you have the necessary rights to all inherited code, data, and assets, and add the correct license and any legally required notices. See [provenance notes](docs/provenance.md).

OpenStreetMap data is provided under the Open Database License; observe its attribution and usage requirements. External APIs and map tiles are subject to their own terms. Prices, forecasts, opening hours, and route estimates are informational and should be checked with providers before travel.

## Contributing

Issues and pull requests are welcome. Please avoid committing secrets, runtime caches, or personal travel data. Run the checks above before submitting a change.
