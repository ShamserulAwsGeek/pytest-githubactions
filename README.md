# Running pytest with GitHub Actions

This repository demonstrates how to run pytest tests using GitHub Actions for automated testing.

## Overview

- Automatically runs pytest on every push and pull request
- Ensures code quality and test coverage
- Supports multiple Python versions
- Reports test results in GitHub

## Setup

1. Place your pytest tests in `/tests` directory
2. Create GitHub Actions workflow in `.github/workflows/`
3. Configure pytest settings in `pytest.ini` or `setup.cfg`

## Example Workflow

```yaml
name: Tests

on: [push, pull_request]

jobs:
    test:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v2
            - name: Set up Python
                uses: actions/setup-python@v2
            - name: Install dependencies
                run: |
                    python -m pip install pytest
                    pip install -r requirements.txt
            - name: Run tests
                run: pytest
```

## Usage

Just push your code to GitHub - tests will run automatically!