# Guia de Instalação - Weekend Blocker

## 🚀 Instalação Rápida

### Passo 1: Localize a pasta de addons do Anki

Abra o Finder e pressione `Cmd + Shift + G`, depois cole o caminho:

```
~/Library/Application Support/Anki2/addons21/
```

### Passo 2: Copie o addon

1. Copie a pasta `weekend_blocker` deste repositório
2. Cole dentro da pasta `addons21/`

A estrutura final deve ficar assim:
```
~/Library/Application Support/Anki2/addons21/
└── weekend_blocker/
    ├── __init__.py
    ├── core.py
    ├── ui.py
    ├── utils.py
    ├── config.json
    ├── config.md
    ├── manifest.json
    └── README.md
```

### Passo 3: Reinicie o Anki

1. Feche o Anki completamente
2. Abra novamente
3. O addon será carregado automaticamente

### Passo 4: Verifique a instalação

1. Abra: **Tools → Weekend Blocker**
2. Clique em **📊 Ver Status**
3. Você deverá ver as informações do addon

## ✅ Pronto!

O addon agora está instalado e funcionando. Consulte o [README.md](weekend_blocker/README.md) para instruções de uso.

## 🧪 Testando Primeiro (Recomendado)

Antes de usar no seu perfil principal:

1. No Anki, vá em **File → Switch Profile → Add**
2. Crie um perfil chamado "Teste"
3. Adicione alguns cards de exemplo
4. Teste o addon neste perfil primeiro
5. Quando estiver satisfeito, use no perfil principal

## 🐛 Problemas na Instalação?

### O menu não aparece em Tools

1. Verifique se a pasta está no local correto
2. Abra: **Tools → Add-ons**
3. Procure por "weekend_blocker" na lista
4. Se não aparecer, pode haver um erro de sintaxe

### Como ver erros

1. Abra: **Tools → Add-ons**
2. Selecione "weekend_blocker"
3. Clique em "View Files"
4. Verifique se todos os arquivos estão presentes
5. Console de erros: **Help → Toggle Debug Console**

## 📁 Estrutura de Arquivos

```
weekend_blocker/
├── __init__.py           # Entry point (registra hooks)
├── core.py              # Lógica principal
├── ui.py                # Interface gráfica (menus)
├── utils.py             # Funções auxiliares
├── config.json          # Configurações padrão
├── config.md            # Documentação das configs
├── manifest.json        # Metadados do addon
└── README.md            # Documentação completa
```

## 🔄 Atualizando o Addon

Para atualizar para uma nova versão:

1. Faça backup das suas configurações (opcional):
   - Copie o arquivo `config.json` para um local seguro
2. Delete a pasta antiga `weekend_blocker`
3. Copie a nova versão para `addons21/`
4. Reinicie o Anki
5. Restaure suas configurações se necessário

## 🗑️ Desinstalando

1. Feche o Anki
2. Delete a pasta `weekend_blocker` de `addons21/`
3. Abra o Anki
4. As configurações de decks permanecerão como estavam na última sincronização

**Importante**: Se o addon estiver com novos cards bloqueados ao desinstalar, você precisará restaurar manualmente:
- Tools → Deck Options → New Cards → [ajuste o valor]
