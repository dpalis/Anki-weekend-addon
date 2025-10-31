"""
Core logic for Weekend Blocker addon.
Manages deck configurations and automatic weekend blocking.
"""

from typing import Dict, List

from aqt import mw
from aqt.deckconf import DeckConf

from .utils import (
    get_addon_config,
    get_day_name,
    is_weekend,
    log_action,
    save_addon_config,
    show_tooltip,
)


def get_all_deck_configs() -> Dict[int, dict]:
    """
    Get all deck configurations with their new cards per day settings.

    Returns:
        dict: Dictionary mapping config_id to config data
    """
    if not mw or not mw.col:
        return {}

    configs = {}
    all_config = mw.col.decks.all_config()

    for config in all_config:
        config_id = config["id"]
        # In Anki 2.1.50+, new card settings are under 'new' key
        new_cards_per_day = config.get("new", {}).get("perDay", 20)
        configs[config_id] = {
            "name": config.get("name", f"Config {config_id}"),
            "new_per_day": new_cards_per_day,
            "full_config": config
        }

    return configs


def save_original_limits() -> None:
    """
    Save the original 'new cards per day' limits for all deck configs.
    This is done only once, on first run, to preserve user settings.
    """
    config = get_addon_config()

    # Only save if we don't have original limits yet
    if config.get("original_limits"):
        return

    deck_configs = get_all_deck_configs()
    original_limits = {}

    for config_id, deck_config in deck_configs.items():
        original_limits[str(config_id)] = deck_config["new_per_day"]

    config["original_limits"] = original_limits
    save_addon_config(config)

    log_action(
        "Saved original limits",
        {"original_limits": original_limits}
    )


def set_new_cards_limit(limit: int, dry_run: bool = False) -> List[str]:
    """
    Set the new cards per day limit for all deck configurations.

    Args:
        limit: The new limit to set (0 to block new cards)
        dry_run: If True, only simulate the changes without applying

    Returns:
        List of messages describing what was changed
    """
    if not mw or not mw.col:
        return ["Error: Anki collection not available"]

    changes = []
    all_config = mw.col.decks.all_config()

    for config in all_config:
        config_id = config["id"]
        config_name = config.get("name", f"Config {config_id}")
        current_limit = config.get("new", {}).get("perDay", 20)

        if current_limit != limit:
            if not dry_run:
                # Update the configuration
                config["new"]["perDay"] = limit
                mw.col.decks.update_config(config)

            changes.append(
                f"{config_name}: {current_limit} → {limit}"
            )

    if not dry_run and changes:
        mw.col.decks.flush()
        log_action(
            f"Set new cards limit to {limit}",
            {"changes": changes}
        )

    return changes


def apply_weekend_block() -> None:
    """
    Apply weekend blocking: set new cards per day to 0.
    """
    changes = set_new_cards_limit(0)

    if changes:
        message = f"🚫 Fim de semana: Novos cards bloqueados\n\n"
        message += f"Hoje: {get_day_name()}\n\n"
        message += f"Alterações:\n" + "\n".join(changes)
        show_tooltip(message, duration=5000)
    else:
        show_tooltip(f"✓ Novos cards já estão bloqueados ({get_day_name()})")


def restore_weekday_limits() -> None:
    """
    Restore original new cards per day limits for weekdays.
    """
    config = get_addon_config()
    original_limits = config.get("original_limits", {})

    if not original_limits:
        show_tooltip("⚠️ Nenhum backup de configurações encontrado")
        return

    if not mw or not mw.col:
        return

    changes = []
    all_config = mw.col.decks.all_config()

    for deck_config in all_config:
        config_id = str(deck_config["id"])
        config_name = deck_config.get("name", f"Config {config_id}")

        if config_id in original_limits:
            original_limit = original_limits[config_id]
            current_limit = deck_config.get("new", {}).get("perDay", 0)

            if current_limit != original_limit:
                deck_config["new"]["perDay"] = original_limit
                mw.col.decks.update_config(deck_config)
                changes.append(f"{config_name}: {current_limit} → {original_limit}")

    if changes:
        mw.col.decks.flush()
        log_action(
            "Restored weekday limits",
            {"changes": changes}
        )

        message = f"✓ Dia de semana: Novos cards liberados\n\n"
        message += f"Hoje: {get_day_name()}\n\n"
        message += f"Restaurado:\n" + "\n".join(changes)
        show_tooltip(message, duration=5000)
    else:
        show_tooltip(f"✓ Configurações já estão corretas ({get_day_name()})")


def pause_all_new_cards() -> None:
    """
    Manually pause all new cards (useful for vacations).
    """
    config = get_addon_config()
    config["manual_pause"] = True
    save_addon_config(config)

    changes = set_new_cards_limit(0)

    message = "⏸️ MODO MANUAL: Novos cards pausados\n\n"
    if changes:
        message += "Alterações:\n" + "\n".join(changes)
    else:
        message += "Novos cards já estavam em 0"

    show_tooltip(message, duration=5000)
    log_action("Manual pause activated")


def resume_all_new_cards() -> None:
    """
    Resume new cards from manual pause.
    """
    config = get_addon_config()
    config["manual_pause"] = False
    save_addon_config(config)

    restore_weekday_limits()
    log_action("Manual pause deactivated")


def run_automatic_check(show_feedback: bool = False) -> None:
    """
    Run the automatic weekend check.
    This is the main function called on profile load.

    Args:
        show_feedback: If True, shows user feedback messages
    """
    config = get_addon_config()

    # Check if addon is enabled
    if not config.get("enabled", True):
        if show_feedback:
            show_tooltip("⚠️ Addon está desativado")
        return

    # Save original limits on first run
    save_original_limits()

    # If manual pause is active, keep new cards at 0
    if config.get("manual_pause", False):
        if show_feedback:
            show_tooltip("⏸️ Modo pausa manual está ativo - novos cards bloqueados")
        set_new_cards_limit(0)
        return

    # Apply weekend logic
    if is_weekend():
        apply_weekend_block()
        if show_feedback and not is_weekend():
            # Only show if we actually applied changes
            pass  # apply_weekend_block already shows tooltip
    else:
        restore_weekday_limits()
        if show_feedback and is_weekend():
            # Only show if we actually applied changes
            pass  # restore_weekday_limits already shows tooltip

    # Update last run timestamp
    import datetime
    config["last_run"] = datetime.datetime.now().isoformat()
    save_addon_config(config)


def get_status_info() -> str:
    """
    Get current status information for display.

    Returns:
        str: Formatted status message
    """
    config = get_addon_config()
    deck_configs = get_all_deck_configs()

    status = f"📊 Weekend Blocker - Status\n\n"
    status += f"Hoje: {get_day_name()}\n"
    status += f"Fim de semana: {'✅' if is_weekend() else '❌'}\n"
    status += f"Addon ativo: {'✅' if config.get('enabled', True) else '❌'}\n"
    status += f"Pausa manual: {'✅' if config.get('manual_pause', False) else '❌'}\n\n"

    status += "Configurações de decks:\n"
    for config_id, deck_config in deck_configs.items():
        name = deck_config["name"]
        current = deck_config["new_per_day"]
        original = config.get("original_limits", {}).get(str(config_id), "?")

        # Format the deck info more clearly
        status += f"  • {name}\n"
        status += f"      Atual: {current} novos cards/dia\n"
        status += f"      Backup: {original} novos cards/dia\n"

    return status
