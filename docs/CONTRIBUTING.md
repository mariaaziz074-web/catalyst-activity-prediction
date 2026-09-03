# Contributing to Catalyst Activity Prediction

Thank you for your interest in contributing! This document outlines the guidelines for contributing to this project.

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in the Issues section
2. Open a new issue with a clear title and description
3. Include steps to reproduce the bug
4. Specify your environment (OS, Python version, package versions)
5. Include error messages and screenshots if applicable

### Suggesting Enhancements

1. Open an issue with the "enhancement" label
2. Describe the feature and its use case
3. Explain why this would be useful to users

### Pull Requests

1. Fork the repository
2. Create a new branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
4. Write or update tests as needed
5. Ensure all tests pass:
   ```bash
   pytest tests/ -v
   ```
6. Update documentation if needed
7. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.8+
- Git
- Virtual environment tool (venv or conda)

### Setup

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/yourusername/catalyst-activity.git
   cd catalyst-activity
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e ".[dev]"
   ```

4. Run tests to verify setup:
   ```bash
   pytest tests/ -v
   ```

## Coding Standards

### Python Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use [Black](https://black.readthedocs.io/) for code formatting
- Maximum line length: 88 characters (Black default)
- Use meaningful variable and function names

### Documentation

- All functions and classes must have docstrings
- Use Google-style or NumPy-style docstrings
- Update README.md if adding new features
- Add comments for complex logic

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor" not "Moves cursor")
- Limit first line to 72 characters
- Reference issues and pull requests where appropriate

Example:
```
Add input validation for pH range

- Add min/max validation for pH input (0-14)
- Add error message for out-of-range values
- Update tests for new validation

Fixes #123
```

## Testing

- Write unit tests for new functionality
- Ensure all tests pass before submitting PR
- Aim for >80% code coverage
- Test edge cases and error conditions

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html

# Run specific test file
pytest tests/test_model.py -v
```

## Model Contributions

When contributing to the model:

1. Document training data sources
2. Report performance metrics (R², RMSE, MAE)
3. Include feature importance analysis
4. Update the model card
5. Add tests for new features

## Documentation

- Keep README.md up to date
- Document new features in the docs/ folder
- Update data dictionary if features change
- Maintain the model card with current information

## Review Process

1. All submissions require review
2. Maintainers will provide feedback
3. Address review comments
4. Approved PRs will be merged

## Recognition

Contributors will be acknowledged in the project documentation.

## Questions?

Feel free to open an issue for any questions or concerns.

Thank you for contributing!
