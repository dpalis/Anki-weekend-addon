# Publication Checklist for Weekend Blocker

Use this checklist before publishing to GitHub and AnkiWeb.

## 📋 Pre-Publication Checklist

### Code Quality
- [x] All Python files have proper docstrings
- [x] Type hints are used consistently
- [x] Code follows PEP 8 style guidelines
- [x] No hardcoded credentials or secrets
- [x] Error handling is in place
- [x] No debug print statements in production code
- [x] All TODO comments are resolved or documented

### Security
- [x] Security audit completed (see SECURITY_AUDIT.md)
- [x] No external network requests
- [x] No SQL injection vulnerabilities
- [x] No command injection vulnerabilities
- [x] File operations are safe and limited
- [x] No eval() or exec() usage
- [x] Dependencies are minimal and trusted

### Testing
- [ ] Tested on fresh Anki installation
- [ ] Tested on Mac (primary development platform)
- [ ] Tested on Windows (if available)
- [ ] Tested on Linux (if available)
- [ ] Tested with Anki 2.1.50+
- [ ] Tested with Anki 25.02.7 (latest at time of release)
- [ ] Weekend detection works correctly
- [ ] Weekday restoration works correctly
- [ ] Manual pause/resume works
- [ ] Enable/disable functionality works
- [ ] Restore settings works
- [ ] Status display is accurate
- [ ] Menu updates dynamically
- [ ] AnkiWeb sync tested (desktop → mobile)
- [ ] Multiple deck configurations tested
- [ ] Error scenarios tested (missing config, etc.)

### Documentation
- [x] README.md is complete and clear
- [x] INSTALLATION.md has step-by-step instructions
- [x] CLAUDE.md has technical documentation
- [x] CONTRIBUTING.md has contribution guidelines
- [x] CHANGELOG.md is up to date
- [x] LICENSE file is included
- [x] Code comments are adequate
- [x] User-facing help is comprehensive
- [ ] Screenshots are included (add if needed)
- [ ] GIFs/videos of functionality (optional but recommended)

### Repository Setup
- [ ] Create GitHub repository
- [ ] Add appropriate topics/tags (anki, addon, python, study)
- [ ] Set repository description
- [ ] Enable Issues
- [ ] Enable Discussions (optional)
- [ ] Add repository URL to manifest.json and README.md
- [ ] Create initial release tag (v1.0.0)

### Files and Structure
- [x] .gitignore is comprehensive
- [x] All necessary files are committed
- [x] No unnecessary files are included (.pyc, __pycache__, etc.)
- [x] Folder structure is clean
- [x] manifest.json has correct metadata
- [ ] Version numbers are consistent across files

### Legal and Licensing
- [x] MIT License is included
- [x] Copyright year is correct (2025)
- [x] Author information is correct
- [x] License is referenced in source files
- [x] Third-party code is properly attributed (if any)

### AnkiWeb Preparation
- [ ] Package addon as .ankiaddon file
- [ ] Test installation from .ankiaddon file
- [ ] Prepare AnkiWeb description (max 5000 chars)
- [ ] Prepare short description (max 80 chars)
- [ ] Create screenshots for AnkiWeb listing
- [ ] Have AnkiWeb account ready

---

## 🚀 Publication Steps

### Step 1: Final Testing
```bash
# Run test script
python3 test_weekend_check.py

# Manual testing in Anki
# 1. Create test profile
# 2. Install addon
# 3. Test all features
# 4. Check logs for errors
```

### Step 2: Update Version Numbers
```bash
# Files to update:
# - weekend_blocker/manifest.json (version field)
# - CHANGELOG.md (add release date)
# - README.md (update version badge if needed)
```

### Step 3: Create GitHub Repository
```bash
git init
git add .
git commit -m "Initial release v1.0.0"
git branch -M main
git remote add origin https://github.com/yourusername/anki-weekend-blocker.git
git push -u origin main
```

### Step 4: Create GitHub Release
1. Go to repository on GitHub
2. Click "Releases" → "Create a new release"
3. Tag: `v1.0.0`
4. Title: `Weekend Blocker v1.0.0 - Initial Release`
5. Description: Copy from CHANGELOG.md
6. Attach .ankiaddon file
7. Publish release

### Step 5: Update URLs
After creating GitHub repo, update:
- [ ] README.md (replace `yourusername` with actual username)
- [ ] manifest.json (add homepage URL)
- [ ] Issue templates (if created)

### Step 6: AnkiWeb Submission (Optional)
1. Create .ankiaddon package:
   ```bash
   cd weekend_blocker
   zip -r ../weekend_blocker.ankiaddon *
   ```
2. Go to https://ankiweb.net/shared/upload
3. Log in with AnkiWeb account
4. Fill in addon details
5. Upload .ankiaddon file
6. Submit for review

---

## 📦 Creating .ankiaddon Package

### Manual Method
```bash
cd weekend_blocker
zip -r ../weekend_blocker.ankiaddon \
  __init__.py \
  core.py \
  ui.py \
  utils.py \
  config.json \
  config.md \
  manifest.json \
  README.md
```

### What to Include
- [x] All .py files
- [x] config.json
- [x] config.md
- [x] manifest.json
- [x] README.md (user documentation)
- [ ] __pycache__/ ❌ (exclude)
- [ ] *.pyc ❌ (exclude)
- [ ] .log files ❌ (exclude)

### Test Installation
1. Open Anki
2. Tools → Add-ons → Install from file
3. Select weekend_blocker.ankiaddon
4. Restart Anki
5. Verify it works

---

## ✅ Post-Publication Tasks

### Immediate
- [ ] Verify GitHub repository is public
- [ ] Verify release is published
- [ ] Test cloning the repository
- [ ] Test installing from GitHub release
- [ ] Share on social media (if desired)
- [ ] Share on Anki forums (if desired)

### Within First Week
- [ ] Monitor GitHub issues
- [ ] Respond to questions
- [ ] Fix any critical bugs
- [ ] Update documentation based on feedback

### Ongoing
- [ ] Maintain issue tracker
- [ ] Review pull requests
- [ ] Plan future features
- [ ] Keep dependencies updated
- [ ] Test with new Anki versions

---

## 🐛 Known Issues (to document)

Document any known issues that exist at release:

1. **Log file growth**: actions.log grows unbounded (low priority)
   - Workaround: Manually delete log file if it gets too large
   - Future: Add log rotation

2. **(Add any other known issues here)**

---

## 📊 Success Metrics

Track these after publication:

- GitHub stars
- GitHub forks
- GitHub issues (open/closed)
- AnkiWeb downloads (if published)
- User feedback
- Bug reports vs feature requests ratio

---

## 🎯 First Version Goals

For v1.0.0, success means:
- ✅ Code is secure and safe
- ✅ Core functionality works reliably
- ✅ Documentation is clear and complete
- ✅ Easy to install and use
- ✅ No critical bugs

Future improvements can be added based on user feedback!

---

**Ready to publish?** ✅

Make sure all checkboxes above are ticked, then proceed with publication steps!

Good luck! 🚀
