---
name: state-management
description: Atualiza .specs/project/STATE.md (memória persistente do projeto) com decisões, blockers, lessons, todos transversais ou ideias deferidas. Use quando disser "registrar decisão", "anotar blocker", "lesson learned" ou ao final de uma feature relevante.
---

# State Management — Memória persistente

> Atualiza `.specs/project/STATE.md` com decisões, blockers, lessons, todos e ideas.
> O STATE é o que sobrevive entre sessões e PRs.

---

## Categorias

| Categoria | ID prefix | Quando usar                                                           |
|-----------|-----------|-----------------------------------------------------------------------|
| Decision  | `D-NNN`   | Decisão técnica que afeta múltiplas features ou cria precedente       |
| Blocker   | `B-NNN`   | Obstáculo que bloqueia uma feature ou ambiente                        |
| Lesson    | `L-NNN`   | Aprendizado de incidente, bug em prod, falha de design                |
| TODO      | `T-NNN`   | Trabalho transversal sem feature específica                           |
| Idea      | `I-NNN`   | Ideia futura sem prioridade definida                                  |

---

## Formatos

### Decision

```markdown
### D-NNN — <título curto>

**Contexto:** <o que motivou a decisão>
**Decisão:** <o que foi decidido>
**Trade-off:** <o que se sacrifica>
**Impacto:** <áreas do código afetadas>
**Referência:** <link para spec, rule, PR>
```

### Blocker

```markdown
### B-NNN — <título curto>

**Sintoma:** <o que está quebrado ou bloqueado>
**Impacto:** <features/ambientes afetados>
**Mitigação atual:** <workaround, se houver>
**Resolução planejada:** <quando/como; ou "aberto">
```

### Lesson

```markdown
### L-NNN — <título curto>

**O que aconteceu:** <incidente ou falha>
**Causa raiz:** <por que aconteceu>
**Lição:** <o que aprendemos>
**Ação:** <mudança no processo ou código>
```

### Idea

```markdown
### I-NNN — <título curto>

**Ideia:** <descrição em 1-2 linhas>
**Status:** não priorizado
```

---

## Fluxo

1. Ler `.specs/project/STATE.md`.
2. Pegar o maior ID da categoria + 1.
3. Inserir a nova entry na seção correta.
4. IDs são **estáveis** — nunca renumerar.
