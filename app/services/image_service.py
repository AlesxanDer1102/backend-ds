import io
import uuid
from pathlib import Path

from fastapi import UploadFile
from PIL import Image, UnidentifiedImageError

from app.config import settings


class ImageStorageService:
    # Aqui se usa el patron Singleton 
    _instancia: "ImageStorageService | None" = None

    def __new__(cls) -> "ImageStorageService":
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self) -> None:
        self._uploads_dir = settings.uploads_dir
        self._uploads_dir.mkdir(parents=True, exist_ok=True)

    def validar(self, archivo: UploadFile, contenido: bytes) -> None:
        if not contenido:
            raise ValueError("La imagen esta vacia")
        if archivo.content_type not in settings.allowed_image_types:
            raise ValueError("Formato de imagen no permitido")
        if len(contenido) > settings.max_image_bytes:
            raise ValueError("La imagen supera el tamano maximo permitido")
        try:
            Image.open(io.BytesIO(contenido)).verify()
        except (UnidentifiedImageError, OSError):
            raise ValueError("El archivo no es una imagen valida")

    def guardar(self, archivo: UploadFile, contenido: bytes) -> tuple[str, str]:
        extension = Path(archivo.filename or "").suffix.lower() or ".jpg"
        nombre = f"{uuid.uuid4().hex}{extension}"
        (self._uploads_dir / nombre).write_bytes(contenido)
        return nombre, f"/uploads/{nombre}"


image_storage = ImageStorageService()
