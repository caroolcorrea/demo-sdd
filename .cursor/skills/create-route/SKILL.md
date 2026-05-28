---
name: create-route
description: Cria uma nova rota HTTP FastAPI seguindo Clean Architecture. Use quando o usuário pedir para criar uma rota, adicionar endpoint ou expor uma API.
---

# Criar Rota

## Fluxo

### 1. Confirmar o que existe

- Se o **repository** já existe: pular para passo 3 (use case).
- Se é **novo recurso**: criar port → repository → use case → container → rota.

### 2. Port (se novo recurso)

Criar `src/domain/repositories/<nome>_repository.py`:
```python
class I<Nome>Repository(ABC):
    @abstractmethod
    async def <metodo>(self, ...) -> ...: ...
```

### 3. Use case

Criar `src/application/use_cases/<dominio>/<nome>.py`.
Ver skill [`create-use-case`](../create-use-case/SKILL.md).

### 4. DTOs (se necessário)

Em `src/application/dto/<dominio>_dto.py`: Pydantic para o que a rota retorna.

### 5. Container DI

Em `src/infrastructure/containers/containers.py`:
```python
nome_use_case = providers.Singleton(NomeUseCase, repository=repository.nome_repository)
```

### 6. Rota

Em `src/infrastructure/entrypoint/http/routes/<nome>.py`:

```python
from fastapi import APIRouter, HTTPException, Request, status
from src.infrastructure.containers.containers import container
from src.application.exceptions import ApplicationException

router = APIRouter(prefix="/<recurso>", tags=["<recurso>"])


@router.get("/{id}", response_model=RecursoResponse, summary="Busca <recurso> por ID")
async def get_recurso(id: str, request: Request):
    """Busca um recurso por ID."""
    use_case = container.use_case.get_recurso_use_case()
    try:
        result = await use_case.execute(GetRecursoInput(id=id))
        if result is None:
            raise HTTPException(status_code=404, detail="Não encontrado")
        return result
    except HTTPException:
        raise
    except ApplicationException:
        raise
    except Exception as e:
        logger.error("[GET_RECURSO] Erro: %s", e, exc_info=True)
        raise HTTPException(status_code=500)
```

### 7. Registrar router em main.py

Só se for arquivo de router **novo** (novo prefix/tag):

```python
from src.infrastructure.entrypoint.http.routes.nome import router as nome_router
app.include_router(nome_router)
```

---

## Referência rápida de arquivos

| Camada    | Caminho                                                           |
|-----------|-------------------------------------------------------------------|
| Port      | `src/domain/repositories/<nome>_repository.py`                   |
| Use case  | `src/application/use_cases/<dominio>/<nome>.py`                  |
| DTOs      | `src/application/dto/<dominio>_dto.py`                           |
| Container | `src/infrastructure/containers/containers.py`                    |
| Rota      | `src/infrastructure/entrypoint/http/routes/<nome>.py`            |
