# .specs/ — Spec-Driven Design

> **Metodologia:** Spec-Driven Design (SDD).
> **Fonte de verdade:** especificações versionadas em git substituem prompts ad-hoc.
> **Regra de ouro:** o spec compila para código. Quando código e spec divergem, o spec deve ser atualizado **no mesmo PR**.

---

## Filosofia

Em vez de "prompt-and-pray", trabalhamos em ciclos de **4 fases** explícitas:

```text
SPECIFY  -->  DESIGN  -->  TASKS  -->  EXECUTE
required      optional*     optional*    required

* Auto-pulado pelo agente quando o escopo não exige.
```

O agente decide a **profundidade** do pipeline a partir da complexidade da feature:

| Escopo  | Critério                          | Specify       | Design   | Tasks    | Execute |
|---------|-----------------------------------|---------------|----------|----------|---------|
| Small   | <= 3 arquivos, uma sentença       | Quick mode    | -        | -        | -       |
| Medium  | Feature clara, < 10 tasks         | Brief         | inline   | implicit | sim     |
| Large   | Multi-componente                  | Full + IDs    | sim      | sim      | sim     |
| Complex | Ambiguidade, domínio novo         | Full + discuss| research | parallel | UAT     |

Specify e Execute são **sempre obrigatórios**. Design e Tasks são pulados quando não agregam.

---

## Estrutura

```text
.specs/
├── project/            # Constitutional: identidade, rumo e memória
│   ├── PROJECT.md      # Visão, objetivos, princípios não-negociáveis
│   ├── ROADMAP.md      # Features e milestones
│   └── STATE.md        # Decisões, blockers, lessons, todos, ideas
├── codebase/           # Brownfield mapping (estado atual)
│   ├── STACK.md
│   ├── ARCHITECTURE.md
│   ├── STRUCTURE.md
│   ├── CONVENTIONS.md
│   ├── TESTING.md
│   ├── INTEGRATIONS.md
│   ├── PERSISTENCE.md
│   ├── SECURITY.md
│   ├── RUNTIME.md
│   ├── AUDIT.md
│   ├── PERMISSIONS.md
│   ├── HTTP_API.md
│   └── CONCERNS.md
├── features/           # Specs por feature (ciclo SDD)
│   └── [slug-feature]/
│       ├── spec.md     # Goal, Requirements, Constraints, Acceptance
│       ├── context.md  # (opcional) Decisões do usuário em gray areas
│       ├── design.md   # (Large/Complex) Arquitetura e componentes
│       └── tasks.md    # (Large/Complex) Tarefas atômicas com gates
└── quick/              # Quick mode (<= 3 arquivos)
    └── NNN-slug/
        ├── TASK.md
        └── SUMMARY.md
```

---

## Workflow

### Projeto novo (greenfield)

1. Inicializar `PROJECT.md` + `ROADMAP.md`.
2. Para cada feature: Specify -> (Design) -> (Tasks) -> Execute.

### Projeto existente (brownfield)

1. `codebase/` mapeia o estado atual.
2. Manter `PROJECT.md` e `ROADMAP.md` atualizados a cada milestone.
3. Para cada feature nova: criar `features/<slug>/spec.md` antes do código.
4. Mudanças triviais (<= 3 arquivos) vão para `quick/NNN-slug/`.
