# STACK — Tecnologias e versões

> Snapshot da stack instalada. Atualizar quando subir versão major ou trocar lib.
> Fonte de verdade: `pyproject.toml`, `pytest.ini`.

---

## Runtime

| Camada      | Tecnologia              | Versão alvo | Notas                              |
|-------------|-------------------------|-------------|------------------------------------|
| Linguagem   | Python                  | 3.12+       | `pyproject.toml`                   |
| Framework   | FastAPI                 | 0.115+      | rotas em `src/infrastructure/entrypoint/http/` |
| Servidor    | uvicorn                 | stable      | local                              |
| Validação   | Pydantic                | v2          | request/response models            |
| DI          | dependency-injector     | stable      | `DeclarativeContainer`             |
| HTTP client | httpx (async)           | stable      | para APIs externas                 |
| Async       | asyncio                 | stdlib      |                                    |
| JWT         | PyJWT                   | stable      | HS256                              |

---

## Persistência

| Componente | Versão | Detalhe                                |
|------------|--------|----------------------------------------|
| MongoDB    | 6+     | hospedado externamente (`MONGODB_URL`) |
| Driver     | Motor  | async (`motor.motor_asyncio`)          |
| ODM        | (none) | acesso direto via collections          |

---

## Testes e qualidade

| Ferramenta        | Uso                                            |
|-------------------|------------------------------------------------|
| pytest            | runner                                         |
| pytest-asyncio    | suporte a `async def` (`asyncio_mode=auto`)    |
| pytest-cov        | coverage (gate 80% em `make coverage`)         |
| pytest-mock       | mocks (`AsyncMock`, `MagicMock`)               |
| pytest-timeout    | timeout 30s default                            |
| pytest-xdist      | paralelismo opcional                           |
| httpx             | HTTP em smoke/externo                          |
| FastAPI TestClient| rotas in-process                               |
| mongomock-motor   | MongoDB simulado em integration                |
| Faker             | dados sintéticos                               |
| freezegun         | tempo congelado                                |
| Hypothesis        | property-based complementar                    |
| ruff              | lint + format                                  |
| mypy              | type checking                                  |

---

## Build

| Componente      | Tecnologia |
|-----------------|------------|
| Package manager | Poetry     |
| CI              | GitHub Actions (`.github/workflows/`) |
