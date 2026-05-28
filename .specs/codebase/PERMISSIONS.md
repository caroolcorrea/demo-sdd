# PERMISSIONS — Controle de acesso

> Modelo de permissões. Atualizar quando adicionar role, ação ou decorator.

---

## Modelo atual

*(A ser definido conforme features são adicionadas.)*

---

## Padrão de decorator de permissão

```python
# src/infrastructure/entrypoint/http/decorators.py

def require_permission(role: str):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            request = kwargs.get("request")
            user = request.state.user
            if not user.has_role(role):
                raise PermissionDeniedException()
            return await func(*args, **kwargs)
        return wrapper
    return decorator
```

---

## Regras

- Toda rota que modifica estado deve ter verificação de permissão explícita.
- Auditar todas as negações de permissão.
- `access_level` numérico: quanto maior, mais privilegiado.
