# PERSISTENCE — MongoDB, collections e índices

> Collections existentes. Atualizar quando adicionar collection, índice ou seed.

---

## Configuração

- URL: `MONGODB_URL` (env var)
- Database: `MONGODB_DB` (env var, default: `demo_db_{APP_ENV}`)
- Driver: Motor async (`motor.motor_asyncio`)

---

## Collections

| Collection | Modelo          | Descrição                  |
|------------|-----------------|----------------------------|
| *(nenhuma ainda)* | —          | —                          |

---

## Padrão de documento

```python
{
    "_id": ObjectId,
    "name": str,
    "active": bool,
    "_created": datetime,
    "_updated": datetime,
    "_version": int  # incrementar a cada update
}
```

---

## Padrão de índices

Definir índices no bootstrap (lifespan do app):

```python
await collection.create_index("field", unique=True)
await collection.create_index([("field_a", 1), ("field_b", -1)])
```

---

## Regras

- `_id` sempre `ObjectId` — nunca usar string como `_id`.
- `_version` incrementado a cada `update`.
- `_updated` atualizado a cada `update`.
- `_created` imutável após inserção.
