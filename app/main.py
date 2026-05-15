
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app import models  
from app.config import settings
from app.database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="API de Registro de Incidencias",
    description="Backend para reportar incidencias en la vía pública.",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/uploads", StaticFiles(directory=settings.uploads_dir), name="uploads")


@app.get("/", tags=["salud"])
def health_check():
    """Endpoint de verificación de estado del servicio."""
    return {"status": "ok", "servicio": "API de Registro de Incidencias"}
