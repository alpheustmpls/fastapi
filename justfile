set shell := ["bash", "-cu"]
set windows-shell := ["powershell"]

# Default action
_:
    just fmt
    just lint
    just type

# Install
i:
    uv sync --all-packages

# Upgrade dependencies
up:
    uv lock --upgrade
    just i

# Format the code
fmt:
    uv run ruff format

# Lint the code
lint:
    ls-lint
    typos
    uv run ruff check --fix

# Check types
type:
    uv run ty check

# Generate HTTPS certificates
cert:
    mkdir -p .venv/.cert
    mkcert \
    --cert-file .venv/.cert/cert.pem \
    --key-file .venv/.cert/key.pem \
    localhost 127.0.0.1 ::1

# Start the dev server with HTTPS
dev:
    PY_ENV=development \
    uv run uvicorn \
    --ssl-certfile=.venv/.cert/cert.pem \
    --ssl-keyfile=.venv/.cert/key.pem \
    --host 0.0.0.0 \
    --port 3001 \
    --log-level "trace" \
    --reload \
    src.app.main:app

# Start the dev server with HTTP
http:
    PY_ENV=development \
    uv run uvicorn \
    --host 0.0.0.0 \
    --port 3001 \
    --log-level "trace" \
    --reload \
    src.main:app

# Start the production server
start:
    PY_ENV=production uv run uvicorn --host 0.0.0.0 --port 3000 src.main:app

# Clean caches
clean:
    rm -rf .ruff_cache
    find . -type d -name "*.egg-info" -exec rm -rf {} +
    find . -type d -name "__pycache__" -exec rm -rf {} +

# Clean everything
clean-all:
    just clean
    rm -rf .venv
