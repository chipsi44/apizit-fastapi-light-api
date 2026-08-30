# Contributing

Keep this project small, runnable, and comparable with the other APIZIT reference APIs.

Before opening a pull request:

1. preserve the five documented routes and their successful JSON responses;
2. keep Python 3.12, pinned direct dependencies, and disabled FastAPI documentation routes;
3. do not add secrets, cloud resources, a Dockerfile, or generated deployment files;
4. run `ruff check .`, `ruff format --check .`, and `pytest -q`;
5. verify `from app import app` and run an APIZIT scan.

The 80-second `/slow` route is intentional. Unit tests must patch the wait while asserting the value 80.
