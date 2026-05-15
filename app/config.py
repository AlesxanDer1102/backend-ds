
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    database_url: str = f"sqlite:///{(BASE_DIR / 'incidencias.db').as_posix()}"

    uploads_dir: Path = BASE_DIR / "uploads"

    frontend_origin: str = "http://localhost:3000"

    max_image_bytes: int = 5 * 1024 * 1024  # 5 MB
    allowed_image_types: tuple[str, ...] = (
        "image/jpeg",
        "image/png",
        "image/webp",
    )

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()


settings.uploads_dir.mkdir(parents=True, exist_ok=True)
