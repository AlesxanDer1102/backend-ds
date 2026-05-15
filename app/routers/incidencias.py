from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.decorators import manejar_errores_de_dominio
from app.enums import Categoria
from app.factories import IncidenciaFactory
from app.models import Incidencia
from app.schemas import IncidenciaOut
from app.services.image_service import image_storage

router = APIRouter(prefix="/incidencias", tags=["incidencias"])


@router.post("", response_model=IncidenciaOut, status_code=status.HTTP_201_CREATED)
@manejar_errores_de_dominio
async def registrar_incidencia(
    categoria: Categoria = Form(...),
    descripcion: str = Form(..., min_length=5, max_length=1000),
    ubicacion: str = Form(..., min_length=3, max_length=255),
    imagen: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    contenido = await imagen.read()
    image_storage.validar(imagen, contenido)
    nombre, url = image_storage.guardar(imagen, contenido)
    incidencia = IncidenciaFactory.crear(
        categoria=categoria.value,
        descripcion=descripcion,
        ubicacion=ubicacion,
        imagen_nombre=nombre,
        imagen_url=url,
    )
    db.add(incidencia)
    db.commit()
    db.refresh(incidencia)
    return incidencia


@router.get("", response_model=list[IncidenciaOut])
def listar_incidencias(db: Session = Depends(get_db)):
    return db.query(Incidencia).order_by(Incidencia.creada_en.desc()).all()


@router.get("/{incidencia_id}", response_model=IncidenciaOut)
def obtener_incidencia(incidencia_id: int, db: Session = Depends(get_db)):
    incidencia = db.get(Incidencia, incidencia_id)
    if incidencia is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incidencia no encontrada",
        )
    return incidencia
