---
name: quick-mode
description: Atalho do SDD para mudanças pequenas (<= 3 arquivos, uma sentença). Use para bug fix simples, config change, ajuste pontual ou correção trivial.
---

# Quick Mode — Atalho SDD

> Para mudanças pequenas, pula o pipeline completo.
> Limite: <= 3 arquivos OU uma sentença de escopo.
> Acima disso, usar [`spec-driven-design`](../spec-driven-design/SKILL.md).

---

## Quando usar

- Bug fix simples (1-3 arquivos).
- Config change (`config/development.env`, `pyproject.toml`).
- Ajuste de docstring / comentário.
- Adição de validação simples.
- Pequeno ajuste de teste.

**NÃO usar quando:**
- Mais de 3 arquivos são tocados.
- Adiciona entidade, port, adapter, use case, rota ou integração nova.
- Toca contrato HTTP, schema MongoDB ou padrão arquitetural.

---

## Estrutura

```text
.specs/quick/NNN-<slug>/
├── TASK.md       # Antes de implementar
└── SUMMARY.md    # Depois de implementar
```

`NNN` = número sequencial zero-padded (`001`, `002`, ...).
`slug` = kebab-case curto.

---

## Fluxo

### 1. Criar `TASK.md`

```markdown
# task: <slug>

> Quick mode
> Criado em: YYYY-MM-DD

## O que

<Uma sentença: o que será mudado e por quê.>

## Arquivos esperados

- `src/path/file_1.py`
- `tests/unit/path/test_file_1.py`

## Como verificar

- `make unit` passa
- `<comando específico>` produz resultado esperado
```

### 2. Implementar

- Só tocar arquivos listados.
- Se mais arquivos precisarem mudar → **parar** e usar [`spec-driven-design`](../spec-driven-design/SKILL.md).

### 3. Verificar

Rodar o gate definido em `Como verificar`.

### 4. Criar `SUMMARY.md`

```markdown
# summary: <slug>

> Quick mode
> Concluído em: YYYY-MM-DD

## O que foi feito

<Uma sentença descrevendo o que foi alterado.>

## Arquivos modificados

- `src/path/file_1.py` — <o que mudou>

## Resultado

- `make unit` passa
```
