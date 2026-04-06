# Contributing to SHD Screening AI

Thank you for your interest in contributing to the **SHD Screening AI** project! We welcome contributions from everyone. This document provides guidelines and instructions for contributing.

## 🎯 How to Contribute

### 1. **Report a Bug**
- Check if the issue already exists in [GitHub Issues](https://github.com/Anannya-Vyas/shd-heart-disease-prediction-/issues)
- Click **"New Issue"** and select **"Bug Report"**
- Provide:
  - Clear description of the bug
  - Steps to reproduce
  - Expected vs actual behavior
  - Screenshots (if applicable)
  - Your environment (OS, browser, Python version)

### 2. **Suggest a Feature**
- Open a new issue with **"Feature Request"** label
- Describe:
  - The problem it solves
  - Why it would be useful
  - Suggested implementation (if you have ideas)

### 3. **Improve Documentation**
- Found a typo or unclear explanation?
- Submit a pull request to fix README.md or code comments
- Add examples or clarifications

### 4. **Submit Code Changes**

#### Fork the Repository
```bash
# Click "Fork" button on GitHub
# Clone your fork
git clone https://github.com/YOUR-USERNAME/shd-heart-disease-prediction-.git
cd shd-heart-disease-prediction-
```

#### Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

#### Make Your Changes
1. Make small, focused commits
2. Write clear commit messages:
   ```
   git commit -m "Fix: Resolve API timeout issue"
   git commit -m "Feature: Add export to CSV functionality"
   ```

#### Test Your Changes
```bash
# Run the app locally
cd shd-hf
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m uvicorn app:app --reload
```

#### Push and Create a Pull Request
```bash
git push origin feature/your-feature-name
```
- Go to GitHub and click **"Create Pull Request"**
- Provide:
  - Clear title and description
  - Link to related issue (if any)
  - Screenshots/videos (if UI changes)

## 📋 Code Guidelines

### Style & Formatting
- **Python**: Follow PEP 8 style guide
- **JavaScript**: Use consistent indentation (2 spaces)
- **HTML/CSS**: Keep markup clean and semantic

### Commit Messages
```
[Type]: Brief description (50 chars max)

Longer explanation of changes (optional)
- Detail 1
- Detail 2

Related Issue: #123
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### Functions & Classes
- Add docstrings explaining purpose, parameters, and return values
- Write self-documenting code with clear variable names
- Add comments for complex logic

## 🐛 Reporting Bugs

Include these details:
1. **What happened?** - Describe the bug clearly
2. **How to reproduce?** - Step-by-step instructions
3. **Expected behavior** - What should happen
4. **Actual behavior** - What actually happens
5. **Environment**:
   - OS (Windows, macOS, Linux)
   - Browser (Chrome, Firefox, Safari)
   - Python version
   - Any error messages

Example:
```
Title: "Analysis fails when health data contains special characters"

Description:
When I enter a name with an apostrophe (e.g., "O'Brien"), 
the API call fails with a 400 error.

Steps:
1. Fill in demographics form
2. Enter "O'Brien" in the Name field
3. Progress to analysis
4. Click "Analyze Heart Health"

Expected: Analysis completes successfully
Actual: Error message: "Bad Request"
```

## 📝 Pull Request Process

1. **Update README.md** if adding new features
2. **Add tests** for new functionality (if applicable)
3. **Keep commits clean** - rebase if needed
4. **One feature per PR** - easier to review
5. **Respond to feedback** - maintainers may request changes

## 🎨 Areas for Contribution

### High Priority
- [ ] Unit and integration tests
- [ ] Additional AI model support
- [ ] Mobile app optimization
- [ ] Multi-language support
- [ ] Dark mode theme

### Medium Priority
- [ ] Performance optimizations
- [ ] Additional health metrics
- [ ] User authentication system
- [ ] Data visualization improvements
- [ ] API rate limiting

### Low Priority
- [ ] UI/UX improvements
- [ ] Documentation enhancement
- [ ] Code cleanup
- [ ] Example use cases

## 💡 Development Tips

### Local Development
```bash
# Install dependencies with dev packages
pip install -r requirements.txt

# Run tests (when added)
pytest shd-hf/tests/

# Check code style
flake8 shd-hf/app.py
```

### File Structure
```
shd-heart-disease-prediction-/
├── shd-hf/
│   ├── app.py              # FastAPI backend
│   ├── requirements.txt    # Dependencies
│   └── static/
│       └── index.html      # Frontend UI
└── README.md               # Documentation
```

### Common Tasks
- **Change the AI model**: Update `model="google/gemma-2-2b-it"` in `app.py`
- **Add a new health metric**: Add field to HTML form and include in prompt
- **Customize styling**: Edit CSS variables in `index.html` (`:root` section)

## 🤝 Community Guidelines

- **Be respectful** - All contributors deserve respect
- **Ask questions** - No question is too basic
- **Help others** - Answer questions in issues
- **Stay on topic** - Keep discussions relevant to the issue
- **No spam** - No advertising or self-promotion

## 📞 Questions?

- 📧 **Email**: Check repository for contact info
- 💬 **Issues**: Ask in GitHub issues
- 📖 **Documentation**: Check README.md and code comments
- 🔗 **GitHub**: [@Anannya-Vyas](https://github.com/Anannya-Vyas)

## 🙏 Thank You!

Contributors are the backbone of open-source. Your time and effort help make healthcare technology better for everyone!

---

**Happy Contributing!** 🎉

For more information, see [README.md](README.md)
