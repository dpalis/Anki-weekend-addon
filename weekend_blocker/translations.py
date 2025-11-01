"""
Translation strings for Weekend Blocker addon.
Supports multiple languages with automatic detection from Anki settings.
"""

TRANSLATIONS = {
    "pt": {
        # Menu items
        "menu_status": "📊 Ver Status",
        "menu_run_check": "▶️ Executar Verificação Agora",
        "menu_pause": "⏸️ Pausar Todos os Novos Cards",
        "menu_resume": "▶️ Retomar Novos Cards",
        "menu_restore": "🔄 Restaurar Configurações Originais",
        "menu_disable": "❌ Desativar Addon",
        "menu_enable": "✅ Ativar Addon",
        "menu_help": "📖 Ajuda",

        # Dialog titles
        "title_pause": "Pausar Novos Cards",
        "title_resume": "Retomar Novos Cards",
        "title_restore": "Restaurar Configurações",
        "title_disable": "Desativar Addon",
        "title_enable": "Ativar Addon",
        "title_help": "Weekend Blocker - Ajuda",

        # Confirmation messages
        "confirm_pause": "Isso irá pausar TODOS os novos cards até você reativá-los manualmente.\n\nÚtil para viagens ou períodos sem estudo.\n\nDeseja continuar?",
        "confirm_resume": "Isso irá retomar os novos cards e aplicar a lógica automática de fim de semana.\n\nDeseja continuar?",
        "confirm_restore": "Isso irá restaurar as configurações de 'novos cards por dia' para os valores originais salvos na primeira execução.\n\nUse esta opção apenas se algo der errado.\n\nDeseja continuar?",
        "confirm_disable": "Isso irá DESATIVAR o addon Weekend Blocker.\n\nO addon não fará mais verificações automáticas.\n\nDeseja continuar?",
        "confirm_enable": "Isso irá ATIVAR o addon Weekend Blocker.\n\nO addon voltará a fazer verificações automáticas.\n\nDeseja continuar?",

        # Status messages
        "status_title": "📊 Weekend Blocker - Status",
        "status_today": "Hoje",
        "status_weekend": "Fim de semana",
        "status_enabled": "Addon ativo",
        "status_manual_pause": "Pausa manual",
        "status_deck_configs": "Configurações de decks",
        "status_current": "Atual",
        "status_backup": "Backup",
        "status_cards_per_day": "novos cards/dia",

        # Tooltip messages
        "tooltip_pause_inactive": "ℹ️ Pausa manual não está ativa",
        "tooltip_disabled": "❌ Weekend Blocker desativado",
        "tooltip_enabled": "✅ Weekend Blocker ativado",
        "tooltip_no_backup": "⚠️ Nenhum backup de configurações encontrado",
        "tooltip_already_blocked": "✓ Novos cards já estão bloqueados",
        "tooltip_already_correct": "✓ Configurações já estão corretas",
        "tooltip_addon_disabled": "⚠️ Addon está desativado",
        "tooltip_manual_pause_active": "⏸️ Modo pausa manual está ativo - novos cards bloqueados",

        # Weekend block messages
        "weekend_blocked_title": "🚫 Fim de semana: Novos cards bloqueados",
        "weekend_buried": "Cards enterrados",
        "weekend_changes": "Alterações",

        # Weekday restore messages
        "weekday_restored_title": "✓ Dia de semana: Novos cards liberados",
        "weekday_unburied": "Cards desenterrados",
        "weekday_restored": "Restaurado",

        # Day names
        "day_monday": "Segunda-feira",
        "day_tuesday": "Terça-feira",
        "day_wednesday": "Quarta-feira",
        "day_thursday": "Quinta-feira",
        "day_friday": "Sexta-feira",
        "day_saturday": "Sábado",
        "day_sunday": "Domingo",

        # Help content
        "help_content": """
<h2>Weekend Blocker - Ajuda</h2>

<h3>O que este addon faz?</h3>
<p>Bloqueia automaticamente novos cards aos <b>sábados e domingos</b>,
permitindo apenas revisões. De segunda a sexta, os novos cards
aparecem normalmente.</p>

<h3>Como funciona?</h3>
<ul>
<li>Quando você abre o Anki, o addon verifica o dia da semana</li>
<li>Se for fim de semana: define "novos cards por dia" = 0</li>
<li>Se for dia de semana: restaura os valores originais</li>
<li>As mudanças sincronizam com AnkiWeb e aparecem no iOS</li>
</ul>

<h3>Modo Manual (Viagens)</h3>
<p>Use <b>"Pausar Todos os Novos Cards"</b> para bloquear novos cards
temporariamente, independente do dia. Útil para viagens!</p>

<p>Use <b>"Retomar Novos Cards"</b> quando voltar.</p>

<h3>Importante</h3>
<ul>
<li>Abra o Anki no Mac/PC <b>pelo menos 2x por semana</b></li>
<li>Sincronize após abrir para que o iOS veja as mudanças</li>
<li>O addon só roda no desktop, mas sincroniza com todos os dispositivos</li>
</ul>

<h3>Segurança</h3>
<p>O addon <b>não modifica seus cards</b>, apenas as configurações de deck.
Na primeira execução, ele salva seus valores originais para poder
restaurá-los depois.</p>

<h3>Problemas?</h3>
<p>Use <b>"Restaurar Configurações Originais"</b> para voltar ao estado inicial.</p>
"""
    },

    "en": {
        # Menu items
        "menu_status": "📊 View Status",
        "menu_run_check": "▶️ Run Check Now",
        "menu_pause": "⏸️ Pause All New Cards",
        "menu_resume": "▶️ Resume New Cards",
        "menu_restore": "🔄 Restore Original Settings",
        "menu_disable": "❌ Disable Addon",
        "menu_enable": "✅ Enable Addon",
        "menu_help": "📖 Help",

        # Dialog titles
        "title_pause": "Pause New Cards",
        "title_resume": "Resume New Cards",
        "title_restore": "Restore Settings",
        "title_disable": "Disable Addon",
        "title_enable": "Enable Addon",
        "title_help": "Weekend Blocker - Help",

        # Confirmation messages
        "confirm_pause": "This will pause ALL new cards until you manually reactivate them.\n\nUseful for vacations or study breaks.\n\nDo you want to continue?",
        "confirm_resume": "This will resume new cards and apply automatic weekend logic.\n\nDo you want to continue?",
        "confirm_restore": "This will restore 'new cards per day' settings to the original values saved on first run.\n\nUse this option only if something goes wrong.\n\nDo you want to continue?",
        "confirm_disable": "This will DISABLE the Weekend Blocker addon.\n\nThe addon will no longer perform automatic checks.\n\nDo you want to continue?",
        "confirm_enable": "This will ENABLE the Weekend Blocker addon.\n\nThe addon will resume automatic checks.\n\nDo you want to continue?",

        # Status messages
        "status_title": "📊 Weekend Blocker - Status",
        "status_today": "Today",
        "status_weekend": "Weekend",
        "status_enabled": "Addon active",
        "status_manual_pause": "Manual pause",
        "status_deck_configs": "Deck configurations",
        "status_current": "Current",
        "status_backup": "Backup",
        "status_cards_per_day": "new cards/day",

        # Tooltip messages
        "tooltip_pause_inactive": "ℹ️ Manual pause is not active",
        "tooltip_disabled": "❌ Weekend Blocker disabled",
        "tooltip_enabled": "✅ Weekend Blocker enabled",
        "tooltip_no_backup": "⚠️ No configuration backup found",
        "tooltip_already_blocked": "✓ New cards are already blocked",
        "tooltip_already_correct": "✓ Settings are already correct",
        "tooltip_addon_disabled": "⚠️ Addon is disabled",
        "tooltip_manual_pause_active": "⏸️ Manual pause mode is active - new cards blocked",

        # Weekend block messages
        "weekend_blocked_title": "🚫 Weekend: New cards blocked",
        "weekend_buried": "Cards buried",
        "weekend_changes": "Changes",

        # Weekday restore messages
        "weekday_restored_title": "✓ Weekday: New cards enabled",
        "weekday_unburied": "Cards unburied",
        "weekday_restored": "Restored",

        # Day names
        "day_monday": "Monday",
        "day_tuesday": "Tuesday",
        "day_wednesday": "Wednesday",
        "day_thursday": "Thursday",
        "day_friday": "Friday",
        "day_saturday": "Saturday",
        "day_sunday": "Sunday",

        # Help content
        "help_content": """
<h2>Weekend Blocker - Help</h2>

<h3>What does this addon do?</h3>
<p>Automatically blocks new cards on <b>Saturdays and Sundays</b>,
allowing only reviews. From Monday to Friday, new cards
appear normally.</p>

<h3>How does it work?</h3>
<ul>
<li>When you open Anki, the addon checks the day of the week</li>
<li>If it's weekend: sets "new cards per day" = 0</li>
<li>If it's weekday: restores original values</li>
<li>Changes sync with AnkiWeb and appear on iOS</li>
</ul>

<h3>Manual Mode (Vacations)</h3>
<p>Use <b>"Pause All New Cards"</b> to block new cards
temporarily, regardless of the day. Useful for vacations!</p>

<p>Use <b>"Resume New Cards"</b> when you return.</p>

<h3>Important</h3>
<ul>
<li>Open Anki on your Mac/PC <b>at least twice per week</b></li>
<li>Sync after opening so iOS sees the changes</li>
<li>The addon only runs on desktop, but syncs with all devices</li>
</ul>

<h3>Safety</h3>
<p>The addon <b>does not modify your cards</b>, only deck settings.
On first run, it saves your original values so it can
restore them later.</p>

<h3>Problems?</h3>
<p>Use <b>"Restore Original Settings"</b> to return to the initial state.</p>
"""
    }
}


def get_supported_languages():
    """Get list of supported language codes."""
    return list(TRANSLATIONS.keys())


def get_translation(key: str, lang: str = None) -> str:
    """
    Get translated string for the given key.

    Args:
        key: Translation key
        lang: Language code (if None, will be auto-detected)

    Returns:
        Translated string, or key if not found
    """
    if lang is None:
        from .utils import get_anki_language
        lang = get_anki_language()

    # Fallback to English if language not supported
    if lang not in TRANSLATIONS:
        lang = "en"

    # Return translation or key if not found
    return TRANSLATIONS[lang].get(key, key)
