# Contributing to Weekend Blocker

First off, thank you for considering contributing to Weekend Blocker! It's people like you that make this addon better for everyone.

## Code of Conduct

This project adheres to a simple code of conduct:
- Be respectful and inclusive
- Assume good intentions
- Provide constructive feedback
- Focus on what's best for the community

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

**Bug Report Template:**
```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
 - OS: [e.g., macOS 14.0]
 - Anki Version: [e.g., 25.02.7]
 - Addon Version: [e.g., 1.0.0]

**Additional context**
- Check the `actions.log` file in the addon directory
- Any error messages from Anki's debug console
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

**Enhancement Template:**
```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Any alternative solutions or features you've considered.

**Additional context**
Any other context or screenshots about the feature request.
```

### Pull Requests

#### Before Submitting

1. Check existing PRs to avoid duplication
2. Test your changes thoroughly
3. Update documentation if needed
4. Follow the existing code style

#### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/anki-weekend-blocker.git
   cd anki-weekend-blocker
   ```

2. **Create a test Anki profile**
   - Open Anki
   - File → Switch Profile → Add
   - Name it "Weekend Blocker Dev"

3. **Symlink the addon for development**
   ```bash
   # Mac/Linux
   ln -s "$(pwd)/weekend_blocker" ~/Library/Application\ Support/Anki2/addons21/weekend_blocker_dev

   # Windows (run as Administrator)
   mklink /D "%APPDATA%\Anki2\addons21\weekend_blocker_dev" "path\to\weekend_blocker"
   ```

4. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Making Changes

1. **Write clear, commented code**
   - Use type hints
   - Add docstrings to functions
   - Follow PEP 8 style guidelines

2. **Test your changes**
   ```bash
   # Run the weekend detection test
   python3 test_weekend_check.py

   # Test in Anki
   # - Open Anki with your test profile
   # - Test the new functionality
   # - Check for errors in the debug console
   ```

3. **Update documentation**
   - Update README.md if needed
   - Update CLAUDE.md for technical changes
   - Add comments explaining complex logic

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add support for custom weekend days"
   ```

#### Commit Message Guidelines

Use conventional commits format:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation only
- `style:` Formatting, missing semicolons, etc.
- `refactor:` Code restructuring
- `test:` Adding tests
- `chore:` Maintenance tasks

Examples:
```
feat: add per-deck configuration option
fix: menu not updating after pause action
docs: update installation instructions for Linux
refactor: simplify weekend detection logic
```

#### Submit Pull Request

1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill in the PR template:

**PR Template:**
```markdown
**Description**
Brief description of changes.

**Type of change**
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

**How Has This Been Tested?**
- [ ] Tested on Mac
- [ ] Tested on Windows
- [ ] Tested on Linux
- [ ] Tested with multiple decks
- [ ] Tested weekend/weekday transitions

**Checklist:**
- [ ] My code follows the style guidelines
- [ ] I have commented my code where needed
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have tested my changes
```

## Code Style Guidelines

### Python Style

- Follow PEP 8
- Use type hints for function parameters and return values
- Maximum line length: 100 characters (soft limit)
- Use docstrings for all public functions

**Example:**
```python
def calculate_weekend_dates(weeks_ahead: int) -> List[datetime.date]:
    """
    Calculate weekend dates for the specified number of weeks ahead.

    Args:
        weeks_ahead: Number of weeks to calculate

    Returns:
        List of weekend dates (Saturdays and Sundays)
    """
    # Implementation
    pass
```

### File Organization

- Keep files focused and modular
- Separate UI code from business logic
- Use utility functions for common operations
- Avoid circular imports

### Error Handling

- Use try-except blocks for operations that might fail
- Log errors appropriately
- Provide helpful error messages to users
- Don't catch generic exceptions unless necessary

**Example:**
```python
try:
    config = get_addon_config()
except Exception as e:
    log_action("Error loading config", {"error": str(e)})
    show_warning("Could not load configuration. Using defaults.")
    config = get_default_config()
```

## Testing Guidelines

### Manual Testing Checklist

Before submitting, test:

- [ ] Fresh installation on test profile
- [ ] Weekend detection (Saturday/Sunday)
- [ ] Weekday detection (Monday-Friday)
- [ ] Manual pause/resume
- [ ] Enable/disable addon
- [ ] Restore original settings
- [ ] Multiple deck configurations
- [ ] AnkiWeb sync behavior
- [ ] Menu updates dynamically
- [ ] Status display is accurate
- [ ] All error scenarios

### Test Cases to Consider

1. **Edge Cases**
   - Empty deck
   - Deck with 0 new cards configured
   - Addon disabled
   - Manual pause active
   - No original_limits saved

2. **User Workflows**
   - Normal weekly usage
   - Vacation mode activation/deactivation
   - Configuration restore
   - First-time setup

3. **Platform-Specific**
   - Different Anki versions
   - Different operating systems
   - Different timezone scenarios

## Documentation

### What to Document

- New features and how to use them
- API changes (if adding hooks or callbacks)
- Configuration options
- Breaking changes
- Migration guides (if needed)

### Where to Document

- `README.md`: User-facing documentation
- `CLAUDE.md`: Technical documentation for future development
- `CHANGELOG.md`: Track all changes between versions
- Code comments: Complex logic and "why" not just "what"

## Release Process

(For maintainers)

1. Update version in `manifest.json`
2. Update `CHANGELOG.md`
3. Create git tag: `git tag v1.x.x`
4. Push tag: `git push origin v1.x.x`
5. Create GitHub release with release notes
6. Package addon for AnkiWeb
7. Submit to AnkiWeb (if applicable)

## Questions?

- Open an issue with the `question` label
- Check existing issues and discussions
- Contact: [Your preferred contact method]

## Recognition

Contributors will be recognized in:
- README.md (Contributors section)
- Release notes
- Git commit history

Thank you for contributing! 🎉
