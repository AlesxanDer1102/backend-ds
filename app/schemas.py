from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.enums import EstadoIncidencia


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


class CambioEstadoIn(BaseModel):
    estado: EstadoIncidencia
