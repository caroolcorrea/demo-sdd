# ROADMAP — demo-sdd

> Marcos atuais, em andamento e planejados. Atualizar quando entregar uma feature ou redefinir prioridade.

---

## Status

- Última revisão: 2026-05-28
- Branch principal: `main`

---

## Milestones entregues

| Milestone                         | Status | Spec relacionada                                        |
|-----------------------------------|--------|---------------------------------------------------------|
| Bootstrap FastAPI + DI            | done   | [`../codebase/ARCHITECTURE.md`](../codebase/ARCHITECTURE.md) |
| Estrutura SDD completa            | done   | [`../README.md`](../README.md)                          |
| Rules e Skills base               | done   | [`/.cursor/rules/`](../../.cursor/rules/)               |

---

## Em andamento

| Feature / refator | Owner       | Observação                            |
|-------------------|-------------|---------------------------------------|
| CRUD de exemplo   | Engenharia  | Demonstrar ciclo SDD completo         |

---

## Backlog priorizado

### Curto prazo

1. **Feature CRUD completo** com spec, design, tasks e testes.
2. **Autenticação JWT** básica.
3. **Cobertura > 80%** em `make coverage`.

### Médio prazo

1. **Paginação padronizada** em rotas de listagem.
2. **OpenAPI com exemplos completos** por endpoint.

---

## Convenções para entradas neste roadmap

Cada feature adicionada deve apontar para um `spec.md` em `.specs/features/<slug>/`,
exceto quando for mudança pequena (usa `.specs/quick/`).
