"""
IExampleRepository — Port (contrato) para persistência de ExampleEntity.
Implementado na camada Infrastructure.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.example import ExampleEntity


class IExampleRepository(ABC):
    """Contrato para operações de persistência de ExampleEntity."""

    @abstractmethod
    async def save(self, entity: ExampleEntity) -> str:
        """Salva entidade e retorna o ID."""

    @abstractmethod
    async def find_by_id(self, entity_id: str) -> Optional[ExampleEntity]:
        """Busca entidade por ID."""

    @abstractmethod
    async def list_all(self, limit: int = 50, skip: int = 0) -> List[ExampleEntity]:
        """Lista entidades com paginação."""

    @abstractmethod
    async def delete(self, entity_id: str) -> bool:
        """Remove entidade por ID."""
