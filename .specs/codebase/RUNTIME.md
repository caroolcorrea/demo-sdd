# RUNTIME — Deploy e variáveis de ambiente

> Configuração de runtime, deploy e env vars. Atualizar quando adicionar env var ou mudar deploy.

---

## Variáveis de ambiente

| Variável      | Obrigatória | Default          | Descrição                      |
|---------------|-------------|------------------|-------------------------------|
| `APP_ENV`     | não         | `development`    | Ambiente (`development`/`production`) |
| `SECRET_KEY`  | **sim**     | —                | Chave JWT HS256                |
| `MONGODB_URL` | **sim**     | `mongodb://localhost:27017` | URL de conexão MongoDB |
| `MONGODB_DB`  | não         | `demo_db_{APP_ENV}` | Nome do banco               |
| `HOST`        | não         | `0.0.0.0`        | Host do servidor               |
| `PORT`        | não         | `8000`           | Porta do servidor              |

---

## Ambiente local

```bash
# Arquivo: config/development.env
APP_ENV=development
SECRET_KEY=dev-secret-key
MONGODB_URL=mongodb://localhost:27017
```

Carregado automaticamente via `python-dotenv` em `src/settings.py`.

---

## Iniciar servidor

```bash
make run
# ou
poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

---

## Docker (futuro)

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-dev
COPY src/ ./src/
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
