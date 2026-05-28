---
name: implement-validate
description: Executa tasks de uma feature do SDD com mudanças cirúrgicas e validação contra acceptance criteria. Use quando spec (e tasks.md, se houver) já estão aprovados e é hora de implementar.
---

# Implement + Validate — Fase 4 do SDD

> Implementa **uma task por vez** e valida contra o spec.
> Mudanças cirúrgicas. Sem scope creep. Gate por task. Validação final contra acceptance criteria.

---

## Fluxo

### Antes de começar

1. Carregar contexto mínimo:
   - `.specs/features/<slug>/spec.md`
   - `.specs/features/<slug>/design.md` (se existir)
   - `.specs/features/<slug>/tasks.md` (se existir)
   - `.specs/codebase/CONVENTIONS.md`
   - Rules sempre-ativas (clean-architecture, project-overview)

2. Confirmar lista de passos com o usuário.

3. Marcar primeira task como `in-progress`.

---

### Loop por task

Para cada task:

#### 1. Ler a task completa

- `REQ cobertos`, `Arquivos`, `Depends on`, `Done When`, `Gate`.

#### 2. Implementar — cirurgicamente

- **Só tocar arquivos listados na task.**
- **Reusar componentes existentes.** Verificar `src/` antes de criar.
- **Seguir convenções** de [`CONVENTIONS.md`](../../../.specs/codebase/CONVENTIONS.md).
- **Sem refactors fora do escopo.**
- **Sem "melhorias"** não pedidas.

#### 3. Aplicar skills técnicas

| Tipo de código     | Skill                                                |
|--------------------|------------------------------------------------------|
| Use case novo      | [`create-use-case`](../create-use-case/SKILL.md)     |
| Rota nova          | [`create-route`](../create-route/SKILL.md)           |
| Repository novo    | [`create-repository`](../create-repository/SKILL.md) |
| Teste              | [`create-test`](../create-test/SKILL.md)             |

#### 4. Rodar o gate da task

Comando exato definido no campo `Gate`.

#### 5. Marcar task como `done`

Atualizar `tasks.md` antes da próxima task.

---

### Ao final

1. Rodar todos os acceptance criteria do `spec.md`.
2. Atualizar status do spec para `done`.
3. Skill [`brownfield-mapping`](../brownfield-mapping/SKILL.md) se mudou contrato.
4. Skill [`commit-push`](../commit-push/SKILL.md).
