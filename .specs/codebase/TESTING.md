# TESTING — Stack de testes

> Fonte de verdade: `pytest.ini`, `pyproject.toml`.

---

## Configuração

- Runner: **pytest** + **pytest-asyncio** (`asyncio_mode = auto` em `pytest.ini`)
- Paths: `pythonpath = ["src", "tests"]`, `testpaths = ["tests"]`
- Timeout padrão: 30s (`pytest-timeout`)
- Coverage gate: **80%** em `make coverage`

---

## Estrutura

```
tests/
├── conftest.py           # Fixtures globais, Hypothesis profiles
├── unit/                 # Espelha src/ — use cases, DTOs, rotas
├── integration/          # Endpoints HTTP, repositórios, fluxos
└── smoke/                # Validação mínima pós-deploy
```

---

## Comandos

```bash
make unit          # somente unit tests
make integration   # somente integration tests
make test-ci       # unit + integration + coverage report
make coverage      # gate 80%
```

---

## Convenção de nomes

```python
def test_<ação>_<cenário>_<resultado_esperado>():
    """Cenário: X. Expectativa: Y."""
```

---

## Anti-padrões — Nunca faça

- **Over-mocking**: não mockar o método/classe sob teste.
- **Assert só de chamada**: sempre verificar resultado observável.
- **Testes duplicados**: usar `@pytest.mark.parametrize` para variações.
- **Setup excessivo**: arrange mínimo; assert específico.

---

## Hypothesis (property-based)

- Marker: `@pytest.mark.property`
- Profiles: `demo` (local) e `ci` (CI)
- Usar em: funções puras, normalizers, mappers determinísticos.
- Não usar em: use cases com mocks pesados, rotas HTTP.
