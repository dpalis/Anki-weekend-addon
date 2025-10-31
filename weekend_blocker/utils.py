"""
Utility functions for Weekend Blocker addon.
Handles logging, date detection, and helper functions.
"""

import datetime
import json
import os
from typing import Optional

from aqt import mw


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
    Get the current day name in Portuguese.

    Returns:
        str: Day name (e.g., "Sábado", "Segunda-feira")
    """
    days = {
        0: "Segunda-feira",
        1: "Terça-feira",
        2: "Quarta-feira",
        3: "Quinta-feira",
        4: "Sexta-feira",
        5: "Sábado",
        6: "Domingo"
    }
    return days[datetime.datetime.now().weekday()]


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
