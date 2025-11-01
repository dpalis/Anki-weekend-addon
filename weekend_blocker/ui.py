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
from .translations import get_translation as tr


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
    add_menu_action(_weekend_blocker_menu, tr("menu_status"), show_status_dialog)
    _weekend_blocker_menu.addSeparator()

    add_menu_action(_weekend_blocker_menu, tr("menu_run_check"), run_manual_check)
    _weekend_blocker_menu.addSeparator()

    # Show only the relevant pause/resume option
    if is_paused:
        add_menu_action(_weekend_blocker_menu, tr("menu_resume"), resume_new_cards_action)
    else:
        add_menu_action(_weekend_blocker_menu, tr("menu_pause"), pause_new_cards_action)

    _weekend_blocker_menu.addSeparator()

    add_menu_action(_weekend_blocker_menu, tr("menu_restore"), restore_settings_action)

    # Show only the relevant enable/disable option
    if is_enabled:
        add_menu_action(_weekend_blocker_menu, tr("menu_disable"), disable_addon_action)
    else:
        add_menu_action(_weekend_blocker_menu, tr("menu_enable"), enable_addon_action)

    _weekend_blocker_menu.addSeparator()

    add_menu_action(_weekend_blocker_menu, tr("menu_help"), show_help_dialog)


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
        tr("confirm_pause"),
        title=tr("title_pause")
    )

    if confirm:
        pause_all_new_cards()


def resume_new_cards_action() -> None:
    """
    Resume new cards from manual pause.
    """
    config = get_addon_config()

    if not config.get("manual_pause", False):
        show_tooltip(tr("tooltip_pause_inactive"))
        return

    confirm = askUser(
        tr("confirm_resume"),
        title=tr("title_resume")
    )

    if confirm:
        resume_all_new_cards()


def restore_settings_action() -> None:
    """
    Restore all deck configurations to their original values.
    """
    confirm = askUser(
        tr("confirm_restore"),
        title=tr("title_restore")
    )

    if confirm:
        restore_weekday_limits()


def disable_addon_action() -> None:
    """
    Disable the addon.
    """
    confirm = askUser(
        tr("confirm_disable"),
        title=tr("title_disable")
    )

    if confirm:
        config = get_addon_config()
        config["enabled"] = False
        save_addon_config(config)
        show_tooltip(tr("tooltip_disabled"))


def enable_addon_action() -> None:
    """
    Enable the addon.
    """
    confirm = askUser(
        tr("confirm_enable"),
        title=tr("title_enable")
    )

    if confirm:
        config = get_addon_config()
        config["enabled"] = True
        save_addon_config(config)
        show_tooltip(tr("tooltip_enabled"))
        run_automatic_check()


def show_help_dialog() -> None:
    """
    Show help information.
    """
    help_text = tr("help_content")

    showInfo(help_text, title=tr("title_help"), textFormat="rich")
