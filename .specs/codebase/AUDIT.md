# AUDIT — Auditoria de operações

> Padrão de auditoria para operações sensíveis. Atualizar quando adicionar AuditAction ou mudar fluxo.

---

## Conceito

Toda operação de escrita relevante (POST, PUT, DELETE) deve ser auditada com:
- `who`: usuário que executou
- `what`: ação (AuditAction enum)
- `when`: timestamp
- `input`: dados de entrada
- `output`: dados de saída / resultado
- `status`: `success` | `error`

---

## Padrão (decorator `@audit`)

```python
from src.application.audit import audit, AuditAction

class CreateExampleUseCase:
    @audit(AuditAction.CREATE_EXAMPLE)
    async def execute(self, input_data: CreateExampleInput) -> CreateExampleOutput:
        ...
```

O decorator captura before/after state e persiste em `audit_logs`.

---

## Collection `audit_logs`

```json
{
  "_id": ObjectId,
  "action": "create_example",
  "user_id": "...",
  "timestamp": "2026-01-01T00:00:00Z",
  "input": {...},
  "output": {...},
  "status": "success"
}
```

> **Contrato congelado**: não alterar campos sem migração e aprovação explícita.

---

## Regras

- Persistência exclusiva via `@audit` em `execute()` de use cases.
- Middleware **não** persiste audit log.
- Auditar sucesso **e** falha.
- Payload é contrato congelado após definido.
