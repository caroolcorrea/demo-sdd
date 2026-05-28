---
name: specify-feature
description: Cria spec.md de uma feature seguindo Spec-Driven Design (Goal, Requirements, Constraints, Acceptance). Use quando o usuário pedir para criar um spec, especificar uma feature, definir requisitos ou iniciar uma feature pelo SDD.
---

# Specify Feature — Fase 1 do SDD

> Cria `.specs/features/<slug>/spec.md` com requisitos rastreáveis e critérios de aceite executáveis.
> Esta skill **não implementa código**. Só especifica.

---

## Quando usar

- Usuário pediu "criar spec da feature X"
- Orquestrador [`spec-driven-design`](../spec-driven-design/SKILL.md) chamou esta fase

Para mudanças pequenas (<= 3 arquivos), usar [`quick-mode`](../quick-mode/SKILL.md).

---

## Passo a passo

### Passo 1 — Definir slug e criar diretório

Slug em kebab-case, descritivo:
- Bom: `add-pagination-examples`, `fix-duplicate-ids`, `extract-email-service`
- Ruim: `feature-1`, `nova-feature`

Criar: `.specs/features/<slug>/spec.md`

### Passo 2 — Avaliar escopo

| Escopo  | Spec format                                                   |
|---------|---------------------------------------------------------------|
| Medium  | Goal + Requirements + Constraints + Acceptance (10-30 linhas) |
| Large   | + Requirement IDs (REQ-1, REQ-2...) + Context expandido       |
| Complex | + Discussão de gray areas em `context.md`                     |

### Passo 3 — Escrever o spec

```markdown
# spec: <slug>

> Status: draft | approved | implementing | done | archived
> Escopo: medium | large | complex
> Criado em: YYYY-MM-DD

## Goal

<Uma sentença clara descrevendo o que será entregue.>

## Requirements

1. <Requisito 1 — verificável>
2. <Requisito 2 — verificável>

## Constraints

- Do NOT <coisa que o agente NÃO deve fazer>
- Do NOT <outra>

## Acceptance criteria

- `make unit` passa
- `<comando específico>` retorna resultado esperado
- `poetry run pytest tests/unit/path -v` passa

## Context

- Arquivos relevantes: `src/...`
- Spec relacionada: `../outra-feature/spec.md`
```

### Passo 4 — Stop point

Apresentar o spec ao usuário. Aguardar aprovação antes de prosseguir para Design ou Execute.

---

## Gray areas

Se houver ambiguidade que não pode ser decidida sem o usuário:
1. Criar `context.md` no mesmo diretório com as perguntas.
2. Aguardar respostas antes de finalizar o spec.
