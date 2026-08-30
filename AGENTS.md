# Reference API repository guidelines

This repository is one autonomous member of the APIZIT reference API suite.

- Keep Python 3.12 compatibility and exactly five detected public routes.
- Preserve the shared paths and successful response contract in README.md.
- Keep /health immediate and keep /slow at exactly 80 seconds.
- Keep FastAPI documentation routes disabled so the public surface is explicit.
- Do not add cloud infrastructure, Dockerfiles, generated handlers, secrets, credentials, or APIZIT-internal imports.
- Pin direct dependencies and keep production manifests at the repository root.
- Update tests, README.md, and CONTRIBUTING.md whenever the HTTP contract changes.
- Run Ruff, pytest, an application import check, and an APIZIT scan before publication.
- Use a codex/ branch, a Conventional Commit, and a reviewed pull request.
