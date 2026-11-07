# API reference

The API is unauthenticated in the current prototype. Do not expose session-management endpoints publicly without adding access controls.

## `GET /health`

Returns a minimal process check: `{"status":"ok"}`.

## `POST /api/process`

JSON body:

```json
{
  "step": "chat",
  "user_input": "I want to visit Paris for three days",
  "selected_attraction_ids": null,
  "session_id": null
}
```

The `step` can be `chat`, `information`, `recommend`, `strategy`, `route`, or `communication`. The returned JSON contains workflow output, current state, and a session ID. If no session ID is sent, one is created.

## `GET /api/stream`

SSE endpoint with query parameters `step`, `user_input`, `selected_attraction_ids` (JSON-encoded list), and `session_id`. Events are sent as `data: <JSON>`, with `type` values including `chunk`, `complete`, and `error`.

## `GET /api/attractions/{city}`

Searches for attractions near a geocoded city. Accepts optional `session_id` query parameter.

## `GET /api/nearby/{lat},{lng}`

Searches for nearby points of interest from latitude and longitude coordinates, with optional `session_id`.

## Session endpoints

- `GET /api/reset?session_id=...` — resets an existing session or creates one.
- `GET /api/sessions` — returns process-local session diagnostics.
- `DELETE /api/sessions/{session_id}` — removes a session; returns 404 if it does not exist.

These endpoints are for development and should be redesigned or protected before deployment.
