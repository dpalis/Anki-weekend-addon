# Weekend Blocker for Anki

<div align="center">

![Anki](https://img.shields.io/badge/Anki-2.1.50+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Mac%20%7C%20Windows%20%7C%20Linux-lightgrey)

**Automatically block new cards on weekends while keeping reviews active**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [FAQ](#-faq) • [Contributing](#-contributing)

</div>

---

## 🎯 Overview

Weekend Blocker is an Anki addon that automatically prevents new cards from appearing on Saturdays and Sundays, while allowing review cards to show up normally. Perfect for maintaining a consistent study schedule during weekdays while taking weekends off from learning new material.

### Why Weekend Blocker?

- 📚 **Focus on Reviews**: Keep up with your review schedule on weekends without the pressure of new cards
- 🔄 **Automatic Syncing**: Works across all your devices (desktop and mobile) via AnkiWeb
- ⚙️ **Set and Forget**: Automatically manages your study schedule based on the day of the week
- ✈️ **Vacation Mode**: Manually pause all new cards for trips or busy periods
- 🛡️ **Safe**: Only modifies deck settings, never touches your cards or review history

## ✨ Features

- ✅ **Automatic Weekend Blocking**: New cards are blocked on Saturday and Sunday
- ✅ **Review Cards Always Available**: Review cards work normally every day
- ✅ **Cross-Platform Sync**: Configuration syncs via AnkiWeb to iOS, Android, and web
- ✅ **Manual Pause Mode**: Temporarily block all new cards for vacations
- ✅ **Dynamic Menu**: Shows only relevant options based on current state
- ✅ **Status Dashboard**: View current configuration and state at a glance
- ✅ **Automatic Backup**: Saves original settings before making any changes
- ✅ **Action Logging**: Tracks all changes for debugging and transparency

## 📦 Installation

### Method 1: From AnkiWeb (Recommended - when published)

1. Open Anki
2. Go to **Tools → Add-ons → Get Add-ons...**
3. Enter the addon code: `[code will be added upon publication]`
4. Click **OK** and restart Anki

### Method 2: Manual Installation

1. Download the latest release from [Releases](https://github.com/yourusername/anki-weekend-blocker/releases)
2. Open Anki and go to **Tools → Add-ons → Install from file...**
3. Select the downloaded `.ankiaddon` file
4. Restart Anki

### Method 3: From Source

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/anki-weekend-blocker.git
   ```

2. Copy the `weekend_blocker` folder to your Anki addons directory:
   - **Mac**: `~/Library/Application Support/Anki2/addons21/`
   - **Windows**: `%APPDATA%\Anki2\addons21\`
   - **Linux**: `~/.local/share/Anki2/addons21/`

3. Restart Anki

## 🚀 Usage

### Automatic Mode (Default)

The addon works automatically! Every time you open Anki:

- **Saturday/Sunday**: New cards are blocked (limit set to 0)
- **Monday-Friday**: New cards appear normally (limits restored)

**Important**: Open Anki on your desktop at least **twice per week**:
- Once between Thursday-Saturday (to block the weekend)
- Once between Sunday-Monday (to unblock the week)

### Manual Controls

Access the addon menu: **Tools → Weekend Blocker**

#### Available Options:

- **📊 Ver Status**: View current state and deck configurations
- **▶️ Executar Verificação Agora**: Manually trigger the weekend check
- **⏸️ Pausar Todos os Novos Cards**: Enable manual pause mode (for vacations)
- **▶️ Retomar Novos Cards**: Disable manual pause mode
- **🔄 Restaurar Configurações Originais**: Restore original deck settings
- **❌ Desativar Addon** / **✅ Ativar Addon**: Toggle addon on/off
- **📖 Ajuda**: View help information

### Vacation Mode

Going on vacation? Pause all new cards:

1. **Tools → Weekend Blocker → Pausar Todos os Novos Cards**
2. Confirm the action
3. Sync with AnkiWeb
4. All new cards will remain blocked until you resume

To resume:
1. **Tools → Weekend Blocker → Retomar Novos Cards**
2. The addon returns to automatic weekend detection

## 🔧 How It Works

### Technical Overview

1. The addon detects the day of the week using system time
2. On weekends, it sets "new cards per day" to 0 in deck options
3. On weekdays, it restores the original values
4. On first run, it saves a backup of your original settings
5. All changes sync via AnkiWeb to all your devices

### Why It Works on Mobile

- The addon runs only on desktop (iOS/Android don't support Python addons)
- **However**, deck configuration changes sync via AnkiWeb
- When you open Anki on mobile, it sees the already-modified settings
- This is why you need to open desktop Anki twice per week

## 📊 Configuration

Advanced users can edit settings via **Tools → Add-ons → Weekend Blocker → Config**:

```json
{
    "enabled": true,              // Enable/disable the addon
    "original_limits": {},        // Backup of original settings (auto-filled)
    "manual_pause": false,        // Manual pause mode state
    "last_run": null,            // Last execution timestamp
    "log_actions": true          // Enable action logging
}
```

## ❓ FAQ

<details>
<summary><b>Does this work on AnkiDroid/iOS?</b></summary>

The addon itself runs only on desktop, but the configuration changes sync via AnkiWeb. So yes, the behavior will be the same on mobile devices after syncing.
</details>

<details>
<summary><b>Can I customize which days are blocked?</b></summary>

Currently, Saturday and Sunday are hardcoded. To change this, edit `utils.py` and modify the `is_weekend()` function. We may add this as a configuration option in a future release.
</details>

<details>
<summary><b>What if I forget to open desktop Anki?</b></summary>

If you only use mobile for a week without opening desktop Anki, the new cards might appear (or not appear) depending on the last synced configuration. Try to maintain the 2x per week routine.
</details>

<details>
<summary><b>Can I apply this to specific decks only?</b></summary>

Not currently, but this is a planned feature. For now, it applies to all decks. If you need this, feel free to open an issue or submit a pull request!
</details>

<details>
<summary><b>Is my data safe?</b></summary>

Yes! The addon only modifies deck configuration settings (the "new cards per day" value). It never touches:
- Card content
- Review history
- Scheduling intervals
- Any actual card data

Your original settings are backed up on first run and can be restored at any time.
</details>

<details>
<summary><b>Something went wrong, how do I fix it?</b></summary>

1. **Tools → Weekend Blocker → Restaurar Configurações Originais**
2. This restores your original deck settings
3. If that doesn't work, check `actions.log` in the addon folder for details
4. You can also disable the addon temporarily: **Tools → Weekend Blocker → Desativar Addon**
</details>

## 🛡️ Security & Privacy

- ✅ No data is sent to external servers
- ✅ No network requests are made
- ✅ No personal information is collected
- ✅ All operations are local to your Anki installation
- ✅ Open source - you can review the code yourself

## 📝 Changelog

### Version 1.0.0 (2025)
- Initial release
- Automatic weekend detection
- Manual pause mode for vacations
- Dynamic menu interface
- Status dashboard with icons
- Action logging
- Automatic configuration backup

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

1. Clone the repository
2. Create a test Anki profile
3. Symlink the addon folder to your test profile's addons directory
4. Make changes and test
5. Submit a pull request

### Running Tests

```bash
python3 test_weekend_check.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with guidance from [Anki Add-on Documentation](https://addon-docs.ankiweb.net/)
- Developed for David Palis
- Created with assistance from Claude (Anthropic)

## 💬 Support

- 🐛 **Bug reports**: [Open an issue](https://github.com/yourusername/anki-weekend-blocker/issues)
- 💡 **Feature requests**: [Open an issue](https://github.com/yourusername/anki-weekend-blocker/issues)
- 📧 **Contact**: [Your email or preferred contact method]

## ⭐ Show Your Support

If you find this addon helpful, please consider:
- ⭐ Starring this repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 📢 Sharing with other Anki users

---

<div align="center">

**Made with ❤️ for the Anki community**

[Report Bug](https://github.com/yourusername/anki-weekend-blocker/issues) • [Request Feature](https://github.com/yourusername/anki-weekend-blocker/issues)

</div>
