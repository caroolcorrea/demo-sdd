"""
Exemplo de entidade de domínio.

Novas entidades DEVEM usar dataclass ou classe Python pura.
Pydantic pertence à camada de infraestrutura/application.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class ExampleEntity:
    """Entidade de exemplo — Python puro, sem dependência de framework."""

    id: Optional[str]
    name: str
    description: Optional[str]
    active: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
