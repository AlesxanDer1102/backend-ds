import functools

from fastapi import HTTPException, status


def manejar_errores_de_dominio(func):
    # Aqui se usa el patron Decorator
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ValueError as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(exc),
            )

    return wrapper
