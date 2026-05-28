# INTEGRATIONS — APIs externas

> Integrações com serviços externos. Atualizar quando adicionar nova API ou adapter.

---

## Padrão `BaseHttpRepository`

Toda integração HTTP segue o padrão de `BaseHttpRepository`:

```python
class BaseHttpRepository:
    def __init__(self, base_url: str, timeout: int = 30):
        self._base_url = base_url
        self._timeout = timeout

    async def _request(self, method: str, path: str, **kwargs) -> dict:
        async with httpx.AsyncClient(base_url=self._base_url, timeout=self._timeout) as client:
            response = await client.request(method, path, **kwargs)
            response.raise_for_status()
            return response.json()
```

---

## Integrações existentes

| Serviço | Adapter | URL env var |
|---------|---------|-------------|
| *(nenhuma ainda)* | — | — |

---

## Regras

- NUNCA instanciar HTTP client dentro de use case — usar repository injetado.
- Mapear resposta externa para entidade/DTO no adapter (não na rota).
- Timeout explícito em toda chamada HTTP.
- Tratar erros HTTP (4xx, 5xx) e converter para `ApplicationException` apropriada.
