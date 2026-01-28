import os
from pathlib import Path

ROOT: str = Path(__file__).parent.parent.parent.resolve().as_posix()


def var(name: str, default: str) -> str:
    value: str | None = os.environ.get(name)
    return value if value is not None else default


def get_py_env() -> str:
    return var("PY_ENV", "development")


def get_app_version() -> str:
    return var("APP_VERSION", "0.0.0")
