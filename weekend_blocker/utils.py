"""
Utility functions for Weekend Blocker addon.
Handles logging, date detection, and helper functions.
"""

import datetime
import json
import os
from typing import Optional

from aqt import mw


def get_anki_language() -> str:
    """
    Get the current Anki interface language.

    Returns:
        str: Language code (e.g., 'en', 'pt', 'es')
    """
    if not mw or not mw.pm:
        return "en"  # Default to English

    # Get language from Anki preferences
    lang = mw.pm.meta.get("defaultLang", "en")

    # Normalize language code (e.g., 'pt_BR' -> 'pt')
    if "_" in lang:
        lang = lang.split("_")[0]

    # Map to supported languages (currently 'pt' and 'en')
    if lang.startswith("pt"):
        return "pt"
    else:
        return "en"  # Default to English for all other languages


def is_weekend() -> bool:
    """
    Check if today is Saturday (5) or Sunday (6).

    Returns:
        bool: True if today is weekend, False otherwise
    """
    today = datetime.datetime.now().weekday()
    return today in [5, 6]  # Saturday=5, Sunday=6


def get_day_name() -> str:
    """
    Get the current day name in the user's language.

    Returns:
        str: Localized day name
    """
    from .translations import get_translation

    day_keys = {
        0: "day_monday",
        1: "day_tuesday",
        2: "day_wednesday",
        3: "day_thursday",
        4: "day_friday",
        5: "day_saturday",
        6: "day_sunday"
    }

    weekday = datetime.datetime.now().weekday()
    return get_translation(day_keys[weekday])


def log_action(action: str, details: Optional[dict] = None) -> None:
    """
    Log an action to the addon's log file.

    Args:
        action: Description of the action taken
        details: Optional dictionary with additional details
    """
    if not mw or not mw.addonManager:
        return

    addon_dir = os.path.dirname(__file__)
    log_file = os.path.join(addon_dir, "actions.log")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        "timestamp": timestamp,
        "action": action,
        "day": get_day_name(),
        "is_weekend": is_weekend()
    }

    if details:
        log_entry["details"] = details

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"Weekend Blocker: Failed to write log: {e}")


def get_addon_config() -> dict:
    """
    Get the addon's configuration.

    Returns:
        dict: Configuration dictionary
    """
    if not mw or not mw.addonManager:
        return {}

    addon_name = os.path.basename(os.path.dirname(__file__))
    config = mw.addonManager.getConfig(addon_name)

    if config is None:
        config = {
            "enabled": True,
            "original_limits": {},
            "manual_pause": False,
            "last_run": None,
            "log_actions": True
        }

    return config


def save_addon_config(config: dict) -> None:
    """
    Save the addon's configuration.

    Args:
        config: Configuration dictionary to save
    """
    if not mw or not mw.addonManager:
        return

    addon_name = os.path.basename(os.path.dirname(__file__))
    mw.addonManager.writeConfig(addon_name, config)


def show_tooltip(message: str, duration: int = 3000) -> None:
    """
    Show a tooltip message to the user.

    Args:
        message: Message to display
        duration: Duration in milliseconds (default 3000ms = 3s)
    """
    from aqt.utils import tooltip
    tooltip(message, duration)


def show_info(message: str, title: str = "Weekend Blocker") -> None:
    """
    Show an info dialog to the user.

    Args:
        message: Message to display
        title: Dialog title
    """
    from aqt.utils import showInfo
    showInfo(message, title=title)


def show_warning(message: str, title: str = "Weekend Blocker") -> None:
    """
    Show a warning dialog to the user.

    Args:
        message: Warning message to display
        title: Dialog title
    """
    from aqt.utils import showWarning
    showWarning(message, title=title)
