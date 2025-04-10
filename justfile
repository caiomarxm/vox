set shell := ["bash", "-c"]

set positional-arguments


# List available commands
default:
  @just --list --unsorted


# -------------------------------------------
x----------------------------------------PREP:
    @just

# Install all dependencies
prep:
    @just prep-python

# Install Python dependencies
prep-python:
    @just python-recreate-venv
    @just python-install-deps

python-recreate-venv:
    uv venv

python-install-deps:
    uv pip install -r pyproject.toml

# -------------------------------------------
x---------------------------------------START:
    @just

# Start the dev server
start:
    @just start-app

# Start the dev server
start-app:
    uv run python ./src/app.py