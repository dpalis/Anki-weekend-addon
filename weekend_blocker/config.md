# Weekend Blocker - Configuração

Este arquivo documenta as opções de configuração do addon Weekend Blocker.

## Configurações Disponíveis

### `enabled`
- **Tipo:** boolean
- **Padrão:** `true`
- **Descrição:** Ativa ou desativa o addon. Quando desativado, nenhuma verificação automática é realizada.

### `original_limits`
- **Tipo:** object
- **Padrão:** `{}`
- **Descrição:** Armazena os valores originais de "novos cards por dia" para cada configuração de deck. Preenchido automaticamente na primeira execução. Usado para restaurar os valores quando necessário.
- **Formato:** `{ "config_id": valor_original }`

### `manual_pause`
- **Tipo:** boolean
- **Padrão:** `false`
- **Descrição:** Indica se o modo de pausa manual está ativo. Quando ativo, todos os novos cards são bloqueados independente do dia da semana. Útil para viagens.

### `last_run`
- **Tipo:** string (ISO date) ou null
- **Padrão:** `null`
- **Descrição:** Data e hora da última execução do addon. Usado para debugging e logs.

### `log_actions`
- **Tipo:** boolean
- **Padrão:** `true`
- **Descrição:** Se verdadeiro, registra todas as ações do addon no arquivo `actions.log`.

## Como Editar

Você pode editar estas configurações através do Anki:
1. Tools → Add-ons
2. Selecione "Weekend Blocker"
3. Clique em "Config"

Ou edite diretamente este arquivo JSON e reinicie o Anki.

## Restaurando Configurações Padrão

Para restaurar as configurações padrão:
1. Delete este arquivo `config.json`
2. Reinicie o Anki
3. O addon criará um novo arquivo com valores padrão
