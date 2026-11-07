# Architecture

## Request flow

1. FastAPI serves the Jinja-rendered UI and static assets.
2. The UI calls `/api/process` or `/api/stream` with a workflow step and a session ID.
3. `TravelGraph` maintains per-session travel state and delegates work to domain agents.
4. Agents call provider adapters for geocoding, attraction discovery, weather, routes, fuel prices, and optional rentals.
5. Responses are returned as JSON or Server-Sent Events. The frontend renders recommendations and itinerary/map data.

## Components

- `main.py`: FastAPI routes, templates/static setup, and in-memory session registry.
- `workflows/travel_graph.py`: step transitions and state handling.
- `agents/`: chat collection, attraction ranking, strategy, communication, and route planning.
- `services/`: provider adapters and fallback behavior.
- `data/`: seed/reference data; runtime caches should not be committed.

Most provider agents are shared by workflow instances; chat state is intentionally created per session to prevent one visitor's conversation history from being reused by another. Session objects remain in process memory and disappear on restart.

## State and concurrency

This design is suitable for a single-process prototype, not a multi-worker production deployment. In-memory sessions are not shared between workers, are not durable, and do not have authentication or expiration controls. Use an external session store, access controls, rate limiting, and appropriate synchronization before public deployment.
