"""
Weekend Blocker - Anki Addon

Automatically blocks new cards on weekends (Saturday and Sunday),
while allowing review cards to appear normally.

Author: Created for David Palis
Version: 1.0.0
License: MIT
"""

from aqt import gui_hooks, mw

from .core import run_automatic_check
from .ui import create_menu


def on_profile_loaded() -> None:
    """
    Hook function called when a profile is loaded.
    Runs the automatic weekend check.
    """
    try:
        run_automatic_check()
    except Exception as e:
        print(f"Weekend Blocker error: {e}")
        import traceback
        traceback.print_exc()


def initialize_addon() -> None:
    """
    Initialize the addon by setting up menus and hooks.
    """
    # Create the menu in Tools
    create_menu()

    # Register hook for profile loading
    gui_hooks.profile_did_open.append(on_profile_loaded)


# Initialize when the module is loaded
if mw:
    initialize_addon()
