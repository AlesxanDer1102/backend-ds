from enum import Enum


class Categoria(str, Enum):
    BACHE = "bache"
    ALUMBRADO = "alumbrado"
    BASURA = "basura"
    SEGURIDAD = "seguridad"
    EMERGENCIA = "emergencia"
