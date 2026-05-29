# summary: remove-user-crud

> Quick mode
> Concluído em: 2026-05-29

## O que foi feito

Foram removidos resíduos de CRUD de usuários/exemplo em docs/specs e o roadmap foi ajustado para priorizar consolidação SDD.

## Arquivos modificados

- `.specs/features/exemplo-crud-entidade/spec.md` — removido por estar fora do foco atual.
- `.specs/project/ROADMAP.md` — removida a prioridade de CRUD e adicionado foco em SDD.
- `.specs/quick/002-remove-user-crud/TASK.md` — registrada a intenção da mudança.

## Resultado

- `git status --short` mostra a remoção do spec CRUD, o ajuste do roadmap e os artefatos quick mode.
- Busca em `.specs` não encontra feature ativa de CRUD fora deste registro.
- Resíduos locais não versionados de `tasks`/CRUD foram removidos quando presentes.
