# Security and deployment notes

The project is an unauthenticated prototype and should not be exposed publicly as-is.

- Keep API keys in environment variables or a secret manager. Rotate credentials previously stored in a source revision or archive.
- The app stores trip state in process memory. Add a proper session store, expiration, user isolation, and access control for a real deployment.
- Add request validation limits, rate limiting, structured error handling, and observability that does not log message contents or credentials.
- Restrict allowed origins as appropriate, review third-party CDN use, and serve the app behind HTTPS.
- Review each external provider's terms, privacy policy, rate limits, and attribution requirements.
- Treat generated itineraries, costs, opening hours, and travel advice as suggestions, not confirmed bookings or guarantees.
- Review dependencies and pin a tested lockfile before production use.
