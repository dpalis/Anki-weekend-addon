# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Weekend Blocker** is an Anki addon that automatically blocks new cards on weekends (Saturday and Sunday) while allowing review cards to appear normally. The addon runs on desktop (Mac/Windows/Linux) and syncs configuration changes via AnkiWeb to mobile devices (iOS/Android).

## Architecture

### Core Components

The addon follows a modular architecture with clear separation of concerns:

1. **`__init__.py`** - Entry point that registers GUI hooks and initializes the addon
2. **`core.py`** - Business logic for detecting weekends and managing deck configurations
3. **`ui.py`** - GUI components (menus, dialogs) for user interaction
4. **`utils.py`** - Helper functions for date detection, logging, and Anki API wrappers

### Key Design Decisions

**Why modify deck configs instead of card scheduling?**
- New cards in Anki don't have traditional "due dates" like review cards
- Modifying the "new cards per day" setting in deck configurations is the cleanest approach
- This change syncs automatically via AnkiWeb to all devices

**Persistence Strategy:**
- Original deck configurations are saved to `config.json` on first run
- This allows restoration if something goes wrong
- The addon is idempotent - running it multiple times has the same effect

**Hook Usage:**
- `gui_hooks.profile_did_open` is the primary trigger
- Executes on every profile load (app startup and profile switches)
- This ensures the weekend check runs at least when the user opens Anki

## Development Commands

### Testing the Weekend Logic

Run the standalone test script (doesn't require Anki):

```bash
python3 test_weekend_check.py
```

This validates the weekend detection logic and shows a week simulation.

### Installing for Development

Copy the addon to Anki's addon directory:

```bash
# Mac
cp -r weekend_blocker ~/Library/Application\ Support/Anki2/addons21/

# Then restart Anki
```

### Viewing Logs

The addon creates an `actions.log` file in its directory:

```bash
tail -f ~/Library/Application\ Support/Anki2/addons21/weekend_blocker/actions.log
```

### Debugging

Enable Anki's debug console: **Help → Toggle Debug Console**

The addon catches exceptions and prints them, so check the console for errors.

## Anki API Usage

### Accessing Deck Configurations

```python
# Get all deck configs
all_configs = mw.col.decks.all_config()

# Modify a config
config["new"]["perDay"] = 0
mw.col.decks.update_config(config)

# Persist changes
mw.col.decks.flush()
```

### Addon Configuration

```python
# Read config
config = mw.addonManager.getConfig(__name__)

# Write config
mw.addonManager.writeConfig(__name__, config)
```

### GUI Hooks

```python
from aqt import gui_hooks

# Profile loaded hook
gui_hooks.profile_did_open.append(callback_function)
```

## Important Constraints

### Version Compatibility

- **Minimum**: Anki 2.1.50+ (uses modern deck config API)
- **Tested on**: Anki 25.02.7 (Mac)
- The addon uses the v3 scheduler API structure

### Platform Support

- **Desktop**: Full functionality (Mac, Windows, Linux)
- **Mobile**: Configuration syncs via AnkiWeb, but addon logic doesn't run
- Users must open desktop app at least 2x per week for consistent behavior

### Configuration Structure (Anki 2.1.50+)

Deck configs use this structure:

```python
config = {
    "id": 1,
    "name": "Default",
    "new": {
        "perDay": 20,  # This is what we modify
        # ... other settings
    },
    # ... other sections
}
```

## Testing Strategy

### Safe Testing Approach

1. **Never test on the user's main profile first**
2. Create a test profile: File → Switch Profile → Add
3. Add sample cards to the test profile
4. Verify the addon behavior
5. Check that original settings are preserved

### What to Test

- Weekend detection (Saturday/Sunday)
- Weekday restoration (Monday-Friday)
- Manual pause/resume functionality
- Configuration backup and restore
- Menu actions and dialogs

## Common Pitfalls

### Don't Modify Card Objects Directly

❌ **Wrong**: Changing card.due or card.queue directly
✅ **Right**: Modifying deck configuration options

### Don't Forget to Flush

After updating deck configs, always call:

```python
mw.col.decks.flush()
```

### Handle Missing Collections Gracefully

Always check if `mw` and `mw.col` exist before accessing:

```python
if not mw or not mw.col:
    return
```

## File Structure

```
weekend_blocker/
├── __init__.py           # Entry point, registers hooks
├── core.py              # Main logic (detect weekend, modify configs)
├── ui.py                # GUI menus and dialogs
├── utils.py             # Helpers (date, logging, config)
├── config.json          # Default configuration
├── config.md            # Configuration documentation
├── manifest.json        # Addon metadata (Anki 2.1.49+)
└── README.md            # User documentation

# Repository root files
├── INSTALLATION.md       # Installation guide
├── test_weekend_check.py # Standalone testing script
└── CLAUDE.md            # This file
```

## Future Enhancement Ideas

If asked to extend functionality:

- Allow per-deck configuration (some decks always active, some weekend-blocked)
- Configurable days (e.g., block Mondays too)
- Vacation mode with date range
- Statistics tracking (cards blocked over time)
- AnkiWeb sync trigger (run check after sync completes)

## Support and Maintenance

When debugging issues:

1. Check `actions.log` for recorded actions
2. Verify `config.json` has correct `original_limits` saved
3. Use "Restore Original Settings" to recover from bad states
4. Check Anki version compatibility (minimum 2.1.50)
5. Ensure the user understands the 2x per week requirement
