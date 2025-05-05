# GitHub Actions Linting Demo

This project demonstrates the use of GitHub Actions for automated code linting.

## Project Structure

```
github_actions_demo/
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions workflow file
├── main.py            # Python file with intentional linting errors
└── README.md          # This file
```

## Workflow

The GitHub Actions workflow in this project:
1. Runs on every push to the repository
2. Sets up Python 3.11
3. Installs flake8 and pylint
4. Runs both linters on the code

## Linting Tools

- **flake8**: Checks for style issues and programming errors
- **pylint**: Performs comprehensive code analysis

## How to Test

1. The initial code has intentional linting errors
2. Push the code to see the workflow fail
3. Fix the linting errors and push again to see the workflow pass 