---
name: commit-push
description: Executa git add, commit e push seguindo conventional commits. Use quando o usuário pedir para commitar, dar push ou salvar alterações no git.
---

# Commit e Push

## Fluxo

1. **Verificar estado**: `git status`
2. **Lint + format**: `make lint` (ou `poetry run ruff check src tests && poetry run ruff format --check src/ tests/`)
3. **Testes**: `make unit`
4. **Stage**: `git add <arquivos>` ou `git add -A`
5. **Commit**: conventional commits (ver abaixo)
6. **Push**: `git push`

---

## Conventional Commits

```
<tipo>(<escopo opcional>): <descrição imperativa>

[corpo opcional]

[rodapé opcional]
```

### Tipos

| Tipo     | Quando usar                                        |
|----------|----------------------------------------------------|
| `feat`   | Nova funcionalidade                                |
| `fix`    | Correção de bug                                    |
| `refactor`| Refactor sem mudança de comportamento             |
| `test`   | Adiciona ou corrige testes                         |
| `docs`   | Apenas documentação                                |
| `chore`  | Build, deps, configs                               |
| `style`  | Formatação, lint (sem mudança de lógica)           |
| `perf`   | Melhoria de performance                            |
| `ci`     | Mudança em CI/CD                                   |

### Exemplos

```bash
git commit -m "feat(examples): add CRUD endpoints for ExampleEntity"
git commit -m "fix(auth): handle expired JWT gracefully"
git commit -m "test(use-cases): add unit tests for CreateExampleUseCase"
git commit -m "docs(specs): update codebase/HTTP_API.md with examples routes"
git commit -m "chore: bump fastapi to 0.115.5"
```

---

## Gate local antes do commit

```bash
# Lint
poetry run ruff check src tests
poetry run ruff format --check src/ tests/

# Testes unitários
make unit
```

Se qualquer passo falhar, corrigir antes do commit.
