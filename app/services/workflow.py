from app.enums import EstadoIncidencia


class WorkflowIncidencia:
    
    _transiciones: dict[EstadoIncidencia, set[EstadoIncidencia]] = {
        EstadoIncidencia.REPORTADA: {
            EstadoIncidencia.EN_REVISION,
            EstadoIncidencia.RECHAZADA,
        },
        EstadoIncidencia.EN_REVISION: {
            EstadoIncidencia.EN_PROCESO,
            EstadoIncidencia.RECHAZADA,
        },
        EstadoIncidencia.EN_PROCESO: {EstadoIncidencia.RESUELTA},
        EstadoIncidencia.RESUELTA: set(),
        EstadoIncidencia.RECHAZADA: set(),
    }

    def validar(self, actual: str, nuevo: str) -> None:
        estado_actual = EstadoIncidencia(actual)
        estado_nuevo = EstadoIncidencia(nuevo)
        permitidos = self._transiciones[estado_actual]
        if estado_nuevo not in permitidos:
            opciones = ", ".join(e.value for e in permitidos) or "ninguno"
            raise ValueError(
                f"Transicion no permitida de '{actual}' a '{nuevo}'. "
                f"Estados permitidos: {opciones}"
            )


workflow = WorkflowIncidencia()
