from enum import Enum


class Categoria(str, Enum):
    BACHE = "bache"
    ALUMBRADO = "alumbrado"
    BASURA = "basura"
    SEGURIDAD = "seguridad"
    EMERGENCIA = "emergencia"


class EstadoIncidencia(str, Enum):
    REPORTADA = "reportada"
    EN_REVISION = "en_revision"
    EN_PROCESO = "en_proceso"
    RESUELTA = "resuelta"
    RECHAZADA = "rechazada"
