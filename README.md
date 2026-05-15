# Backend — API de Registro de Incidencias

API REST construida con **FastAPI** + **SQLAlchemy** + **SQLite** para el
registro de incidencias en la vía pública.

## Requisitos

- Python 3.11+

## Puesta en marcha

```powershell
# 1. Crear y activar el entorno virtual
python -m venv .venv
.venv\Scripts\Activate.ps1

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Levantar el servidor de desarrollo
uvicorn app.main:app --reload
```

La API queda disponible en `http://localhost:8000`.
Documentación interactiva (Swagger): `http://localhost:8000/docs`.

## Estructura

```
backend-ds/
├── app/
│   ├── config.py     # Configuración (BD, uploads, CORS, límites)
│   ├── database.py   # Motor SQLite y sesión SQLAlchemy
│   ├── models.py     # Modelo ORM Incidencia
│   └── main.py       # Aplicación FastAPI
├── uploads/          # Imágenes subidas (generada en tiempo de ejecución)
├── incidencias.db    # Base de datos SQLite (generada en tiempo de ejecución)
└── requirements.txt
```

## Almacenamiento de imágenes

Las imágenes se guardan como archivos en `uploads/`; en la base de datos solo
se almacena su nombre y URL. Esto mantiene la BD ligera y permite servir las
imágenes como archivos estáticos en `/uploads/{archivo}`.
