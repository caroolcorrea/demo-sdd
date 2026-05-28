# HTTP_API — Superfície HTTP

> Rotas, padrões de resposta e erros. Atualizar quando adicionar rota ou mudar contrato.

---

## Prefixos de routers

| Prefixo   | Arquivo                                        | Tag       |
|-----------|------------------------------------------------|-----------|
| `/health` | `src/main.py`                                  | health    |

---

## Padrão de rota

```python
@router.get("/recurso/{id}", response_model=RecursoResponse)
async def get_recurso(id: str, request: Request):
    use_case = container.use_case.get_recurso_use_case()
    result = await use_case.execute(GetRecursoInput(id=id))
    if result is None:
        raise HTTPException(status_code=404, detail="Não encontrado")
    return result
```

---

## Formato de erro padronizado

```json
{
  "success": false,
  "error_code": "RESOURCE_NOT_FOUND",
  "message": "Resource '123' não encontrado",
  "details": null
}
```

| Status | Código             | Quando                              |
|--------|--------------------|-------------------------------------|
| 400    | VALIDATION_ERROR   | Parâmetros inválidos                |
| 403    | PERMISSION_DENIED  | Sem permissão                       |
| 404    | *_NOT_FOUND        | Recurso não encontrado              |
| 409    | CONFLICT           | Conflito de estado                  |
| 500    | INTERNAL_ERROR     | Erro interno não tratado            |

---

## Regras de OpenAPI

- `response_model=` obrigatório em todos os decorators de rota.
- `summary=` e `description=` para documentação legível.
- `status_code=` explícito para respostas não-200.
