# Changelog

All notable changes to Weekend Blocker will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features
- Per-deck configuration (allow some decks to always show new cards)
- Customizable blocked days (not just Saturday/Sunday)
- Date range vacation mode
- Statistics dashboard (cards blocked over time)
- Automatic sync trigger detection

## [1.1.0] - 2025-11-01

### Added
- ✨ **Multilingual support**: Addon now supports Portuguese and English
- 🌍 Automatic language detection from Anki interface settings
- 📝 All menus, dialogs, and messages are now translated
- 🔧 Easy to add new languages (all strings in single file)

### Changed
- Created `translations.py` module with PT and EN translations
- Added `get_anki_language()` function to detect user's language
- Updated all UI strings to use translation system
- Updated all core.py messages to use translation system
- Updated day names to be localized
- README now includes Translations section inviting contributions

### Technical Details
- New file: `translations.py` (~250 lines)
- Modified: `ui.py`, `core.py`, `utils.py` to use `tr()` function
- Supports easy addition of new languages via GitHub Issues
- Fallback to English for unsupported languages

## [1.0.1] - 2025-11-01

### Fixed
- **Critical**: Fixed issue where only some decks were being blocked on weekends
  - Now correctly modifies both deck configurations AND individual deck settings
  - Buries new cards already in today's queue (fixes cards appearing even after blocking)
  - Unburied cards automatically restored on weekdays
- Improved deck detection to handle all deck configuration scenarios
- Enhanced backup system to save both config-level and deck-level limits

### Changed
- `save_original_limits()`: Now saves both deck configs and individual deck overrides
- `set_new_cards_limit()`: Now modifies both deck configs and individual decks
- `restore_weekday_limits()`: Now restores both types of limits and unburied cards
- Added `bury_new_cards_in_queue()`: Buries new cards already scheduled for today
- Added `unbury_new_cards()`: Unburied cards on weekdays

### Technical Details
- Cards are now buried using `mw.col.sched.bury_cards()` to hide them from today's queue
- This ensures cards already loaded into the queue are hidden immediately
- Cards automatically unbury on weekdays when limits are restored

## [1.0.0] - 2025-10-31

### Added
- ✨ Automatic weekend detection (Saturday/Sunday)
- ✨ Automatic blocking of new cards on weekends
- ✨ Review cards remain available every day
- ✨ Manual pause mode for vacations
- ✨ Dynamic menu interface (shows only relevant options)
- ✨ Status dashboard with visual icons (✅/❌)
- ✨ Automatic backup of original deck configurations
- ✨ Action logging system
- ✨ Enable/disable addon functionality
- ✨ Restore original settings option
- ✨ Manual verification trigger
- ✨ Cross-platform sync via AnkiWeb
- 📚 Comprehensive documentation
- 📚 Installation guide
- 📚 User manual (Portuguese)
- 📚 Developer documentation (CLAUDE.md)
- 🛡️ Security audit completed
- 🧪 Test script for weekend detection

### Technical Details
- Minimum Anki version: 2.1.50+
- Compatible with Anki v3 scheduler
- Uses modern deck configuration API
- Supports Mac, Windows, Linux
- Configuration syncs to iOS, Android, Web via AnkiWeb

### Initial Release Features
1. **Automatic Mode**
   - Detects day of week using system time
   - Sets "new cards per day" to 0 on weekends
   - Restores original values on weekdays

2. **Manual Controls**
   - Pause/Resume all new cards
   - Enable/Disable addon
   - Restore original settings
   - View current status
   - Execute manual check

3. **Safety Features**
   - Automatic backup on first run
   - Action logging
   - Confirmation dialogs for destructive actions
   - Easy restoration of original settings
   - No modification of card data or review history

4. **User Interface**
   - Menu integration in Tools menu
   - Dynamic menu (updates based on state)
   - Status dialog with clear formatting
   - Help system with usage instructions
   - Visual feedback for all actions

### Files Included
- `__init__.py` - Entry point and hooks
- `core.py` - Business logic
- `ui.py` - User interface components
- `utils.py` - Helper functions
- `config.json` - Default configuration
- `config.md` - Configuration documentation
- `manifest.json` - Addon metadata
- `README.md` - User documentation

---

## Release Notes Template (for future versions)

## [X.Y.Z] - YYYY-MM-DD

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Features that will be removed in future versions

### Removed
- Features removed in this version

### Fixed
- Bug fixes

### Security
- Security vulnerability fixes

---

## Version History

- **1.0.0** (2025-10-31): Initial release

[Unreleased]: https://github.com/yourusername/anki-weekend-blocker/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/yourusername/anki-weekend-blocker/releases/tag/v1.0.0
