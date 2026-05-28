"""
ErrorResponseDTO — formato padronizado de erro para todas as respostas de erro da API.
"""

from typing import Any, Optional
from pydantic import BaseModel


class ErrorResponseDTO(BaseModel):
    """Formato padrão de resposta de erro."""

    success: bool = False
    error_code: str
    message: str
    details: Optional[Any] = None
