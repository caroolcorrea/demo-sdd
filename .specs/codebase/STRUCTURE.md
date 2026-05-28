# STRUCTURE — Árvore de diretórios

> Onde cada tipo de código vai. Atualizar quando adicionar top-level dir ou módulo relevante.

```
demo-sdd/
├── .specs/                          # Spec-Driven Design
│   ├── README.md                    # Workflow SDD
│   ├── project/                     # Constitution (PROJECT, ROADMAP, STATE)
│   ├── codebase/                    # Brownfield mapping
│   ├── features/                    # Specs por feature
│   └── quick/                       # Quick mode (<= 3 arquivos)
├── .cursor/
│   ├── manifest.yml                 # Registro de rules e skills
│   ├── rules/                       # Regras sempre-ativas do agente
│   └── skills/                      # Skills invocáveis por nome
├── src/
│   ├── main.py                      # App FastAPI, lifespan, exception handlers
│   ├── settings.py                  # Configuração via variáveis de ambiente
│   ├── application/                 # Camada de Aplicação
│   │   ├── dto/                     # Data Transfer Objects (Pydantic)
│   │   ├── exceptions.py            # Exceções de negócio
│   │   ├── mappers/                 # Transformações de dados
│   │   └── use_cases/               # Use cases por domínio
│   ├── domain/                      # Camada de Domínio (puro)
│   │   ├── entities/                # Dataclasses Python puro
│   │   ├── enums/                   # IntEnum / StrEnum
│   │   └── repositories/            # Ports (interfaces ABC)
│   └── infrastructure/              # Camada de Infraestrutura
│       ├── containers/              # Containers DI (dependency-injector)
│       ├── entrypoint/http/         # Entrypoint HTTP FastAPI
│       │   ├── routes/              # Routers FastAPI
│       │   └── middleware/          # Middlewares HTTP
│       └── persistence/
│           └── repositories/        # Implementações MongoDB
├── tests/
│   ├── conftest.py                  # Fixtures globais
│   ├── unit/                        # Testes unitários (espelha src/)
│   ├── integration/                 # Testes de integração
│   └── smoke/                       # Validação pós-deploy
├── config/
│   └── development.env              # Variáveis de ambiente (local)
├── pyproject.toml
├── pytest.ini
├── Makefile
└── README.md
```

---

## Onde colocar código novo

| Tipo                   | Local                                                     |
|------------------------|-----------------------------------------------------------|
| Entidade de domínio    | `src/domain/entities/<nome>.py`                           |
| Enum                   | `src/domain/enums/enums.py` (ou arquivo separado)         |
| Port (interface)       | `src/domain/repositories/<nome>_repository.py`            |
| Use case               | `src/application/use_cases/<dominio>/<nome>.py`           |
| DTO                    | `src/application/dto/<dominio>_dto.py`                    |
| Mapper                 | `src/application/mappers/<dominio>/`                      |
| Exceção de negócio     | `src/application/exceptions.py`                           |
| Repository MongoDB     | `src/infrastructure/persistence/repositories/mongodb_<nome>_repository.py` |
| Rota FastAPI           | `src/infrastructure/entrypoint/http/routes/<nome>.py`     |
| Middleware             | `src/infrastructure/entrypoint/http/middleware/`          |
| Spec de feature        | `.specs/features/<slug>/spec.md`                          |
| Quick mode             | `.specs/quick/NNN-<slug>/TASK.md`                         |
