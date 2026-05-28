# CONVENTIONS — Padrões de código

> Convenções adotadas no projeto. Atualizar quando uma nova convenção for oficialmente adotada.

---

## Nomenclatura

| Tipo                    | Convenção            | Exemplo                              |
|-------------------------|----------------------|--------------------------------------|
| Arquivos Python         | `snake_case.py`      | `create_user.py`                     |
| Classes                 | `PascalCase`         | `CreateUserUseCase`                  |
| Funções/métodos         | `snake_case`         | `find_by_email()`                    |
| Variáveis               | `snake_case`         | `user_id`                            |
| Constantes              | `UPPER_SNAKE_CASE`   | `MAX_RETRIES = 3`                    |
| Membros privados        | `_prefixado`         | `self._db_client`                    |
| Use case                | `{Acao}{Entidade}UseCase` | `CreateUserUseCase`             |
| Input/Output use case   | `{Acao}{Entidade}Input/Output` | `CreateUserInput`          |
| Repository port         | `I{Entidade}Repository` | `IUserRepository`                 |
| Repository impl         | `MongoDB{Entidade}Repository` | `MongoDBUserRepository`      |

---

## Estrutura de use case

```python
class CreateExampleInput(BaseModel):
    name: str
    description: Optional[str] = None

class CreateExampleOutput(BaseModel):
    id: str
    name: str

class CreateExampleUseCase:
    def __init__(self, repository: IExampleRepository):
        self.repository = repository

    async def execute(self, input_data: CreateExampleInput) -> CreateExampleOutput:
        logger.info("[CREATE_EXAMPLE] name=%s", input_data.name)
        ...
```

---

## Logging

- `logger = logging.getLogger(__name__)` por módulo.
- Prefixo `[NOME_USE_CASE]` em todos os logs de use case.
- Níveis: `ERROR` para falhas, `WARNING` para negado/ignorado, `INFO` para sucesso.

---

## Type hints

- Obrigatórios em parâmetros e retorno de todas as funções.
- `Optional[T]` para valores anuláveis.
- Evitar `Any` a menos que estritamente necessário.

---

## Async

- Todas as operações de I/O (DB, HTTP) devem usar `async/await`.
- Use `AsyncMock` nos testes para métodos async.

---

## Imports

- Ordem: stdlib → terceiros → locais (separados por linha em branco).
- Imports absolutos a partir de `src`: `from src.domain.entities.example import ExampleEntity`.
- Evitar imports circulares.

---

## Formatação

- Linha: 88 caracteres (ruff/black).
- Formatador: `ruff format`.
- Linter: `ruff check`.
