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
