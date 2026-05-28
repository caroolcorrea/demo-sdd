---
name: create-repository
description: Cria um novo repositório com interface no domain e implementação MongoDB no infrastructure. Use quando o usuário pedir para criar uma nova camada de acesso a dados ou persistência.
---

# Criar Repositório

## Passo 1: Interface no Domain

Criar `src/domain/repositories/<nome>_repository.py`:

```python
"""
I<Entidade>Repository — Port para persistência de <Entidade>.
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.<entidade> import <Entidade>Entity


class I<Entidade>Repository(ABC):
    """Contrato para operações de persistência de <Entidade>."""

    @abstractmethod
    async def save(self, entity: <Entidade>Entity) -> str:
        """Salva entidade e retorna o ID."""

    @abstractmethod
    async def find_by_id(self, entity_id: str) -> Optional[<Entidade>Entity]:
        """Busca entidade por ID."""

    @abstractmethod
    async def list_all(self, limit: int = 50, skip: int = 0) -> List[<Entidade>Entity]:
        """Lista entidades com paginação."""

    @abstractmethod
    async def delete(self, entity_id: str) -> bool:
        """Remove entidade por ID."""
```

## Passo 2: Implementação MongoDB

Criar `src/infrastructure/persistence/repositories/mongodb_<entidade>_repository.py`:

```python
"""
MongoDB<Entidade>Repository — Implementa I<Entidade>Repository.
"""

from typing import List, Optional
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.domain.entities.<entidade> import <Entidade>Entity
from src.domain.repositories.<entidade>_repository import I<Entidade>Repository


class MongoDB<Entidade>Repository(I<Entidade>Repository):
    def __init__(self, db: AsyncIOMotorDatabase):
        self._collection = db["<entidades>"]

    async def save(self, entity: <Entidade>Entity) -> str:
        doc = {"name": entity.name, "_created": entity.created_at}
        result = await self._collection.insert_one(doc)
        return str(result.inserted_id)

    async def find_by_id(self, entity_id: str) -> Optional[<Entidade>Entity]:
        doc = await self._collection.find_one({"_id": ObjectId(entity_id)})
        return self._to_entity(doc) if doc else None

    async def list_all(self, limit: int = 50, skip: int = 0) -> List[<Entidade>Entity]:
        cursor = self._collection.find().skip(skip).limit(limit)
        return [self._to_entity(doc) async for doc in cursor]

    async def delete(self, entity_id: str) -> bool:
        result = await self._collection.delete_one({"_id": ObjectId(entity_id)})
        return result.deleted_count > 0

    def _to_entity(self, doc: dict) -> <Entidade>Entity:
        return <Entidade>Entity(id=str(doc["_id"]), name=doc["name"])
```

## Passo 3: Registrar no container

Em `src/infrastructure/containers/containers.py`:

```python
<entidade>_repository = providers.Singleton(
    MongoDB<Entidade>Repository,
    db=mongodb_client.provided.db,
)
```

---

## Regras

- Interface SEMPRE em `src/domain/repositories/`.
- Implementação SEMPRE em `src/infrastructure/persistence/repositories/`.
- `_id` sempre `ObjectId`.
- `_to_entity` converte doc MongoDB → entidade de domínio.
