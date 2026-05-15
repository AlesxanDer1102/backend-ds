from app.models import Incidencia


class IncidenciaFactory:
    # Aqui se usa el patron Factory 
    @staticmethod
    def crear(
        categoria: str,
        descripcion: str,
        ubicacion: str,
        imagen_nombre: str,
        imagen_url: str,
    ) -> Incidencia:
        return Incidencia(
            categoria=categoria,
            descripcion=descripcion,
            ubicacion=ubicacion,
            estado="reportada",
            imagen_nombre=imagen_nombre,
            imagen_url=imagen_url,
        )
