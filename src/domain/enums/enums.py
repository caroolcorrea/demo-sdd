"""
Enums de domínio — use IntEnum para valores numéricos.
"""

from enum import IntEnum, StrEnum


class StatusEnum(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"


class LevelEnum(IntEnum):
    OWNER = 1
    MANAGER = 2
    ANALYST = 3
