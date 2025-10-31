"""
UI components for Weekend Blocker addon.
Creates menus and dialogs for user interaction.
"""

from typing import Callable, Optional

from aqt import mw
from aqt.qt import QAction, QMenu
from aqt.utils import askUser, showInfo

from .core import (
    get_status_info,
    pause_all_new_cards,
    restore_weekday_limits,
    resume_all_new_cards,
    run_automatic_check,
)
from .utils import get_addon_config, save_addon_config, show_info, show_tooltip


# Global variable to store the menu reference
_weekend_blocker_menu: Optional[QMenu] = None


def rebuild_menu() -> None:
    """
    Rebuild the menu to reflect current state.
    Called after actions that change the config.
    """
    global _weekend_blocker_menu

    if not mw or not _weekend_blocker_menu:
        return

    # Clear the existing menu
    _weekend_blocker_menu.clear()

    # Get current state to show relevant options
    config = get_addon_config()
    is_paused = config.get("manual_pause", False)
    is_enabled = config.get("enabled", True)

    # Rebuild menu actions
    add_menu_action(_weekend_blocker_menu, "📊 Ver Status", show_status_dialog)
    _weekend_blocker_menu.addSeparator()

    add_menu_action(_weekend_blocker_menu, "▶️ Executar Verificação Agora", run_manual_check)
    _weekend_blocker_menu.addSeparator()

    # Show only the relevant pause/resume option
    if is_paused:
        add_menu_action(_weekend_blocker_menu, "▶️ Retomar Novos Cards", resume_new_cards_action)
    else:
        add_menu_action(_weekend_blocker_menu, "⏸️ Pausar Todos os Novos Cards", pause_new_cards_action)

    _weekend_blocker_menu.addSeparator()

    add_menu_action(_weekend_blocker_menu, "🔄 Restaurar Configurações Originais", restore_settings_action)

    # Show only the relevant enable/disable option
    if is_enabled:
        add_menu_action(_weekend_blocker_menu, "❌ Desativar Addon", disable_addon_action)
    else:
        add_menu_action(_weekend_blocker_menu, "✅ Ativar Addon", enable_addon_action)

    _weekend_blocker_menu.addSeparator()

    add_menu_action(_weekend_blocker_menu, "📖 Ajuda", show_help_dialog)


def create_menu() -> None:
    """
    Create the Weekend Blocker menu in Anki's Tools menu.
    """
    global _weekend_blocker_menu

    if not mw:
        return

    # Create main menu
    _weekend_blocker_menu = QMenu("Weekend Blocker", mw)

    # Connect to aboutToShow signal to rebuild menu dynamically
    _weekend_blocker_menu.aboutToShow.connect(rebuild_menu)

    # Initial build
    rebuild_menu()

    # Add menu to Tools
    mw.form.menuTools.addMenu(_weekend_blocker_menu)


def add_menu_action(menu: QMenu, text: str, callback: Callable) -> QAction:
    """
    Add an action to a menu.

    Args:
        menu: The menu to add the action to
        text: The action text
        callback: Function to call when action is triggered

    Returns:
        QAction: The created action
    """
    action = QAction(text, mw)
    action.triggered.connect(callback)
    menu.addAction(action)
    return action


def show_status_dialog() -> None:
    """
    Show a dialog with current status information.
    """
    status = get_status_info()
    show_info(status)


def run_manual_check() -> None:
    """
    Manually trigger the weekend check.
    """
    run_automatic_check(show_feedback=True)


def pause_new_cards_action() -> None:
    """
    Pause all new cards (manual mode for vacations).
    """
    confirm = askUser(
        "Isso irá pausar TODOS os novos cards até você reativá-los manualmente.\n\n"
        "Útil para viagens ou períodos sem estudo.\n\n"
        "Deseja continuar?",
        title="Pausar Novos Cards"
    )

    if confirm:
        pause_all_new_cards()


def resume_new_cards_action() -> None:
    """
    Resume new cards from manual pause.
    """
    config = get_addon_config()

    if not config.get("manual_pause", False):
        show_tooltip("ℹ️ Pausa manual não está ativa")
        return

    confirm = askUser(
        "Isso irá retomar os novos cards e aplicar a lógica automática de fim de semana.\n\n"
        "Deseja continuar?",
        title="Retomar Novos Cards"
    )

    if confirm:
        resume_all_new_cards()


def restore_settings_action() -> None:
    """
    Restore all deck configurations to their original values.
    """
    confirm = askUser(
        "Isso irá restaurar as configurações de 'novos cards por dia' "
        "para os valores originais salvos na primeira execução.\n\n"
        "Use esta opção apenas se algo der errado.\n\n"
        "Deseja continuar?",
        title="Restaurar Configurações"
    )

    if confirm:
        restore_weekday_limits()


def disable_addon_action() -> None:
    """
    Disable the addon.
    """
    confirm = askUser(
        "Isso irá DESATIVAR o addon Weekend Blocker.\n\n"
        "O addon não fará mais verificações automáticas.\n\n"
        "Deseja continuar?",
        title="Desativar Addon"
    )

    if confirm:
        config = get_addon_config()
        config["enabled"] = False
        save_addon_config(config)
        show_tooltip("❌ Weekend Blocker desativado")


def enable_addon_action() -> None:
    """
    Enable the addon.
    """
    confirm = askUser(
        "Isso irá ATIVAR o addon Weekend Blocker.\n\n"
        "O addon voltará a fazer verificações automáticas.\n\n"
        "Deseja continuar?",
        title="Ativar Addon"
    )

    if confirm:
        config = get_addon_config()
        config["enabled"] = True
        save_addon_config(config)
        show_tooltip("✅ Weekend Blocker ativado")
        run_automatic_check()


def show_help_dialog() -> None:
    """
    Show help information.
    """
    help_text = """
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
<li>Abra o Anki no Mac <b>pelo menos 2x por semana</b></li>
<li>Sincronize após abrir para que o iOS veja as mudanças</li>
<li>O addon só roda no Mac, mas sincroniza com todos os dispositivos</li>
</ul>

<h3>Segurança</h3>
<p>O addon <b>não modifica seus cards</b>, apenas as configurações de deck.
Na primeira execução, ele salva seus valores originais para poder
restaurá-los depois.</p>

<h3>Problemas?</h3>
<p>Use <b>"Restaurar Configurações Originais"</b> para voltar ao estado inicial.</p>
"""

    showInfo(help_text, title="Weekend Blocker - Ajuda", textFormat="rich")
