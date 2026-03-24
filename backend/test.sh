#!/usr/bin/env -S bash -e

uv run coverage run --module behave --stop
echo
uv run coverage report --show-missing
