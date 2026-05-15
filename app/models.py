from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Incidencia(Base):

    __tablename__ = "incidencias"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    categoria: Mapped[str] = mapped_column(String(30), nullable=False)
    descripcion: Mapped[str] = mapped_column(Text, nullable=False)
    ubicacion: Mapped[str] = mapped_column(String(255), nullable=False)

    estado: Mapped[str] = mapped_column(
        String(20), nullable=False, default="reportada"
    )

    imagen_nombre: Mapped[str] = mapped_column(String(255), nullable=False)
    imagen_url: Mapped[str] = mapped_column(String(255), nullable=False)

    creada_en: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    actualizada_en: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )
