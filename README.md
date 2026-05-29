# demo-sdd

Projeto de referência para demonstrar **Spec-Driven Design (SDD)** em uma API Python/FastAPI com Clean Architecture.

A ideia principal é simples: antes de mudar o código, a intenção da mudança fica registrada em uma spec versionada. Assim, o projeto mantém contexto, decisões e critérios de aceite junto do código.

## Como este projeto funciona

Toda mudança relevante segue o pipeline:

```text
SPECIFY -> DESIGN -> TASKS -> EXECUTE
```

- **Specify**: define objetivo, requisitos, restrições e critérios de aceite.
- **Design**: descreve a arquitetura quando a mudança exige decisão técnica.
- **Tasks**: quebra features grandes em passos pequenos e verificáveis.
- **Execute**: implementa a mudança e valida os critérios definidos.

Mudanças pequenas usam **quick mode** em `.specs/quick/`, com um `TASK.md` antes da alteração e um `SUMMARY.md` depois.

## Estrutura SDD

```text
.specs/
├── project/      # Visão, roadmap e memória do projeto
├── codebase/     # Mapa do estado atual do código
├── features/     # Specs completas por feature
└── quick/        # Mudanças pequenas e pontuais
```

## Stack

- Python 3.12+
- FastAPI
- MongoDB com Motor async
- Pydantic v2
- dependency-injector
- pytest + pytest-asyncio
- Poetry

## Comandos básicos

```bash
poetry install
make unit
make run
```

## Onde começar

Leia primeiro `.specs/README.md` para entender o fluxo SDD. Depois consulte `.specs/project/PROJECT.md` para ver os princípios do projeto e `.specs/codebase/` para entender o estado atual da arquitetura.
