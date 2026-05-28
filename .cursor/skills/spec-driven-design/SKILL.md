---
name: spec-driven-design
description: Orquestrador do pipeline Spec-Driven Design (Specify -> Design -> Tasks -> Execute). Use quando o usuário pedir para iniciar uma feature, refator ou mudança relevante, ou disser "criar spec", "planejar feature", "spec driven", "SDD".
---

# Spec-Driven Design — Orquestrador

> Pipeline de planejamento e execução baseado em especificações. Auto-sizing por complexidade.
> Constitution do projeto: [`.specs/project/PROJECT.md`](../../../.specs/project/PROJECT.md).

---

## Quando esta skill é o ponto de entrada

- "Vamos planejar/iniciar a feature X"
- "Criar spec para Y"
- "Como vamos refatorar Z?"
- "Spec driven design", "SDD"

Para mudanças pequenas (<= 3 arquivos), ir direto para [`quick-mode`](../quick-mode/SKILL.md).

---

## Pipeline

```text
SPECIFY  -->  DESIGN  -->  TASKS  -->  EXECUTE
required      optional*     optional*    required
```

---

## Auto-sizing

| Escopo  | Critério                                     | Specify       | Design   | Tasks    | Execute |
|---------|----------------------------------------------|---------------|----------|----------|---------|
| Small   | <= 3 arquivos, uma sentença                  | Quick mode    | -        | -        | -       |
| Medium  | Feature clara, < 10 tasks                    | brief         | inline   | implicit | sim     |
| Large   | Multi-componente                             | full + IDs    | sim      | sim      | sim     |
| Complex | Ambiguidade, domínio novo, integração nova   | full + discuss| research | parallel | UAT     |

### Como classificar

1. **Quantos arquivos** são tocados? (1-3 = Small; 4-10 = Medium; 10+ = Large)
2. **Quantas camadas** (domain, application, infrastructure, tests)? (1 = Small/Medium; 3+ = Large)
3. **Há decisões arquiteturais novas**? Se sim, Large/Complex.
4. **Há ambiguidade no requisito**? Se sim, Complex (ativa discuss mode).

---

## Workflow

### Fase 1 — Specify (sempre)

Ler [`specify-feature/SKILL.md`](../specify-feature/SKILL.md).

Output: `.specs/features/<slug>/spec.md` com:
- Goal, Requirements, Constraints, Acceptance criteria, Context.

**Stop point:** revisar o spec com o usuário antes de seguir.

---

### Fase 2 — Design (Large/Complex)

Ler [`design-feature/SKILL.md`](../design-feature/SKILL.md).

Pular se: nenhuma decisão arquitetural nova; caminho óbvio a partir do spec.

Output: `.specs/features/<slug>/design.md`.

---

### Fase 3 — Tasks (Large/Complex)

Ler [`tasks-breakdown/SKILL.md`](../tasks-breakdown/SKILL.md).

Pular se: Medium com 3-5 passos lineares.

Output: `.specs/features/<slug>/tasks.md`.

---

### Fase 4 — Execute (sempre)

Ler [`implement-validate/SKILL.md`](../implement-validate/SKILL.md).

Implementar task por task. Gate por task. Validar contra acceptance criteria ao final.

---

## Atualização pós-feature

Ao final de cada feature:

1. Atualizar `codebase/` se mudou contrato — skill [`brownfield-mapping`](../brownfield-mapping/SKILL.md).
2. Registrar decisão no STATE se relevante — skill [`state-management`](../state-management/SKILL.md).
3. Atualizar ROADMAP com status `done`.
4. Commit — skill [`commit-push`](../commit-push/SKILL.md).
