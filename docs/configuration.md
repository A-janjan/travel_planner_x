# Configuration

Configuration is read from environment variables. For local work, copy `.env.example` to `.env`; the file is ignored by Git.

## Language model

`OPENAI_API_KEY` enables the LLM-backed portions of chat and trip planning. The application is designed to start without a key and use limited deterministic fallbacks, but the offline experience is not equivalent to full AI planning. Some agents currently specify model names directly in source, so `OPENAI_MODEL` is informational until those defaults are consolidated.

## Optional integrations

- `RAPIDAPI_KEY` enables the optional car-rental provider. Without it, the integration is unavailable and the app should not attempt live requests.
- Geocoding, attraction lookup, weather, and route services make outbound HTTP requests. Availability, rate limits, and terms are controlled by each provider.
- `PORT` is used by `python main.py`; when invoking Uvicorn directly, pass the port on the command line.

Do not place credentials in source files, JSON data, logs, screenshots, or issue reports. Rotate any key that may have been committed in an earlier version.
