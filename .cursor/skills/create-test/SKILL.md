---
name: create-test
description: Use quando criar testes, adicionar cobertura ou escrever qualquer tipo de teste (unit, integration, smoke, property, e2e).
---

# Testing & QA — Python Backend

## Pirâmide de testes

```
          [E2E]              <- fluxo completo, lentos, use com moderação
       [Integration]         <- endpoints, repositórios, fluxos reais
    ████ Unit Tests ████      <- lógica isolada, ms, base da pirâmide
```

## Regra fundamental

> **Um teste que passa mesmo quando o código está errado é pior do que nenhum teste.**

Comente o `return` principal — o teste DEVE falhar. Se não falhar, descarte.

---

## Template: unit test de use case

```python
import pytest
from unittest.mock import AsyncMock, MagicMock

from src.application.use_cases.examples.create_example import (
    CreateExampleInput,
    CreateExampleUseCase,
)


@pytest.fixture
def mock_repository():
    repo = MagicMock()
    repo.save = AsyncMock(return_value="507f1f77bcf86cd799439011")
    return repo


@pytest.fixture
def use_case(mock_repository):
    return CreateExampleUseCase(repository=mock_repository)


class TestCreateExampleUseCase:
    async def test_execute_valid_input_returns_output(self, use_case, mock_repository):
        """Cenário: input válido. Expectativa: retorna output com id."""
        input_data = CreateExampleInput(name="Test", description="Desc")

        result = await use_case.execute(input_data)

        assert result.id == "507f1f77bcf86cd799439011"
        assert result.name == "Test"
        mock_repository.save.assert_called_once()

    async def test_execute_empty_name_raises_validation(self, use_case):
        """Cenário: nome vazio. Expectativa: ValidationException."""
        with pytest.raises(ValidationException):
            await use_case.execute(CreateExampleInput(name=""))
```

---

## Template: integration test de rota

```python
import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch

from src.main import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


class TestExamplesRoutes:
    def test_get_example_not_found_returns_404(self, client):
        response = client.get("/examples/000000000000000000000000")
        assert response.status_code == 404
        assert response.json()["error_code"] == "EXAMPLE_NOT_FOUND"
```

---

## Anti-padrões — Nunca faça

- **Over-mocking**: não mockar o método/classe sob teste.
- **Assert só de chamada**: sempre verificar resultado observável.
- **Testes duplicados**: usar `@pytest.mark.parametrize`.

## O que mockar

| Categoria     | Ação                               |
|---------------|------------------------------------|
| MongoDB       | `AsyncMock` na collection          |
| API externa   | `AsyncMock` no repository          |
| Tempo         | `freezegun.freeze_time`            |
| O próprio UC  | NUNCA                              |
