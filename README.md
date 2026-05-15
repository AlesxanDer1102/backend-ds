# Backend — API de Registro de Incidencias

API REST construida con **FastAPI** + **SQLAlchemy** + **SQLite** para el
registro de incidencias en la vía pública (baches, alumbrado, basura,
seguridad ciudadana y emergencias).

## Historias de usuario

### HU-01 — Reporte de una incidencia con evidencia fotográfica

 Como ciudadano, quiero reportar una incidencia en la vía pública
 adjuntando una fotografía, su categoría, una descripción y la ubicación,
 para que la autoridad pueda identificar el problema y darle seguimiento.


Criterios de aceptación:

- El reporte exige categoría, descripción, ubicación e imagen; si falta alguno,
  no se registra.
- Solo se aceptan imágenes JPG, PNG o WEBP de hasta 5 MB.
- Si el archivo no es una imagen válida, el reporte se rechaza con un mensaje
  claro del motivo.
- Toda incidencia registrada nace con estado *reportada*.

### HU-02 — Consulta y visualización de incidencias

Como ciudadano, quiero ver las incidencias ya reportadas con su
fotografía y su estado actual, para que pueda saber si un problema ya fue
notificado y en qué punto de atención se encuentra.

Criterios de aceptación:

- Se puede obtener el listado completo de incidencias, las más recientes
  primero.
- Cada incidencia se muestra con su imagen, categoría, estado y fecha.
- Se puede consultar el detalle de una incidencia concreta.
- Si se pide una incidencia que no existe, la respuesta lo indica con un error
  de "no encontrada".

### HU-03 — Seguimiento del estado de una incidencia
Como autoridad, quiero actualizar el estado de una incidencia conforme
avanza su atención, para que la ciudadanía tenga trazabilidad del
seguimiento que se le da.

Criterios de aceptación:

- El estado solo puede cambiar siguiendo el flujo definido (por ejemplo, una
  incidencia reportada no puede pasar directo a resuelta).
- Una transición no permitida se rechaza e informa cuáles son los estados
  válidos desde el estado actual.
- Si la incidencia no existe, la operación responde con un error de "no
  encontrada".

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

## Endpoints

| Método  | Ruta                        | Descripción                          |
|---------|-----------------------------|--------------------------------------|
| `POST`  | `/incidencias`              | Registra una incidencia con imagen.  |
| `GET`   | `/incidencias`              | Lista todas las incidencias.         |
| `GET`   | `/incidencias/{id}`         | Detalle de una incidencia.           |
| `PATCH` | `/incidencias/{id}/estado`  | Actualiza el estado de una incidencia. |
| `GET`   | `/uploads/{archivo}`        | Sirve el archivo de imagen.          |

## Estructura

```
backend-ds/
├── app/
│   ├── config.py     # Configuración (BD, uploads, CORS, límites)
│   ├── database.py   # Motor SQLite y sesión SQLAlchemy
│   ├── models.py     # Modelo ORM Incidencia
│   ├── schemas.py    # Modelos Pydantic de entrada/salida
│   ├── enums.py      # Categorías y estados
│   ├── factories.py  # Construcción de la entidad Incidencia
│   ├── decorators.py # Manejo de errores de dominio
│   ├── services/     # Almacenamiento de imágenes y workflow de estados
│   ├── routers/      # Endpoints de la API
│   └── main.py       # Aplicación FastAPI
├── uploads/          # Imágenes subidas (generada en tiempo de ejecución)
├── incidencias.db    # Base de datos SQLite (generada en tiempo de ejecución)
└── requirements.txt
```

## Almacenamiento de imágenes

Las imágenes se guardan como archivos en `uploads/`; en la base de datos solo
se almacena su nombre y URL. Esto mantiene la BD ligera y permite servir las
imágenes como archivos estáticos en `/uploads/{archivo}`.
