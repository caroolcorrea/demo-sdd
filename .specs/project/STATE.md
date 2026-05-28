# STATE — Memória persistente do projeto

> Decisões técnicas, blockers conhecidos, lessons learned, todos transversais e ideias deferidas.
> Atualizar ao registrar uma decisão relevante ou descobrir um trade-off importante.

---

## Como usar

- **Decision (D-NNN)**: decisão técnica importante com contexto e racional.
- **Blocker (B-NNN)**: obstáculo conhecido que afeta features ou refactors.
- **Lesson (L-NNN)**: aprendizado de incidente ou falha.
- **TODO (T-NNN)**: tarefa transversal que não se encaixa em uma feature.
- **Idea (I-NNN)**: ideia futura não priorizada.

Cada entry tem ID estável — referenciar por ID em PRs, specs e issues.

---

## Decisions

### D-001 — Spec-Driven Design para todas as features novas

**Contexto:** Sem metodologia explícita, mudanças eram conduzidas via prompt direto, gerando retrabalho.

**Decisão:** Adotar SDD. Toda feature nova passa por `spec.md` antes de código.
Mudanças pequenas (<= 3 arquivos) usam quick mode.

**Trade-off:** Overhead de spec para features pequenas é atenuado pelo auto-sizing (quick mode).
Para features grandes, o ROI é claro (menos retrabalho, review objetiva).

**Referência:** [`/.cursor/rules/spec-driven-design.mdc`](../../.cursor/rules/spec-driven-design.mdc).

---

### D-002 — Clean Architecture estrita com Ports & Adapters

**Contexto:** Sem separação de camadas, código tende a misturar lógica de negócio com infraestrutura.

**Decisão:** Adotar Clean Architecture — Domain ← Application ← Infrastructure.
Use cases recebem interfaces (ports) injetadas pelo container DI.

**Trade-off:** Mais arquivos e boilerplate inicial, mas testabilidade isolada e trocar infra sem afetar regras.

**Referência:** [`/.cursor/rules/clean-architecture.mdc`](../../.cursor/rules/clean-architecture.mdc).

---

## Blockers

*(nenhum registrado)*

---

## Lessons

*(nenhum registrado)*

---

## TODOs transversais

*(nenhum registrado)*

---

## Ideas

### I-001 — Plugin de geração de spec via CLI

**Ideia:** CLI `make spec feature=<slug>` que scaffolda `spec.md` com template pré-preenchido.

**Status:** não priorizado.
