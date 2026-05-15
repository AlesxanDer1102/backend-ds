from datetime import datetime

from pydantic import BaseModel, ConfigDict


class IncidenciaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    categoria: str
    descripcion: str
    ubicacion: str
    estado: str
    imagen_url: str
    creada_en: datetime
    actualizada_en: datetime
