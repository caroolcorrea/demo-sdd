---
name: brownfield-mapping
description: Atualiza .specs/codebase/*.md (mapa do estado atual do código) quando o código muda contrato, schema, env var ou padrão arquitetural. Use ao final de uma feature SDD ou quando disser "atualizar codebase docs".
---

# Brownfield Mapping — Atualizar codebase/

> Mantém `.specs/codebase/` em sincronia com o código.
> Update obrigatório quando mudar contrato, schema, env, padrão ou integração.

---

## Quando usar

- Após feature SDD que mudou contrato HTTP, schema MongoDB, env var, etc.
- Após refactor que mudou padrão arquitetural.
- Quando descobrir divergência entre `codebase/*.md` e o código.

---

## Índice

| Arquivo          | Quando atualizar                                                          |
|------------------|---------------------------------------------------------------------------|
| `STACK.md`       | Subiu versão major, trocou ferramenta, mudou comando canônico             |
| `STRUCTURE.md`   | Adicionou/removeu top-level dir ou módulo relevante                       |
| `ARCHITECTURE.md`| Mudou camadas, bootstrap, DI ou padrão de fluxo                           |
| `CONVENTIONS.md` | Nova convenção adotada                                                    |
| `HTTP_API.md`    | Nova rota, novo padrão de erro, mudança em paginação                      |
| `SECURITY.md`    | Mudança em JWT/Auth, nova rota pública, mudança em CORS                   |
| `PERMISSIONS.md` | Nova role, novo decorator, mudança em access_level                        |
| `AUDIT.md`       | Nova AuditAction, mudança em payload, novo fluxo                          |
| `PERSISTENCE.md` | Nova collection, novo índice, novo seed                                   |
| `INTEGRATIONS.md`| Nova API externa, novo adapter HTTP                                       |
| `RUNTIME.md`     | Nova env var, mudança em deploy                                           |
| `TESTING.md`     | Novo marker, nova fixture global, mudança em comando de teste             |
| `CONCERNS.md`    | Novo concern identificado, ou concern resolvido                           |

---

## Fluxo

1. Identificar quais arquivos de `codebase/` foram afetados pela feature.
2. Ler o arquivo inteiro para entender tom e estrutura existente.
3. Aplicar update **incremental** — adicionar linha na tabela ou parágrafo curto.
4. Não recriar — editar o existente.

---

## Regras

- Atualizar **no mesmo PR** da feature.
- Tom: português claro, sem floreio.
- Tabelas para listas de itens, parágrafos curtos para padrões.
- Não duplicar informação já em rules ou specs de feature.
