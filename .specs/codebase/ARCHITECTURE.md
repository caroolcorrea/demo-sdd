# ARCHITECTURE — Camadas, DI e fluxo

> Snapshot arquitetural do projeto. Atualizar quando mudar camadas, bootstrap ou padrão de fluxo.

---

## Camadas

```
Domain  <--  Application  <--  Infrastructure
(puro)       (use cases)        (adapters, HTTP, DB)
```

### Domain

- Entidades: `dataclass` Python puro — sem Pydantic, sem framework.
- Enums: `IntEnum` / `StrEnum` em `src/domain/enums/`.
- Ports (interfaces): `ABC` em `src/domain/repositories/`.

### Application

- Use cases em `src/application/use_cases/<dominio>/`.
- DTOs: Pydantic `BaseModel` em `src/application/dto/`.
- Exceções de negócio: `ApplicationException` e subclasses em `src/application/exceptions.py`.
- Mappers em `src/application/mappers/`.

### Infrastructure

- Adapters MongoDB em `src/infrastructure/persistence/repositories/`.
- Entrypoint HTTP (FastAPI) em `src/infrastructure/entrypoint/http/`.
- Container DI em `src/infrastructure/containers/containers.py`.

---

## Fluxo principal

```
Rota (APIRouter) → Use Case (execute) → Repository (interface) → MongoDB / API Externa
```

---

## Container DI

```python
container = ApplicationContainer()
use_case = container.use_case.example_use_case()
result = await use_case.execute(input_data)
```

`ApplicationContainer` em `src/infrastructure/containers/containers.py`:
- `RepositoryContainer` — instâncias MongoDB.
- `UseCaseContainer` — use cases com repositórios injetados.

---

## Lifespan (main.py)

Bootstrap e shutdown via `@asynccontextmanager lifespan(app)`.
Inicialização do MongoDB client no startup.
