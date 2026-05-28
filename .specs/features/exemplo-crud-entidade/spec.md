# spec: exemplo-crud-entidade

> Status: draft
> Escopo: medium
> Criado em: YYYY-MM-DD

## Goal

Implementar CRUD completo para `ExampleEntity` com endpoint REST, use case, repository MongoDB e testes.

## Requirements

1. `POST /examples` cria uma nova entidade e retorna `{id, name, description, active, created_at}`.
2. `GET /examples/{id}` retorna a entidade ou 404.
3. `GET /examples` lista entidades com paginação (`limit`, `skip`).
4. `DELETE /examples/{id}` remove a entidade ou retorna 404.

## Constraints

- Do NOT adicionar autenticação neste primeiro ciclo.
- Do NOT alterar a entidade `ExampleEntity` existente em `src/domain/entities/example.py`.
- Do NOT usar Pydantic na camada Domain.

## Acceptance criteria

- `make unit` passa com cobertura dos 4 endpoints.
- `POST /examples` retorna 201 com `id` no body.
- `GET /examples/id-inexistente` retorna 404.
- `DELETE /examples/id-existente` retorna 204.

## Context

- Entidade: [`src/domain/entities/example.py`](../../../src/domain/entities/example.py)
- Port: [`src/domain/repositories/example_repository.py`](../../../src/domain/repositories/example_repository.py)
- Arquitetura: [`.specs/codebase/ARCHITECTURE.md`](../../codebase/ARCHITECTURE.md)
