# Weekend Blocker

Um addon para Anki que bloqueia automaticamente novos cards aos finais de semana (sábado e domingo), permitindo apenas cards de revisão.

## 🎯 Funcionalidades

- ✅ **Bloqueio Automático**: Novos cards não aparecem aos sábados e domingos
- ✅ **Revisões Normais**: Cards de revisão aparecem normalmente nos fins de semana
- ✅ **Sincronização**: Funciona em todos os dispositivos via AnkiWeb (Mac, iOS, Web)
- ✅ **Modo Manual**: Pause todos os novos cards para viagens
- ✅ **Seguro**: Não modifica seus cards, apenas configurações de deck
- ✅ **Backup Automático**: Salva suas configurações originais

## 📦 Instalação

### Método 1: Instalação Manual (Recomendado para desenvolvimento)

1. Localize a pasta de addons do Anki:
   - **Mac**: `~/Library/Application Support/Anki2/addons21/`
   - **Windows**: `%APPDATA%\Anki2\addons21\`
   - **Linux**: `~/.local/share/Anki2/addons21/`

2. Copie a pasta `weekend_blocker` para a pasta de addons

3. Reinicie o Anki

4. O addon estará ativo automaticamente

### Método 2: Via Anki (quando publicado)

1. Abra o Anki
2. Tools → Add-ons → Get Add-ons...
3. Digite o código do addon: `[código será gerado ao publicar]`
4. Clique em OK

## 🚀 Como Usar

### Uso Automático (Padrão)

O addon funciona automaticamente! Toda vez que você abrir o Anki:

- **Sábado/Domingo**: Novos cards são bloqueados (limite = 0)
- **Segunda a Sexta**: Novos cards aparecem normalmente (valores restaurados)

**Importante**: Abra o Anki no Mac pelo menos **2 vezes por semana**:
- 1x entre quinta-feira e sábado (para bloquear o fim de semana)
- 1x entre domingo e segunda-feira (para desbloquear a semana)

### Menu do Addon

Acesse: **Tools → Weekend Blocker**

#### Opções Disponíveis:

- **📊 Ver Status**: Mostra o estado atual do addon e configurações de decks
- **▶️ Executar Verificação Agora**: Força uma verificação imediata
- **⏸️ Pausar Todos os Novos Cards**: Modo manual para viagens
- **▶️ Retomar Novos Cards**: Sai do modo manual
- **🔄 Restaurar Configurações Originais**: Restaura valores salvos na primeira execução
- **⚙️ Ativar/Desativar Addon**: Liga ou desliga o addon
- **📖 Ajuda**: Mostra ajuda detalhada

### Modo Manual (para Viagens)

Quando você viajar ou não quiser novos cards por um período:

1. **Tools → Weekend Blocker → Pausar Todos os Novos Cards**
2. Confirme a ação
3. Sincronize com AnkiWeb
4. Todos os novos cards ficarão bloqueados até você reativar

Para reativar:
1. **Tools → Weekend Blocker → Retomar Novos Cards**
2. O addon voltará ao modo automático

## 🔧 Como Funciona

### Tecnicamente

1. O addon detecta o dia da semana usando o horário do sistema
2. Nos fins de semana, altera a configuração "new cards per day" para 0
3. Nos dias de semana, restaura os valores originais
4. Na primeira execução, salva um backup das configurações originais
5. Todas as mudanças sincronizam via AnkiWeb para todos os dispositivos

### Por que funciona no iOS?

- O addon roda apenas no Mac/PC (iOS não suporta addons)
- **MAS** as configurações de deck sincronizam via AnkiWeb
- Quando você abre o Anki no iOS, ele vê as configurações já modificadas
- Por isso é importante abrir no Mac 2x por semana

## 🛡️ Segurança

### O que o addon modifica?

✅ **Apenas configurações de deck** ("new cards per day")

### O que o addon NÃO modifica?

❌ Conteúdo dos cards
❌ Histórico de revisões
❌ Intervalos de cards
❌ Dados de progresso

### Backup e Restauração

- Na **primeira execução**, o addon salva todas as configurações originais
- Você pode restaurar a qualquer momento: **Tools → Weekend Blocker → Restaurar Configurações Originais**
- Todas as ações são registradas em `actions.log`

## 🧪 Testando com Segurança

Antes de usar no seu perfil principal:

1. **Crie um perfil de teste**:
   - File → Switch Profile → Add
   - Nome: "Teste Weekend Blocker"

2. **Adicione alguns cards de teste**

3. **Teste o addon**:
   - Verifique o status
   - Teste pausar/retomar
   - Simule diferentes dias da semana (pode temporariamente modificar o código)

4. **Quando estiver confortável**:
   - Volte ao seu perfil principal
   - O addon funcionará da mesma forma

## 📊 Logs e Debug

O addon registra todas as ações em: `weekend_blocker/actions.log`

Cada entrada contém:
- Timestamp
- Ação realizada
- Dia da semana
- Detalhes das mudanças

Para ver os logs:
1. Vá até a pasta do addon
2. Abra `actions.log` em um editor de texto

## ⚙️ Configurações Avançadas

Acesse: **Tools → Add-ons → Weekend Blocker → Config**

```json
{
    "enabled": true,              // Ativa/desativa o addon
    "original_limits": {},        // Backup das configurações (preenchido automaticamente)
    "manual_pause": false,        // Estado do modo manual
    "last_run": null,            // Última execução
    "log_actions": true          // Ativar logging
}
```

## ❓ Perguntas Frequentes

### O addon funciona no AnkiDroid?

Não diretamente (AnkiDroid não suporta addons Python), mas as **configurações sincronizam** via AnkiWeb, então o comportamento será o mesmo.

### Posso usar em alguns decks apenas?

Atualmente o addon aplica a todos os decks. Se precisar de customização, você pode editar o código em `core.py`.

### E se eu esquecer de abrir no Mac?

Se você só usar o iOS em uma semana sem abrir no Mac, os novos cards poderão aparecer (ou não aparecer) dependendo da última configuração sincronizada. Tente manter a rotina de abrir 2x por semana.

### Posso mudar os dias (ex: bloquear segunda também)?

Sim! Edite o arquivo `utils.py` e modifique a função `is_weekend()`:

```python
def is_weekend() -> bool:
    today = datetime.datetime.now().weekday()
    # 0=Monday, 1=Tuesday, ..., 5=Saturday, 6=Sunday
    return today in [5, 6]  # Modifique esta linha
```

### O addon afeta meus cards existentes?

**Não!** O addon apenas modifica a configuração de quantos novos cards aparecem por dia. Seus cards, histórico e progresso ficam intactos.

## 🐛 Problemas?

Se algo der errado:

1. **Restaure as configurações**: Tools → Weekend Blocker → Restaurar Configurações Originais
2. **Verifique os logs**: Abra `actions.log` para ver o que aconteceu
3. **Desative temporariamente**: Tools → Weekend Blocker → Ativar/Desativar Addon
4. **Contato**: [Adicione seu email ou GitHub aqui]

## 📝 Licença

MIT License - Sinta-se livre para modificar e distribuir

## 🙏 Créditos

Desenvolvido para David Palis com assistência da Claude (Anthropic)

---

**Versão**: 1.0.0
**Compatibilidade**: Anki 2.1.50+
**Plataformas**: Mac, Windows, Linux (sincroniza com iOS/Android/Web)
