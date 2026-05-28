# SECURITY — Auth e JWT

> Padrões de autenticação e autorização. Atualizar quando mudar fluxo de auth.

---

## Fluxo de autenticação

```
Cliente → Bearer JWT → AuthMiddleware → request.state.user → Rota
```

---

## JWT

- Algoritmo: HS256
- Secret: `SECRET_KEY` (env var)
- Payload: `{"sub": user_id, "email": email, "exp": ...}`

---

## Paths públicos (sem auth)

- `GET /health`
- `GET /docs`
- `GET /openapi.json`
- `GET /redoc`

---

## Headers de segurança

```
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
```

---

## CORS

Configurado em `src/main.py` via `CORSMiddleware`.
Em produção, restringir `allow_origins` a domínios específicos.

---

## Regras

- NUNCA armazene segredos no código — usar env vars.
- NUNCA logue tokens, JWT completo ou senhas.
- SEMPRE valide JWT antes de qualquer operação protegida.
- Use `Depends(get_current_user)` para endpoints autenticados.
