# demo-sdd

> Projeto demo de **Spec-Driven Design (SDD)** com Clean Architecture em Python/FastAPI.
> Use este repositório como template ou referência para novos projetos.

---

## Stack

- **Python** 3.12+
- **FastAPI** 0.115+
- **MongoDB** (Motor async)
- **Pydantic** v2
- **dependency-injector** (DeclarativeContainer)
- **pytest** + pytest-asyncio
- **Poetry**

## Estrutura SDD

```
.specs/
├── project/     # Constitution: PROJECT.md, ROADMAP.md, STATE.md
├── codebase/    # Brownfield mapping do estado atual
├── features/    # Specs por feature (spec.md, design.md, tasks.md)
└── quick/       # Mudanças pequenas (<= 3 arquivos)
```

## Início rápido

```bash
# Instalar dependências
poetry install

# Rodar testes
make unit

# Rodar servidor local
make run
```

## Workflow SDD

Toda mudança relevante segue o pipeline:

```
SPECIFY  -->  DESIGN  -->  TASKS  -->  EXECUTE
```

Detalhes em [`.specs/README.md`](.specs/README.md) e skill [`spec-driven-design`](.cursor/skills/spec-driven-design/SKILL.md).
