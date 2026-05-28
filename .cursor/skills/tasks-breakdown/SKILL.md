---
name: tasks-breakdown
description: Quebra uma feature Large/Complex em tasks atômicas com dependências e gates de aceite. Use quando o spec/design já existem e a feature tem mais de 5 passos ou dependências entre passos.
---

# Tasks Breakdown — Fase 3 do SDD

> Cria `.specs/features/<slug>/tasks.md` com tasks atômicas, dependências explícitas e gates.
> Pula quando há <= 5 passos óbvios sem dependências.

---

## Quando usar

- Spec (e Design, se Large/Complex) aprovados.
- Feature tem **>= 6 passos** OU dependências entre passos.
- Beneficia de execução paralela parcial.

**Pular Tasks** quando:
- Feature Medium com 3-5 passos lineares.
- Quick mode.

---

## Estrutura do `tasks.md`

```markdown
# tasks: <slug>

> Spec: ./spec.md
> Design: ./design.md (opcional)
> Status: draft | approved | in-progress | done
> Criado em: YYYY-MM-DD

## Resumo

<Total: N tasks. Paralelizáveis: M. Caminho crítico: T1 -> T3 -> T5.>

## Dependências

```mermaid
graph TD
    T1[T1: Entidade] --> T3[T3: Use case]
    T2[T2: Port]     --> T3
    T3              --> T4[T4: Repository]
    T4              --> T5[T5: Rota]
    T3              --> T6[T6: Testes]
```

## Tasks

### T1: <título curto> `[P]`

- **REQ cobertos:** 1, 2
- **Arquivos:** `src/domain/entities/foo.py` (novo)
- **Reuso:** `src/domain/entities/example.py` (template)
- **Depends on:** -
- **Done when:**
  - [ ] Entidade criada como `dataclass`
  - [ ] Tipos completos
- **Tests:** `poetry run pytest tests/unit/domain/entities/test_foo.py -v`
- **Gate:** `make unit` passa
- **Status:** pending | in-progress | done | blocked
```

---

## Marcadores

- `[P]` — paralelizável (não depende de nenhuma task in-progress)
- `[SEQ]` — sequencial (bloqueia tasks seguintes)
- `[GATE]` — gate obrigatório antes de continuar o pipeline
