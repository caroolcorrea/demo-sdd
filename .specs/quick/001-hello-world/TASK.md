# task: 001-hello-world

> Quick mode
> Criado em: 2026-05-28

## O que

Adicionar rota `GET /hello` que retorna `{"message": "Hello, World!"}` como smoke test do bootstrap.

## Arquivos esperados

- `src/infrastructure/entrypoint/http/routes/hello.py`
- `src/main.py` (include_router)
- `tests/unit/test_hello_route.py`

## Como verificar

- `make unit` passa
- `curl http://localhost:8000/hello` retorna `{"message": "Hello, World!"}`
