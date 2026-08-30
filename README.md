# APIZIT FastAPI Light API

A minimal FastAPI application for repeatable APIZIT scan, build, launch, and
timeout tests. It has no external service or cloud-specific code.

## Routes

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/health` | Immediate health response |
| `GET` | `/info` | Framework and profile metadata |
| `POST` | `/echo` | JSON request and response |
| `GET` | `/items/{item_id}?include_details=true` | Path and query parameters |
| `GET` | `/slow` | Intentional 80-second response |

`/slow` is a timeout probe. Never configure it as a health check.

## Run locally

Python 3.12 is required.

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m uvicorn app:app
```

The API is available at `http://127.0.0.1:8000`.

```bash
curl http://127.0.0.1:8000/health
curl "http://127.0.0.1:8000/items/7?include_details=true"
curl -X POST http://127.0.0.1:8000/echo -H "Content-Type: application/json" -d '{"message":"hello","count":2}'
```

## Verify

```bash
ruff check .
ruff format --check .
pytest -q
```

This is a controlled beta reference project, not a production application.
