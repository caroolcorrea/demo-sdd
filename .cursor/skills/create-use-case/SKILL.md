---
name: create-use-case
description: Cria um novo use case seguindo os padrões de Clean Architecture do projeto. Use quando o usuário pedir para criar um novo use case, operação de negócio ou funcionalidade.
---

# Criar Use Case

## Fluxo

### Passo 1: Criar arquivo em `src/application/use_cases/<dominio>/<acao>_<entidade>.py`

```python
"""
<Acao><Entidade>UseCase — <descrição breve>.
"""

import logging
from typing import Optional
from pydantic import BaseModel

from src.application.exceptions import ApplicationException, NotFoundException

logger = logging.getLogger(__name__)


class <AcaoEntidade>Input(BaseModel):
    """Modelo de entrada para o use case."""
    # campos de entrada com tipos e Optional quando necessário


class <AcaoEntidade>Output(BaseModel):
    """Modelo de saída do use case."""
    # campos de saída — mínimo necessário para o chamador


class <AcaoEntidade>UseCase:
    """
    <Descrição do use case>.

    Responsabilidades:
    - <lista de responsabilidades>
    """

    def __init__(self, repository: I<Entidade>Repository):
        self.repository = repository

    async def execute(self, input_data: <AcaoEntidade>Input) -> <AcaoEntidade>Output:
        """Executa a lógica de negócio."""
        logger.info("[<ACAO_ENTIDADE>] iniciando — %s", input_data)
        try:
            # 1. Validar regras de negócio
            # 2. Executar operação principal via repository
            # 3. Retornar output
            pass
        except ApplicationException:
            raise
        except Exception:
            logger.error("[<ACAO_ENTIDADE>] Erro inesperado", exc_info=True)
            raise
```

### Passo 2: Registrar no container DI

Em `src/infrastructure/containers/containers.py`, no `UseCaseContainer`:

```python
<acao>_<entidade>_use_case: providers.Singleton[<AcaoEntidade>UseCase] = providers.Singleton(
    <AcaoEntidade>UseCase,
    repository=repository.<entidade>_repository,
)
```

### Passo 3: Criar testes

Em `tests/unit/application/use_cases/<dominio>/test_<acao>_<entidade>.py`.
Ver skill [`create-test`](../create-test/SKILL.md).

---

## Regras

- Um use case = uma operação de negócio.
- `execute()` DEVE ser `async`.
- NUNCA acessar DB, HTTP client diretamente — usar repository injetado.
- Lançar subtipos de `ApplicationException` para erros de negócio.
- Logging estruturado com prefixo `[NOME_USE_CASE]`.
