"""
Exceções de negócio da camada Application.
Toda exceção de domínio estende ApplicationException.
"""


class ApplicationException(Exception):
    """Exceção base da camada de aplicação."""

    def __init__(self, message: str, code: str = "APPLICATION_ERROR", status_code: int = 400):
        self.message = message
        self.code = code
        self.status_code = status_code
        super().__init__(self.message)


class NotFoundException(ApplicationException):
    def __init__(self, resource: str, resource_id: str):
        super().__init__(
            message=f"{resource} '{resource_id}' não encontrado",
            code=f"{resource.upper()}_NOT_FOUND",
            status_code=404,
        )


class ValidationException(ApplicationException):
    def __init__(self, message: str):
        super().__init__(message=message, code="VALIDATION_ERROR", status_code=400)


class ConflictException(ApplicationException):
    def __init__(self, message: str):
        super().__init__(message=message, code="CONFLICT", status_code=409)


class PermissionDeniedException(ApplicationException):
    def __init__(self, message: str = "Permissão negada"):
        super().__init__(message=message, code="PERMISSION_DENIED", status_code=403)
