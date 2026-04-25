from pathlib import Path

from dotenv import load_dotenv

from src.configs.log import logger


def load_env_file(
    path: Path,
    name: str,
) -> None:
    if not path.exists():
        return

    load_dotenv(
        dotenv_path=path,
        override=True,
    )

    logger.info(f"Environment loaded: {name}")


def load_env_files(
    root: Path,
    py_env: str,
) -> None:
    files: list[str] = [
        ".env",
        ".env.local",
        f".env.{py_env}",
        f".env.{py_env}.local",
    ]

    for file in files:
        load_env_file(
            path=root / file,
            name=file,
        )
