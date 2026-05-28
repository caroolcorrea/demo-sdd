# PROJECT — demo-sdd

> **Constitution do projeto.** Decisões não-negociáveis. Toda contribuição deve respeitar esses limites.

---

## Identidade

| Campo            | Valor                                   |
|------------------|-----------------------------------------|
| Nome             | `demo-sdd`                              |
| Linguagem        | Python 3.12+                            |
| Framework HTTP   | FastAPI 0.115+                          |
| Persistência     | MongoDB (Motor async)                   |
| Validação        | Pydantic v2                             |
| DI               | dependency-injector (DeclarativeContainer) |
| Pacotes          | Poetry                                  |
| Testes           | pytest + pytest-asyncio                 |

---

## Visão

> Projeto de referência para demonstrar o pipeline **Spec-Driven Design (SDD)** aplicado a uma API Python/FastAPI com Clean Architecture. Serve como template para novos projetos.

---

## Objetivos

1. Demonstrar o pipeline SDD completo (Specify → Design → Tasks → Execute).
2. Aplicar Clean Architecture estrita (Domain → Application → Infrastructure).
3. Fornecer estrutura de rules e skills reutilizável para novos projetos.
4. Manter cobertura de testes ≥ 80%.

---

## Princípios não-negociáveis

### 1. Clean Architecture estrita

```text
Domain  <--  Application  <--  Infrastructure
```

- **Domain** não importa framework, Motor, Pydantic (em entidades novas) ou infra.
- **Application** não instancia DB/HTTP client; depende apenas de ports.
- **Infrastructure** implementa adapters e nunca contém regra de negócio.

Detalhe: [`/.cursor/rules/clean-architecture.mdc`](../../.cursor/rules/clean-architecture.mdc).

### 2. Side-effects somente via interface

Use cases **não** chamam DB, API externa ou serviços externos diretamente.
Tudo passa por ports (`I*Repository`, `*Service`) injetadas via `__init__`.

### 3. Spec antes de código

Toda feature relevante (>= 4 arquivos ou >= 2 camadas) começa por `spec.md`.
Mudanças pequenas (<= 3 arquivos) usam **quick mode**.

Detalhe: [`/.cursor/rules/spec-driven-design.mdc`](../../.cursor/rules/spec-driven-design.mdc).

### 4. Testes com assertion real

Um teste que passa mesmo quando o código está errado é pior que nenhum teste.
Sempre verificar resultado observável, nunca só chamada de mock.
